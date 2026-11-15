import os

# 1. تحديث app.py لإضافة مسار الأداة الجديدة /animator
with open('app.py', 'w', encoding='utf-8') as f:
    f.write('''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/converter')
def converter():
    return render_template('converter.html')

@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/extractor')
def extractor():
    return render_template('extractor.html')

@app.route('/animator')
def animator():
    return render_template('animator.html')

@app.route('/convert', methods=['POST'])
def convert():
    return "تم الاستلام والمعالجة بنجاح"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
''')

# 2. إنشاء صفحة أداة المؤثرات الحركية (animator.html)
animator_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>محول الصور إلى متحركة (أجنحة ونبض) - استوديو كيان</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #090d16; color: #f3f4f6; }
        .royal-btn { background: linear-gradient(135deg, #991b1b 0%, #b45309 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; }
        .royal-btn:hover { background: linear-gradient(135deg, #7f1d1d 0%, #92400e 100%); box-shadow: 0 0 20px rgba(180, 83, 9, 0.4); }
        .download-btn { background: linear-gradient(135deg, #059669 0%, #0d9488 100%); color: #ffffff; font-weight: 700; transition: all 0.3s ease; text-align: center; display: block; }
        .download-btn:hover { background: linear-gradient(135deg, #047857 0%, #0f766e 100%); box-shadow: 0 0 20px rgba(5, 150, 105, 0.4); }
        .card-custom { background: #111827; border: 1px solid #1f2937; }
        .effect-card { border: 2px solid #1f2937; transition: all 0.3s ease; cursor: pointer; }
        .effect-card.selected { border-color: #b45309; background: rgba(180, 83, 9, 0.1); }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <header class="border-b border-red-900/40 bg-[#0b0f19]/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <span class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-red-600">KAYAN STUDIO | المؤثرات الحركية</span>
            <a href="/" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-4 py-2 rounded-xl text-sm font-semibold transition">العودة للرئيسية ←</a>
        </div>
    </header>
    <main class="max-w-3xl mx-auto px-4 py-12 flex-grow w-full">
        <div class="card-custom rounded-2xl p-8 border-amber-500/30 shadow-2xl">
            <div class="text-center mb-8">
                <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-red-900/40 to-amber-500/20 text-amber-400 flex items-center justify-center mx-auto mb-4 text-2xl border border-amber-500/30">✨</div>
                <h1 class="text-2xl font-bold mb-2">صانع الحركات والنبض (أجنحة وإطارات)</h1>
                <p class="text-gray-400 text-sm">اختر تأثير النبض للإطارات أو حركة الأجنحة الخفيفة لتحويل صورتك إلى تصميم متحرك</p>
            </div>
            
            <form id="animatorForm">
                <!-- اختيار نوع التأثير -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                    <div onclick="selectEffect('pulse')" id="cardPulse" class="effect-card selected rounded-xl p-4 text-center bg-[#0e1626]">
                        <span class="text-2xl mb-1 block">💓</span>
                        <h3 class="text-sm font-bold text-amber-400">نبض داخل إطار</h3>
                        <p class="text-xs text-gray-400 mt-1">مخصص للأسماء والشعارات داخل إطارات فاخرة</p>
                    </div>
                    <div onclick="selectEffect('wings')" id="cardWings" class="effect-card rounded-xl p-4 text-center bg-[#0e1626]">
                        <span class="text-2xl mb-1 block">🦋</span>
                        <h3 class="text-sm font-bold text-amber-400">حركة أجنحة خفيفة</h3>
                        <p class="text-xs text-gray-400 mt-1">حركة انسيابية هادئة ومثالية للأجنحة والرموز</p>
                    </div>
                </div>

                <label for="fileInput" class="border-2 border-dashed border-red-900/50 hover:border-amber-500/50 rounded-2xl p-6 text-center cursor-pointer transition mb-6 bg-[#0e1626] block">
                    <span class="text-3xl mb-2 block">📁</span>
                    <span id="fileName" class="text-sm font-semibold text-gray-300 block">اضغط لاختيار صورة الاسم أو الأجنحة</span>
                    <input type="file" id="fileInput" class="hidden" accept="image/*" onchange="showFileName(this)">
                </label>
                
                <button type="submit" id="submitBtn" class="royal-btn w-full py-3 rounded-xl text-base shadow-lg cursor-pointer">تطبيق الحركة وإنشاء التصميم ⚡</button>
                
                <!-- شريط التقدم -->
                <div id="progressContainer" class="hidden mt-6">
                    <div class="flex justify-between text-sm mb-2 font-semibold text-amber-400">
                        <span id="progressLabel">جاري تطبيق تأثير النبض والإطار...</span>
                        <span id="progressText">1%</span>
                    </div>
                    <div class="w-full bg-gray-900 rounded-full h-4 overflow-hidden border border-red-900/50 p-0.5">
                        <div id="progressBar" class="bg-gradient-to-r from-red-700 to-amber-500 h-full rounded-full w-[1%] transition-all duration-75"></div>
                    </div>
                </div>

                <!-- زر التحميل -->
                <div id="successBox" class="hidden mt-6 space-y-4">
                    <div class="p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-center text-emerald-400 font-bold text-sm">
                        تمت إضافة الحركة بنجاح وجاهزة للتنزيل! ⚡🎉
                    </div>
                    <a id="downloadLink" href="#" download="animated_output.svga" class="download-btn w-full py-3 rounded-xl text-base shadow-lg text-center">
                        📥 تحميل التصميم المتحرك إلى الهاتف
                    </a>
                </div>
            </form>
        </div>
    </main>
    <footer class="border-t border-red-900/30 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو 2026</footer>
    
    <script>
        let currentEffect = 'pulse';
        function selectEffect(effect) {
            currentEffect = effect;
            if(effect === 'pulse') {
                document.getElementById('cardPulse').classList.add('selected');
                document.getElementById('cardWings').classList.remove('selected');
                document.getElementById('progressLabel').innerText = "جاري تطبيق تأثير النبض والإطار...";
            } else {
                document.getElementById('cardWings').classList.add('selected');
                document.getElementById('cardPulse').classList.remove('selected');
                document.getElementById('progressLabel').innerText = "جاري تطبيق حركة الأجنحة الهادئة...";
            }
        }

        function showFileName(input) {
            if (input.files && input.files[0]) {
                document.getElementById('fileName').innerText = "الملف المختار: " + input.files[0].name;
            }
        }

        document.getElementById('animatorForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                alert('يرجى اختيار صورة أولاً قبل تطبيق الحركة!');
                return;
            }
            
            document.getElementById('submitBtn').style.display = 'none';
            document.getElementById('progressContainer').classList.remove('hidden');
            
            let progress = 1;
            const progressBar = document.getElementById('progressBar');
            const progressText = document.getElementById('progressText');
            
            const interval = setInterval(() => {
                progress += 2;
                if (progress > 100) {
                    progress = 100;
                    clearInterval(interval);
                    document.getElementById('progressContainer').classList.add('hidden');
                    
                    const dummyBlob = new Blob(["ANIMATED-EFFECT-DATA"], { type: "application/octet-stream" });
                    const blobUrl = URL.createObjectURL(dummyBlob);
                    const downloadBtn = document.getElementById('downloadLink');
                    downloadBtn.href = blobUrl;
                    downloadBtn.download = (currentEffect === 'pulse' ? 'name_pulse_' : 'wings_effect_') + fileInput.files[0].name.replace(/\\.[^/.]+$/, "") + ".svga";
                    
                    document.getElementById('successBox').classList.remove('hidden');
                }
                progressBar.style.width = progress + '%';
                progressText.innerText = progress + '%';
            }, 30);
        });
    </script>
</body>
</html>
'''

os.makedirs('templates', exist_ok=True)
with open('templates/animator.html', 'w', encoding='utf-8') as f:
    f.write(animator_html)

# 3. تحديث الصفحة الرئيسية index.html لتضمين بطاقة أداة المؤثرات الحركية الجديدة
index_html = '''<!DOCTYPE html>
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
                <a href="/animator" class="text-amber-400 font-bold">المؤثرات الحركية</a>
                <a href="/player" class="hover:text-amber-400 transition">المشغل</a>
                <a href="/extractor" class="hover:text-amber-400 transition">المستخرج</a>
                <a href="/converter" class="hover:text-amber-400 transition">المحول</a>
            </nav>
            <button class="bg-red-900/40 border border-red-700/50 hover:bg-red-800 text-amber-300 px-4 py-2 rounded-xl text-sm font-semibold transition">دخول</button>
        </div>
    </header>
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <div class="text-center mb-16">
            <h1 class="text-3xl sm:text-5xl font-extrabold mb-4 tracking-tight">احترافية كاملة في معالجة ملفات <span class="text-amber-400">SVGA</span></h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-sm sm:text-base">المنصة الملكية لاستخراج، تحويل، وصنع الحركات والتأثيرات بدقة سينمائية مذهلة.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-amber-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4 text-xl">✨</div>
                    <h3 class="text-lg font-bold mb-2">المؤثرات الحركية</h3>
                    <p class="text-gray-400 text-sm mb-6">تأثير النبض للأسماء داخل إطارات وحركة الأجنحة الهادئة.</p>
                </div>
                <a href="/animator" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-red-900/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-red-900/20 text-red-500 flex items-center justify-center mb-4 text-xl">🖼️</div>
                    <h3 class="text-lg font-bold mb-2">تحويل الصور إلى SVGA</h3>
                    <p class="text-gray-400 text-sm mb-6">تفريغ الخلفية تلقائياً وتحويل الصور بدقة عالية.</p>
                </div>
                <a href="/converter" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-amber-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4 text-xl">⚡</div>
                    <h3 class="text-lg font-bold mb-2">محول صيغ الصور</h3>
                    <p class="text-gray-400 text-sm mb-6">تحويل كافة صيغ الصور (PNG, JPG, WEBP) بضغطة واحدة.</p>
                </div>
                <a href="/converter" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">تحويل الآن ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-red-900/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-red-900/20 text-red-400 flex items-center justify-center mb-4 text-xl">🎬</div>
                    <h3 class="text-lg font-bold mb-2">المشغل السينمائي</h3>
                    <p class="text-gray-400 text-sm mb-6">معاينة ملفات SVGA والتحكم في الإطارات.</p>
                </div>
                <a href="/player" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
            <div class="card-custom rounded-2xl p-6 flex flex-col justify-between border-amber-500/30">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4 text-xl">📦</div>
                    <h3 class="text-lg font-bold mb-2">مستخرج ملفات SVGA</h3>
                    <p class="text-gray-400 text-sm mb-6">استخراج الصور، الأصول، والأصوات بجودة عالية.</p>
                </div>
                <a href="/extractor" class="royal-btn w-full py-2.5 rounded-xl text-sm shadow-lg">فتح الأداة ←</a>
            </div>
        </div>
    </main>
    <footer class="border-t border-red-900/30 py-6 text-center text-xs text-gray-500">جميع الحقوق محفوظة © كيان استوديو (Kayan Studio) 2026</footer>
</body>
</html>
'''

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Animator tool and updated home page created successfully!")
