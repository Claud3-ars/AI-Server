from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

# Load AI Model
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = chatbot(user_input, max_length=100)[0]["generated_text"]
    return {"reply": response}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
