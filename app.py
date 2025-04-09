from flask import Flask, render_template, request, jsonify
from scripts.match import match_text_emoji

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/matchEmoji', methods=['POST'])
def match_emoji():
    try:
        data = request.get_json()
        text = data.get('text')
        response = match_text_emoji(text)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error':f'Internal server error: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)