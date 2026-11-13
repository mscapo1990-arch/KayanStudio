import os, uuid
from flask import Blueprint, request, send_file, jsonify
from engine import process_video_task

bp = Blueprint("processor", __name__)
BASE_TEMP = "/tmp/kayan_jobs"
os.makedirs(BASE_TEMP, exist_ok=True)

@bp.route("/process", methods=["POST"])
def process_media():
    if "file" not in request.files:
        return jsonify({"error": "يرجى اختيار ملف فيديو أولاً"}), 400
    file = request.files["file"]
    mode = request.form.get("mode", "svga")
    tolerance = int(request.form.get("tolerance", 45))
    job_id = str(uuid.uuid4())
    job_dir = os.path.join(BASE_TEMP, job_id)
    os.makedirs(job_dir, exist_ok=True)
    input_path = os.path.join(job_dir, "input_video.mp4")
    file.save(input_path)
    try:
        output_path = process_video_task(input_path, job_dir, mode=mode, tolerance=tolerance)
        download_name = "Kayan_Transparent.webm" if mode == "video_only" else "Kayan_Animation.svga"
        return send_file(output_path, as_attachment=True, download_name=download_name)
    except Exception as e:
        return jsonify({"error": f"خطأ: {str(e)}"}), 500
