import os
import zlib
import struct
import subprocess
import numpy as np
from PIL import Image

def remove_background_smart(img: Image.Image, tolerance: int = 45) -> Image.Image:
    rgba = img.convert("RGBA")
    data = np.array(rgba, dtype=np.float32)
    h, w, _ = data.shape
    corners = np.vstack([
        data[0:5, 0:5, :3].reshape(-1, 3),
        data[0:5, w-5:w, :3].reshape(-1, 3),
        data[h-5:h, 0:5, :3].reshape(-1, 3),
        data[h-5:h, w-5:w, :3].reshape(-1, 3)
    ])
    bg_color = np.median(corners, axis=0)
    diff = np.linalg.norm(data[:, :, :3] - bg_color, axis=2)
    low_thresh = tolerance * 0.7
    high_thresh = tolerance * 1.4
    alpha = np.clip((diff - low_thresh) / (high_thresh - low_thresh + 1e-5), 0.0, 1.0) * 255.0
    data[:, :, 3] = np.minimum(data[:, :, 3], alpha)
    return Image.fromarray(data.astype(np.uint8), "RGBA")

def _encode_varint(value: int) -> bytes:
    out = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            out.append(byte | 0x80)
        else:
            out.append(byte)
            break
    return bytes(out)

def _pb_bytes(field_num: int, data: bytes) -> bytes:
    return _encode_varint((field_num << 3) | 2) + _encode_varint(len(data)) + data

def _pb_string(field_num: int, text: str) -> bytes:
    return _pb_bytes(field_num, text.encode("utf-8"))

def _pb_int(field_num: int, val: int) -> bytes:
    return _encode_varint((field_num << 3) | 0) + _encode_varint(val)

def _pb_float(field_num: int, val: float) -> bytes:
    return _encode_varint((field_num << 3) | 5) + struct.pack("<f", val)

def create_svga_from_images(image_paths: list, output_path: str, fps: int = 15):
    if not image_paths:
        raise ValueError("لا توجد إطارات")
    first_img = Image.open(image_paths[0])
    width, height = first_img.size
    total_frames = len(image_paths)
    params_pb = _pb_float(1, float(width)) + _pb_float(2, float(height)) + _pb_int(3, fps) + _pb_int(4, total_frames)
    movie_pb = bytearray()
    movie_pb.extend(_pb_string(1, "2.0.0"))
    movie_pb.extend(_pb_bytes(2, params_pb))
    transform_pb = _pb_float(1, 1.0) + _pb_float(4, 1.0)
    layout_pb = _pb_float(3, float(width)) + _pb_float(4, float(height))

    for idx, img_path in enumerate(image_paths):
        key = f"img_{idx}"
        with open(img_path, "rb") as f:
            png_bytes = f.read()
        movie_pb.extend(_pb_bytes(3, _pb_string(1, key) + _pb_bytes(2, png_bytes)))
        frames_pb = bytearray()
        for f_idx in range(total_frames):
            alpha_val = 1.0 if f_idx == idx else 0.0
            frames_pb.extend(_pb_bytes(3, _pb_float(1, alpha_val) + _pb_bytes(2, layout_pb) + _pb_bytes(3, transform_pb)))
        movie_pb.extend(_pb_bytes(4, _pb_string(1, key) + bytes(frames_pb)))

    with open(output_path, "wb") as f:
        f.write(zlib.compress(bytes(movie_pb), level=6))

def process_video_task(video_path: str, work_dir: str, mode: str = "svga", tolerance: int = 45) -> str:
    frames_dir = os.path.join(work_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-i", video_path, "-vf", "fps=15,scale='min(500,iw)':-2", os.path.join(frames_dir, "raw_%04d.png")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    raw_files = sorted([os.path.join(frames_dir, f) for f in os.listdir(frames_dir) if f.startswith("raw_")])
    if not raw_files:
        raise RuntimeError("فشل استخراج الإطارات")
    clean_files = []
    for idx, rf in enumerate(raw_files):
        clean_img = remove_background_smart(Image.open(rf), tolerance=tolerance)
        clean_path = os.path.join(frames_dir, f"clean_{idx:04d}.png")
        clean_img.save(clean_path, "PNG")
        clean_files.append(clean_path)

    if mode == "video_only":
        out_video = os.path.join(work_dir, "transparent_video.webm")
        subprocess.run(["ffmpeg", "-y", "-framerate", "15", "-i", os.path.join(frames_dir, "clean_%04d.png"), "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "1M", out_video], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return out_video
    else:
        out_svga = os.path.join(work_dir, "animation.svga")
        create_svga_from_images(clean_files, out_svga, fps=15)
        return out_svga
