from flask import Flask, render_template, request

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

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get('image')
    if file:
        return f"تم استلام الصورة بنجاح: {file.filename} - جاري المعالجة والتحويل..."
    return "لم يتم اختيار أي ملف، يرجى المحاولة مجدداً."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
