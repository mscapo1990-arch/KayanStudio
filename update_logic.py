import os

# تحديث صفحة المحول لتصبح تفاعلية بالكامل
converter_code = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>محول صيغ الصور إلى SVGA - استوديو كيان</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #090d16; color: #f3f4f6; }
        .gold-btn { background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%); color: #111827; font-weight: 700; transition: all 0.3s ease; }
        .gold-btn:hover { background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%); box-shadow: 0 0 20px rgba(251, 191, 36, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-gray-800 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-amber-600">KAYAN STUDIO | محول الصور</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-3xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="card-custom rounded-2xl p-8 border-amber-500/30 shadow-2xl">
            <div class="text-center mb-8">
                <div class="w-16 h-16 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center mx-auto mb-4 text-2xl">⚡</div>
                <h1 class="text-2xl font-bold mb-2">محول صيغ الصور المتعددة إلى SVGA</h1>
                <p class="text-gray-400 text-sm">قم برفع أي صورة (PNG, JPG, WEBP, GIF) ليتم تحويلها ومعالجتها فورا</p>
            </div>
            
            <form action="/convert" method="POST" enctype="multipart/form-data" id="uploadForm">
                <div onclick="document.getElementById('fileInput').click()" class="border-2 border-dashed border-gray-700 hover:border-amber-500/50 rounded-2xl p-8 text-center cursor-pointer transition mb-6 bg-[#0e1626]">
                    <span class="text-3xl mb-2 block">📁</span>
                    <p id="fileName" class="text-sm font-semibold text-gray-300">اضغط لاختيار الصور أو اسحبها هنا</p>
                    <p class="text-xs text-gray-500 mt-1">تدعم كافة الصيغ الشهيرة بجودة عالية</p>
                    <input type="file" name="image" id="fileInput" class="hidden" accept="image/*" onchange="showFileName(this)">
                </div>
                <button type="submit" class="gold-btn w-full py-3 rounded-xl text-base shadow-lg cursor-pointer">بدء التحويل الآن ⚡</button>
            </form>
        </div>
    </main>
    <footer class="border-t border-gray-800 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
    
    <script>
        function showFileName(input) {
            if (input.files && input.files[0]) {
                document.getElementById('fileName').innerText = "الملف المختار: " + input.files[0].name;
            }
        }
    </script>
</body>
</html>
'''

with open('templates/converter.html', 'w', encoding='utf-8') as f:
    f.write(converter_code)

print("Converter interface updated with interactive JS!")
