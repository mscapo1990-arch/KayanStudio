import os, zlib, struct, subprocess
import numpy as np
from PIL import Image, ImageSequence

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
    low_t, high_t = tolerance * 0.7, tolerance * 1.4
    alpha = np.clip((diff - low_t) / (high_t - low_t + 1e-5), 0.0, 1.0) * 255.0
    data[:, :, 3] = np.minimum(data[:, :, 3], alpha)
    return Image.fromarray(data.astype(np.uint8), "RGBA")

def _varint(v: int) -> bytes:
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v: out.append(b | 0x80)
        else: out.append(b); break
    return bytes(out)

def _pb_bytes(n: int, d: bytes) -> bytes:
    return _varint((n << 3) | 2) + _varint(len(d)) + d

def _pb_str(n: int, t: str) -> bytes:
    return _pb_bytes(n, t.encode("utf-8"))

def _pb_int(n: int, v: int) -> bytes:
    return _varint((n << 3) | 0) + _varint(v)

def _pb_flt(n: int, v: float) -> bytes:
    return _varint((n << 3) | 5) + struct.pack("<f", v)

def create_svga_from_images(image_paths: list, output_path: str, fps: int = 15):
    w, h = Image.open(image_paths[0]).size
    total = len(image_paths)
    params = _pb_flt(1, float(w)) + _pb_flt(2, float(h)) + _pb_int(3, fps) + _pb_int(4, total)
    movie = bytearray(_pb_str(1, "2.0.0") + _pb_bytes(2, params))
    trans = _pb_flt(1, 1.0) + _pb_flt(4, 1.0)
    layout = _pb_flt(3, float(w)) + _pb_flt(4, float(h))

    for idx, p in enumerate(image_paths):
        key = f"img_{idx}"
        with open(p, "rb") as f: png = f.read()
        movie.extend(_pb_bytes(3, _pb_str(1, key) + _pb_bytes(2, png)))
        frames = bytearray()
        for f_idx in range(total):
            a = 1.0 if f_idx == idx else 0.0
            frames.extend(_pb_bytes(3, _pb_flt(1, a) + _pb_bytes(2, layout) + _pb_bytes(3, trans)))
        movie.extend(_pb_bytes(4, _pb_str(1, key) + bytes(frames)))

    with open(output_path, "wb") as f:
        f.write(zlib.compress(bytes(movie), level=6))

def process_media_task(file_paths: list, work_dir: str, mode: str = "svga", remove_bg: bool = True, tolerance: int = 45) -> str:
    f_dir = os.path.join(work_dir, "frames")
    os.makedirs(f_dir, exist_ok=True)
    raw_files = []

    if mode == "images_svga":
        idx, base_size = 0, None
        for fp in file_paths:
            for frame in ImageSequence.Iterator(Image.open(fp)):
                rgba = frame.convert("RGBA")
                if base_size is None:
                    w, h = rgba.size
                    s = min(1.0, 600 / max(w, h))
                    base_size = (int(w * s), int(h * s))
                rp = os.path.join(f_dir, f"raw_{idx:04d}.png")
                rgba.resize(base_size, Image.Resampling.LANCZOS).save(rp, "PNG")
                raw_files.append(rp)
                idx += 1
    else:
        subprocess.run(["ffmpeg", "-y", "-i", file_paths[0], "-vf", "fps=15,scale='min(500,iw)':-2", os.path.join(f_dir, "raw_%04d.png")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        raw_files = sorted([os.path.join(f_dir, f) for f in os.listdir(f_dir) if f.startswith("raw_")])

    clean_files = []
    for idx, rf in enumerate(raw_files):
        im = Image.open(rf)
        out_im = remove_background_smart(im, tolerance) if remove_bg else im.convert("RGBA")
        cp = os.path.join(f_dir, f"clean_{idx:04d}.png")
        out_im.save(cp, "PNG")
        clean_files.append(cp)

    if mode == "video_only":
        out_v = os.path.join(work_dir, "out.webm")
        subprocess.run(["ffmpeg", "-y", "-framerate", "15", "-i", os.path.join(f_dir, "clean_%04d.png"), "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "1M", out_v], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return out_v
    out_s = os.path.join(work_dir, "out.svga")
    create_svga_from_images(clean_files, out_s, fps=10 if mode == "images_svga" else 15)
    return out_s
