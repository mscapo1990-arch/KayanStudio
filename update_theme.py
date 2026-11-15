import os

# 1. تحديث الصفحة الرئيسية index.html
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>استوديو كيان الذكي - Kayan Studio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #090d16; color: #f3f4f6; }
        .royal-btn { background: linear-gradient(135deg, #991b1b 0%, #b45309 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; text-align: center; display: block; }
        .royal-btn:hover { background: linear-gradient(135deg, #7f1d1d 0%, #92400e 100%); box-shadow: 0 0 20px rgba(180, 83, 9, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; transition: all 0.3s ease; }
        .card-custom:hover { border-color: #b45309; box-shadow: 0 10px 25px -5px rgba(153, 27, 27, 0.2); }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-red-900/40 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-red-600">KAYAN STUDIO</span>
            <nav class="hidden md:flex space-x-6 space-x-reverse text-sm text-gray-300">
                <a href="#" class="hover:text-amber-400 transition">الرئيسية</a>
                <a href="/player" class="hover:text-amber-400 transition">المشغل</a>
                <a href="/extractor" class="hover:text-amber-400 transition">المستخرج</a>
                <a href="/converter" class="text-amber-400 font-bold">المحول</a>
            </nav>
            <button class="bg-red-900/40 border border-red-700/50 hover:bg-red-800 text-amber-300 px-4 py-2 rounded-xl text-sm font-semibold transition">دخول</button>
        </div>
    </header>
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <div class="text-center mb-16">
            <h1 class="text-3xl sm:text-5xl font-extrabold mb-4 tracking-tight">احترافية كاملة في معالجة ملفات <span class="text-amber-400">SVGA</span></h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-sm sm:text-base">المنصة الملكية لاستخراج، تحويل، ومعاينة ملفات الـ SVGA بدقة سينمائية مذهلة.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-red-900/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-red-900/20 text-red-500 flex items-center justify-center mb-4 text-xl">🖼️</div>
                    <h3 class="text-lg font-bold mb-2">تحويل الصور إلى SVGA</h3>
                    <p class="text-gray-400 text-sm mb-6">اختر صورة أو عدة صور مع تفريغ الخلفية تلقائياً وتحويلها بدقة عالية.</p>
                </div>
                <a href="/converter" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-amber-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4 text-xl">⚡</div>
                    <h3 class="text-lg font-bold mb-2">محول صيغ الصور المتعددة</h3>
                    <p class="text-gray-400 text-sm mb-6">تحويل كافة صيغ الصور (PNG, JPG, WEBP, GIF) إلى SVGA بضغطة واحدة.</p>
                </div>
                <a href="/converter" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">تحويل الآن ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-red-900/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-red-900/20 text-red-400 flex items-center justify-center mb-4 text-xl">🎬</div>
                    <h3 class="text-lg font-bold mb-2">المشغل السينمائي</h3>
                    <p class="text-gray-400 text-sm mb-6">معاينة ملفات SVGA، التحكم في الإطارات، وتحويل الفيديوهات لغرف الدردشة.</p>
                </div>
                <a href="/player" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-amber-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4 text-xl">📦</div>
                    <h3 class="text-lg font-bold mb-2">مستخرج ملفات SVGA</h3>
                    <p class="text-gray-400 text-sm mb-6">استخراج الصور، الأصول، والأصوات من ملفات الـ SVGA وتنزيلها بجودة عالية.</p>
                </div>
                <a href="/extractor" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
        </div>
    </main>
    <footer class="border-t border-red-900/30 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو (Kayan Studio) 2026</footer>
</body>
</html>
''')

# 2. تحديث صفحة المحول converter.html
with open('templates/converter.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>محول صيغ الصور إلى SVGA - استوديو كيان</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #090d16; color: #f3f4f6; }
        .royal-btn { background: linear-gradient(135deg, #991b1b 0%, #b45309 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; }
        .royal-btn:hover { background: linear-gradient(135deg, #7f1d1d 0%, #92400e 100%); box-shadow: 0 0 20px rgba(180, 83, 9, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-red-900/40 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-red-600">KAYAN STUDIO | محول الصور</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-3xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="card-custom rounded-2xl p-8 border-amber-500/30 shadow-2xl">
            <div class="text-center mb-8">
                <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-red-900/40 to-amber-500/20 text-amber-400 flex items-center justify-center mx-auto mb-4 text-2xl border border-amber-500/30">⚡</div>
                <h1 class="text-2xl font-bold mb-2">محول صيغ الصور المتعددة إلى SVGA</h1>
                <p class="text-gray-400 text-sm">قم برفع أي صورة (PNG, JPG, WEBP, GIF) ليتم تحويلها ومعالجتها فورا</p>
            </div>
            
            <form action="/convert" method="POST" enctype="multipart/form-data">
                <label for="fileInput" class="border-2 border-dashed border-red-900/50 hover:border-amber-500/50 rounded-2xl p-8 text-center cursor-pointer transition mb-6 bg-[#0e1626] block">
                    <span class="text-3xl mb-2 block">📁</span>
                    <span id="fileName" class="text-sm font-semibold text-gray-300 block">اضغط لاختيار الصور أو اسحبها هنا</span>
                    <span class="text-xs text-gray-500 mt-1 block">تدعم كافة الصيغ الشهيرة بجودة عالية</span>
                    <input type="file" name="image" id="fileInput" class="hidden" accept="image/*" onchange="showFileName(this)">
                </label>
                <button type="submit" class="royal-btn w-full py-3 rounded-xl text-base shadow-lg cursor-pointer">بدء التحويل الآن ⚡</button>
            </form>
        </div>
    </main>
    <footer class="border-t border-red-900/30 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
    
    <script>
        function showFileName(input) {
            if (input.files && input.files[0]) {
                document.getElementById('fileName').innerText = "الملف المختار: " + input.files[0].name;
            }
        }
    </script>
</body>
</html>
''')

# 3. تحديث صفحة المشغل player.html
with open('templates/player.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>معالجة الفيديو والمشغل السينمائي - استوديو كيان</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #090d16; color: #f3f4f6; }
        .royal-btn { background: linear-gradient(135deg, #991b1b 0%, #b45309 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; }
        .royal-btn:hover { background: linear-gradient(135deg, #7f1d1d 0%, #92400e 100%); box-shadow: 0 0 20px rgba(180, 83, 9, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-red-900/40 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-red-600">KAYAN STUDIO | المشغل السينمائي</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-4xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="md:col-span-2 card-custom rounded-2xl p-6 border-red-900/30 shadow-2xl">
                <div class="flex items-center space-x-3 space-x-reverse mb-6">
                    <div class="w-12 h-12 rounded-xl bg-red-900/20 text-red-500 flex items-center justify-center text-xl">🎬</div>
                    <div>
                        <h1 class="text-xl font-bold">معالج الفيديو وتحويله إلى SVGA</h1>
                        <p class="text-gray-400 text-xs">التحكم في الإطارات، الجودة، والتأثيرات لغرف الدردشة</p>
                    </div>
                </div>
                <div class="space-y-4 mb-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-300 mb-2">رفع ملف الفيديو (MP4 / GIF):</label>
                        <div class="border-2 border-dashed border-red-900/50 hover:border-amber-500/50 rounded-xl p-6 text-center cursor-pointer bg-[#0e1626]">
                            <span class="text-2xl mb-1 block">📁</span>
                            <p class="text-xs text-gray-300">اختر ملف الفيديو لبدء التحويل</p>
                        </div>
                    </div>
                </div>
                <button class="royal-btn w-full py-3 rounded-xl text-sm shadow-lg">بدء التحويل والمعالجة ⚡</button>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col items-center justify-center text-center border-gray-800">
                <div class="w-16 h-16 rounded-2xl bg-amber-500/10 text-amber-400 flex items-center justify-center mb-3 text-2xl">▶️</div>
                <h3 class="text-sm font-bold mb-1">معاينة المشغل</h3>
                <p class="text-xs text-gray-500">في انتظار ملف SVGA للتشغيل السينمائي</p>
            </div>
        </div>
    </main>
    <footer class="border-t border-red-900/30 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
</body>
</html>
''')

# 4. تحديث صفحة المستخرج extractor.html
with open('templates/extractor.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مستخرج ملفات SVGA - استوديو كيان</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #090d16; color: #f3f4f6; }
        .royal-btn { background: linear-gradient(135deg, #991b1b 0%, #b45309 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; }
        .royal-btn:hover { background: linear-gradient(135deg, #7f1d1d 0%, #92400e 100%); box-shadow: 0 0 20px rgba(180, 83, 9, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-red-900/40 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-red-600">KAYAN STUDIO | المستخرج</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-4xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="card-custom rounded-2xl p-6 border-red-900/30 shadow-2xl">
                <div class="w-12 h-12 rounded-xl bg-red-900/20 text-red-500 flex items-center justify-center mb-4 text-xl">📦</div>
                <h1 class="text-xl font-bold mb-2">مستخرج أصول SVGA</h1>
                <p class="text-gray-400 text-sm mb-6">استخراج الصور، الرسوم، والأصوات من ملفات الـ SVGA وتنزيلها بجودة عالية.</p>
                <div class="border-2 border-dashed border-red-900/50 hover:border-amber-500/50 rounded-xl p-6 text-center cursor-pointer bg-[#0e1626] mb-6">
                    <span class="text-2xl mb-1 block">📁</span>
                    <p class="text-xs text-gray-300">ارفع ملف SVGA للاستخراج</p>
                </div>
                <button class="royal-btn w-full py-3 rounded-xl text-sm shadow-lg">استخراج الملفات الآن ⚡</button>
            </div>
            
            <div class="card-custom rounded-2xl p-6 flex flex-col items-center justify-center text-center border-gray-800">
                <div class="w-16 h-16 rounded-2xl bg-amber-500/10 text-amber-400 flex items-center justify-center mb-3 text-2xl">📊</div>
                <h3 class="text-sm font-bold mb-1">معاينة الإطارات المستخرجة</h3>
                <p class="text-xs text-gray-500">ستظهر العناصر والأصول هنا بعد اتمام عملية الاستخراج</p>
            </div>
        </div>
    </main>
    <footer class="border-t border-red-900/30 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
</body>
</html>
''')

print("Royal Gold & Dark Red theme applied successfully!")
