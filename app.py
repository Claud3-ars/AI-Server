from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load AI Model
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    
    response = chatbot(user_input, max_length=100)
    reply = response[0]["generated_text"]
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
