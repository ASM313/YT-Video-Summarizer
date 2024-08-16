from flask import Flask, request, render_template
from utility import *  # Replace with your actual module

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/summary', methods=['POST'])
def get_response():
    
    url = request.form['userInput']
    transcript = transcript_text(url)
    response = generate_gemini_content(transcript, prompt)
    print(response)
    return render_template('result.html', response=response)

if __name__ == '__main__':
    app.run()
