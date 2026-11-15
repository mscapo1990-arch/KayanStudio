import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home(): return render_template('index.html')
@app.route('/converter')
def converter(): return render_template('converter.html')
@app.route('/bg_remover')
def bg_remover(): return render_template('bg_remover.html')
@app.route('/svga_player')
def svga_player(): return render_template('svga_player.html')
@app.route('/ai_generator')
def ai_generator(): return render_template('ai_generator.html')
@app.route('/animator')
def animator(): return render_template('animator.html')
@app.route('/extractor')
def extractor(): return render_template('extractor.html')

@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'Empty prompt'}), 400
    return jsonify({'status': 'success', 'message': 'Processed successfully', 'prompt': prompt})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
