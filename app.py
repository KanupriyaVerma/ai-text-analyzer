from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def analyze_text(text):
    text = text.lower()

    summary = text[:50] + "..." if len(text) > 50 else text

    negative_words = ["scared", "confused", "sad", "crying", "depressed", "stressed"]
    positive_words = ["happy", "excited", "motivated", "confident"]

    if any(word in text for word in negative_words):
        sentiment = "Negative"
    elif any(word in text for word in positive_words):
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    # 🔥 Dynamic suggestions
    if sentiment == "Negative":
        suggestions = "Take a short break, talk to someone you trust, and focus on small positive steps."
    elif sentiment == "Positive":
        suggestions = "Keep up the great momentum! Stay consistent and build on this positivity."
    else:
        suggestions = "Try reflecting more on your thoughts and set small, clear goals."

    word_count = len(text.split())

    return {
        "summary": summary,
        "sentiment": sentiment,
        "suggestions": suggestions,
        "word_count": word_count
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "") if data else ""

    result = analyze_text(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)