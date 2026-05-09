from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

# Load data
with open('faq.json') as f:
    data = json.load(f)

questions = [item['question'] for item in data]
answers = [item['answer'] for item in data]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Clean input
def clean_text(text):
    return text.lower().strip()

# Get response
def get_response(user_input):
    user_input = clean_text(user_input)
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()

    if similarity[0][index] < 0.6:
        return "Sorry, I didn't understand. Try asking about eligibility, fees, or documents."

    return answers[index]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)