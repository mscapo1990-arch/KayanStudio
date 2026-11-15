import zlib
import struct
import io
from PIL import Image

def _encode_varint(value):
    bits = value & 0x7f
    value >>= 7
    res = bytearray()
    while value:
        res.append(0x80 | bits)
        bits = value & 0x7f
        value >>= 7
    res.append(bits)
    return bytes(res)

def _encode_key(field_number, wire_type):
    return _encode_varint((field_number << 3) | wire_type)

def _encode_bytes(field_number, data):
    return _encode_key(field_number, 2) + _encode_varint(len(data)) + data

def _encode_string(field_number, text):
    return _encode_bytes(field_number, text.encode('utf-8'))

def _encode_float(field_number, val):
    return _encode_key(field_number, 5) + struct.pack('<f', val)

def _encode_int32(field_number, val):
    return _encode_key(field_number, 0) + _encode_varint(val)

def create_svga_from_images(image_list, output_path, fps=20):
    if not image_list:
        raise ValueError("لا توجد صور للتحويل")
    
    width, height = image_list[0].size
    frames_count = len(image_list)
    
    # 1. بناء MovieParams
    params_data = (
        _encode_float(1, float(width)) +
        _encode_float(2, float(height)) +
        _encode_int32(3, fps) +
        _encode_int32(4, frames_count)
    )
    
    movie_spec = _encode_string(1, "2.0.0") + _encode_bytes(2, params_data)
    
    # 2. إضافة الصور (images map) وبناء الإطارات (sprites)
    sprites_data = b""
    for idx, img in enumerate(image_list):
        img_rgba = img.convert("RGBA").resize((width, height))
        buf = io.BytesIO()
        img_rgba.save(buf, format="PNG")
        png_bytes = buf.getvalue()
        
        img_key = f"img_{idx}"
        # MapEntry: key=1 (string), value=2 (bytes)
        map_entry = _encode_string(1, img_key) + _encode_bytes(2, png_bytes)
        movie_spec += _encode_bytes(3, map_entry)
        
        # بناء Sprite لكل صورة تظهر في إطارها المحدد فقط
        frames_proto = b""
        transform_proto = (
            _encode_float(1, 1.0) + # a
            _encode_float(4, 1.0)   # d
        )
        layout_proto = (
            _encode_float(3, float(width)) +
            _encode_float(4, float(height))
        )
        
        for f_idx in range(frames_count):
            alpha = 1.0 if f_idx == idx else 0.0
            frame_item = (
                _encode_float(1, alpha) +
                _encode_bytes(2, layout_proto) +
                _encode_bytes(3, transform_proto)
            )
            frames_proto += _encode_bytes(1, frame_item)
            
        sprite_entity = _encode_string(1, img_key) + frames_proto
        sprites_data += _encode_bytes(4, sprite_entity)
        
    full_proto = movie_spec + sprites_data
    compressed_data = zlib.compress(full_proto)
    
    with open(output_path, "wb") as f:
        f.write(compressed_data)
    return output_path
import numpy as np
from PIL import Image

def remove_background_smart(input_image: Image.Image, tolerance: int = 45) -> Image.Image:
    """
    إزالة الخلفية تلقائياً بالاعتماد على لون الزوايا مع تنعيم الحواف
    """
    img = input_image.convert("RGBA")
    data = np.array(img, dtype=np.float32)
    
    # أخذ لون الخلفية من الزاوية العلوية اليسرى
    bg_color = data[0, 0, :3]
    
    # حساب المسافة اللونية لكل بكسل
    diff = np.sqrt(np.sum((data[:, :, :3] - bg_color) ** 2, axis=2))
    
    # إنشاء قناة الشفافية (Alpha) مع تدرج ناعم للحواف
    alpha = np.clip((diff - tolerance * 0.6) / (tolerance * 0.4) * 255, 0, 255)
    
    # دمج الشفافية الجديدة مع الشفافية الأصلية إن وجدت
    data[:, :, 3] = np.minimum(data[:, :, 3], alpha)
    
    result = Image.fromarray(data.astype(np.uint8), "RGBA")
    return result
