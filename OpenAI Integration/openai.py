from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    # Your GPT-3 prompt and settings
    prompt_text = f"You asked: {user_input}\nAI Response:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=100  # Adjust max_tokens as needed
    )

    ai_response = response.choices[0].text.strip()
    return render_template('index.html', user_input=user_input, ai_response=ai_response)

if __name__ == '__main__':
    app.run(debug=True)
