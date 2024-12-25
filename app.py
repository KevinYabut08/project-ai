from flask import Flask, request, jsonify, render_template
import openai  # Replace with your AI library

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "your-openai-api-key"

@app.route('/')
def home():
    return render_template('index.html')  # HTML file for the frontend

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Example using OpenAI GPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )
    return jsonify({'response': response['choices'][0]['text'].strip()})

if __name__ == '__main__':
    app.run(debug=True)
