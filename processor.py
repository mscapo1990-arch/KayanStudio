from flask import Blueprint, request, send_file, jsonify
from PIL import Image, ImageSequence
import io
import os
import uuid
from engine import remove_background_smart
from engine import create_svga_from_images

bp = Blueprint('processor', __name__, url_prefix='/api')
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@bp.route("/image-to-svga", methods=["POST"])
def image_to_svga():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    file = request.files['file']
    fps = int(request.form.get('fps', 20))
    
    img = Image.open(io.BytesIO(file.read()))
    frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        
    file_id = str(uuid.uuid4())[:8]
    out_path = os.path.join(OUTPUT_DIR, f"kayan_{file_id}.svga")
    create_svga_from_images(frames, out_path, fps=fps)
    
    return send_file(os.path.abspath(out_path), as_attachment=True, download_name=f"kayan_{file_id}.svga")

@bp.route("/remove-bg", methods=["POST"])
def remove_bg():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    file = request.files['file']
    tolerance = int(request.form.get('tolerance', 45))
    
    img = Image.open(io.BytesIO(file.read()))
    result_img = remove_background_smart(img, tolerance=tolerance)
    
    file_id = str(uuid.uuid4())[:8]
    out_path = os.path.join(OUTPUT_DIR, f"nobg_{file_id}.png")
    result_img.save(out_path, format="PNG")
    
    return send_file(os.path.abspath(out_path), as_attachment=True, download_name=f"nobg_{file_id}.png")

@bp.route("/remove-bg-and-svga", methods=["POST"])
def remove_bg_and_svga():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    file = request.files['file']
    tolerance = int(request.form.get('tolerance', 45))
    fps = int(request.form.get('fps', 20))
    
    img = Image.open(io.BytesIO(file.read()))
    frames = [remove_background_smart(frame.copy(), tolerance=tolerance) for frame in ImageSequence.Iterator(img)]
        
    file_id = str(uuid.uuid4())[:8]
    out_path = os.path.join(OUTPUT_DIR, f"kayan_clean_{file_id}.svga")
    create_svga_from_images(frames, out_path, fps=fps)
    
    return send_file(os.path.abspath(out_path), as_attachment=True, download_name=f"kayan_clean_{file_id}.svga")
