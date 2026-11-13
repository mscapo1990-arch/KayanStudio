import os, uuid
from flask import Blueprint, request, send_file, jsonify
from engine import process_media_task

bp = Blueprint("processor", __name__)
BASE_TEMP = "/tmp/kayan_jobs"
os.makedirs(BASE_TEMP, exist_ok=True)

@bp.route("/process", methods=["POST"])
def process_media():
    files = request.files.getlist("files")
    if not files or not files[0].filename:
        return jsonify({"error": "يرجى اختيار ملف واحد على الأقل"}), 400
    mode = request.form.get("mode", "images_svga")
    remove_bg = request.form.get("remove_bg") == "true"
    tolerance = int(request.form.get("tolerance", 45))
    job_dir = os.path.join(BASE_TEMP, str(uuid.uuid4()))
    os.makedirs(job_dir, exist_ok=True)
    paths = []
    for idx, f in enumerate(files):
        ext = os.path.splitext(f.filename)[1] or ".png"
        p = os.path.join(job_dir, f"in_{idx}{ext}")
        f.save(p)
        paths.append(p)
    try:
        out = process_media_task(paths, job_dir, mode=mode, remove_bg=remove_bg, tolerance=tolerance)
        name = "Kayan_Transparent.webm" if mode == "video_only" else "Kayan_Animation.svga"
        return send_file(out, as_attachment=True, download_name=name)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
