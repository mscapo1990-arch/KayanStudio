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
        .gold-btn { background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%); color: #111827; font-weight: 700; transition: all 0.3s ease; text-align: center; display: block; }
        .gold-btn:hover { background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%); box-shadow: 0 0 20px rgba(251, 191, 36, 0.4); }
        .indigo-link-btn { background: rgba(99, 102, 241, 0.2); color: #c7d2fe; transition: all 0.3s ease; text-align: center; display: block; border: 1px solid rgba(99, 102, 241, 0.3); }
        .indigo-link-btn:hover { background: rgb(99, 102, 241); color: #ffffff; }
        .purple-link-btn { background: rgba(124, 58, 237, 0.2); color: #ddd6fe; transition: all 0.3s ease; text-align: center; display: block; border: 1px solid rgba(124, 58, 237, 0.3); }
        .purple-link-btn:hover { background: rgb(124, 58, 237); color: #ffffff; }
        .card-custom { background: #111827; border: 1px solid #1f2937; transition: all 0.3s ease; }
        .card-custom:hover { border-color: #7c3aed; box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.15); }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-gray-800 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-500">KAYAN STUDIO</span>
            <nav class="hidden md:flex space-x-6 space-x-reverse text-sm text-gray-300">
                <a href="#" class="hover:text-purple-400 transition">الرئيسية</a>
                <a href="/player" class="hover:text-purple-400 transition">المشغل</a>
                <a href="/extractor" class="hover:text-purple-400 transition">المستخرج</a>
                <a href="/converter" class="text-amber-400 font-bold">المحول</a>
            </nav>
            <button class="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-xl text-sm font-semibold transition">دخول</button>
        </div>
    </header>
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <div class="text-center mb-16">
            <h1 class="text-3xl sm:text-5xl font-extrabold mb-4 tracking-tight">احترافية كاملة في معالجة ملفات <span class="text-purple-400">SVGA</span></h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-sm sm:text-base">المنصة الأولى والأجدر لاستخراج، تحويل، ومعاينة ملفات الـ SVGA بدقة سينمائية مذهلة.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-purple-600/20 text-purple-400 flex items-center justify-center mb-4 text-xl">🖼️</div>
                    <h3 class="text-lg font-bold mb-2">تحويل الصور إلى SVGA</h3>
                    <p class="text-gray-400 text-sm mb-6">اختر صورة أو عدة صور مع تفريغ الخلفية تلقائياً وتحويلها بدقة عالية.</p>
                </div>
                <button class="w-full bg-purple-600/20 hover:bg-purple-600 text-purple-300 hover:text-white py-2.5 rounded-xl text-sm font-semibold transition border border-purple-500/30">فتح الأداة ←</button>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-amber-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4 text-xl">⚡</div>
                    <h3 class="text-lg font-bold mb-2">محول صيغ الصور المتعددة</h3>
                    <p class="text-gray-400 text-sm mb-6">تحويل كافة صيغ الصور (PNG, JPG, WEBP, GIF) إلى SVGA بضغطة واحدة.</p>
                </div>
                <a href="/converter" class="gold-btn w-full py-2.5 rounded-xl text-sm shadow-lg">تحويل الآن ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-indigo-600/20 text-indigo-400 flex items-center justify-center mb-4 text-xl">🎬</div>
                    <h3 class="text-lg font-bold mb-2">المشغل السينمائي</h3>
                    <p class="text-gray-400 text-sm mb-6">معاينة ملفات SVGA، التحكم في الإطارات، وتحويل الفيديوهات لغرف الدردشة.</p>
                </div>
                <a href="/player" class="indigo-link-btn w-full py-2.5 rounded-xl text-sm font-semibold">فتح الأداة ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-purple-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-purple-600/20 text-purple-400 flex items-center justify-center mb-4 text-xl">📦</div>
                    <h3 class="text-lg font-bold mb-2">مستخرج ملفات SVGA</h3>
                    <p class="text-gray-400 text-sm mb-6">استخراج الصور، الأصول، والأصوات من ملفات الـ SVGA وتنزيلها بجودة عالية.</p>
                </div>
                <a href="/extractor" class="purple-link-btn w-full py-2.5 rounded-xl text-sm font-semibold">فتح الأداة ←</a>
            </div>
        </div>
    </main>
    <footer class="border-t border-gray-800 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو (Kayan Studio) 2026</footer>
</body>
</html>
''')

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
            <div class="border-2 border-dashed border-gray-700 hover:border-amber-500/50 rounded-2xl p-8 text-center cursor-pointer transition mb-6 bg-[#0e1626]">
                <span class="text-3xl mb-2 block">📁</span>
                <p class="text-sm font-semibold text-gray-300">اضغط لاختيار الصور أو اسحبها هنا</p>
                <p class="text-xs text-gray-500 mt-1">تدعم كافة الصيغ الشهيرة بجودة عالية</p>
            </div>
            <button class="gold-btn w-full py-3 rounded-xl text-base shadow-lg">بدء التحويل الآن ⚡</button>
        </div>
    </main>
    <footer class="border-t border-gray-800 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
</body>
</html>
''')

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
        .indigo-btn { background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; }
        .indigo-btn:hover { background: linear-gradient(135deg, #4f46e5 100%, #3730a3 100%); box-shadow: 0 0 20px rgba(99, 102, 241, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-gray-800 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-500">KAYAN STUDIO | المشغل السينمائي</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-4xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="md:col-span-2 card-custom rounded-2xl p-6 border-indigo-500/30 shadow-2xl">
                <div class="flex items-center space-x-3 space-x-reverse mb-6">
                    <div class="w-12 h-12 rounded-xl bg-indigo-600/20 text-indigo-400 flex items-center justify-center text-xl">🎬</div>
                    <div>
                        <h1 class="text-xl font-bold">معالج الفيديو وتحويله إلى SVGA</h1>
                        <p class="text-gray-400 text-xs">التحكم في الإطارات، الجودة، والتأثيرات لغرف الدردشة</p>
                    </div>
                </div>
                <div class="space-y-4 mb-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-300 mb-2">رفع ملف الفيديو (MP4 / GIF):</label>
                        <div class="border-2 border-dashed border-gray-700 hover:border-indigo-500/50 rounded-xl p-6 text-center cursor-pointer bg-[#0e1626]">
                            <span class="text-2xl mb-1 block">📁</span>
                            <p class="text-xs text-gray-300">اختر ملف الفيديو لبدء التحويل</p>
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs text-gray-400 mb-1">عدد الإطارات (FPS): 16</label>
                        <input type="range" min="10" max="60" value="16" class="w-full accent-indigo-500">
                    </div>
                    <div>
                        <label class="block text-xs text-gray-400 mb-1">جودة الضغط: 80%</label>
                        <input type="range" min="10" max="100" value="80" class="w-full accent-indigo-500">
                    </div>
                </div>
                <button class="indigo-btn w-full py-3 rounded-xl text-sm shadow-lg">بدء التحويل والمعالجة ⚡</button>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col items-center justify-center text-center border-gray-800">
                <div class="w-16 h-16 rounded-2xl bg-indigo-600/10 text-indigo-400 flex items-center justify-center mb-3 text-2xl">▶️</div>
                <h3 class="text-sm font-bold mb-1">معاينة المشغل</h3>
                <p class="text-xs text-gray-500">في انتظار ملف SVGA للتشغيل السينمائي</p>
            </div>
        </div>
    </main>
    <footer class="border-t border-gray-800 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
</body>
</html>
''')

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
        .purple-btn { background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; }
        .purple-btn:hover { background: linear-gradient(135deg, #6d28d9 100%, #4338ca 100%); box-shadow: 0 0 20px rgba(124, 58, 237, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-gray-800 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-500">KAYAN STUDIO | المستخرج</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-4xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="card-custom rounded-2xl p-6 border-purple-500/30 shadow-2xl">
                <div class="w-12 h-12 rounded-xl bg-purple-600/20 text-purple-400 flex items-center justify-center mb-4 text-xl">📦</div>
                <h1 class="text-xl font-bold mb-2">مستخرج أصول SVGA</h1>
                <p class="text-gray-400 text-sm mb-6">استخراج الصور، الرسوم، والأصوات من ملفات الـ SVGA وتنزيلها بجودة عالية.</p>
                <div class="border-2 border-dashed border-gray-700 hover:border-purple-500/50 rounded-xl p-6 text-center cursor-pointer bg-[#0e1626] mb-6">
                    <span class="text-2xl mb-1 block">📁</span>
                    <p class="text-xs text-gray-300">ارفع ملف SVGA للاستخراج</p>
                </div>
                <button class="purple-btn w-full py-3 rounded-xl text-sm shadow-lg">استخراج الملفات الآن ⚡</button>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col items-center justify-center text-center border-gray-800">
                <div class="w-16 h-16 rounded-2xl bg-purple-600/10 text-purple-400 flex items-center justify-center mb-3 text-2xl">📊</div>
                <h3 class="text-sm font-bold mb-1">معاينة الإطارات المستخرجة</h3>
                <p class="text-xs text-gray-500">ستظهر العناصر والأصول هنا بعد اتمام عملية الاستخراج</p>
            </div>
        </div>
    </main>
    <footer class="border-t border-gray-800 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
</body>
</html>
''')

print("All HTML files created successfully!")
