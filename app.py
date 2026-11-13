from flask import Flask, render_template_string
from processor import bp

app = Flask(__name__)
app.register_blueprint(bp)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>استوديو كيان - SVGA وتفريغ الفيديو</title>
    <style>
        body { font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .card { background: #1e293b; border-radius: 16px; padding: 24px; width: 100%; max-width: 450px; border: 1px solid #334155; }
        h1 { font-size: 22px; text-align: center; color: #38bdf8; margin-bottom: 8px; }
        p.sub { text-align: center; color: #94a3b8; font-size: 14px; margin-bottom: 24px; }
        .box { border: 2px dashed #475569; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 18px; background: #0f172a; }
        .box input { width: 100%; color: #cbd5e1; }
        label { display: block; margin-bottom: 8px; font-weight: bold; font-size: 14px; }
        select, input[type="range"] { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #475569; background: #0f172a; color: #fff; font-size: 15px; margin-bottom: 18px; box-sizing: border-box; }
        button { width: 100%; padding: 14px; border: none; border-radius: 12px; background: linear-gradient(135deg, #0284c7, #6366f1); color: white; font-size: 16px; font-weight: bold; cursor: pointer; }
        button:disabled { opacity: 0.6; }
        #status { margin-top: 16px; text-align: center; font-size: 14px; color: #38bdf8; }
    </style>
</head>
<body>
    <div class="card">
        <h1>استوديو كيان الذكي</h1>
        <p class="sub">تفريغ جميع ألوان الخلفيات وتصدير SVGA 2.0 قياسي</p>
        <form id="uploadForm">
            <label>1. اختر الفيديو من هاتفك:</label>
            <div class="box"><input type="file" id="videoFile" name="file" accept="video/*" required></div>
            <label>2. اختر نوع المعالجة المطلوبة:</label>
            <select name="mode" id="mode">
                <option value="svga">تحويل إلى ملف SVGA 2.0 (بدون خلفية)</option>
                <option value="video_only">حذف خلفية الفيديو فقط (تصدير فيديو شفاف WebM)</option>
            </select>
            <label>3. دقة عزل الخلفية (الحساسية: <span id="tolVal">45</span>):</label>
            <input type="range" name="tolerance" id="tolerance" min="15" max="90" value="45" oninput="document.getElementById('tolVal').innerText=this.value">
            <button type="submit" id="submitBtn">بدء المعالجة والتحميل</button>
        </form>
        <div id="status"></div>
    </div>
    <script>
        document.getElementById('uploadForm').onsubmit = async (e) => {
            e.preventDefault();
            const btn = document.getElementById('submitBtn');
            const status = document.getElementById('status');
            btn.disabled = true;
            status.innerText = "جاري تحليل الإطارات وعزل الخلفية... يرجى الانتظار";
            const formData = new FormData(e.target);
            try {
                const res = await fetch('/process', { method: 'POST', body: formData });
                if (!res.ok) { const err = await res.json(); throw new Error(err.error || "فشلت المعالجة"); }
                const blob = await res.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                const mode = document.getElementById('mode').value;
                a.download = mode === 'video_only' ? 'Kayan_Transparent.webm' : 'Kayan_Animation.svga';
                document.body.appendChild(a); a.click(); a.remove();
                status.innerText = "✅ تم التصدير بنجاح!";
            } catch (err) { status.innerText = "❌ " + err.message; }
            finally { btn.disabled = false; }
        };
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)
