import google.generativeai as genai
from flask import Flask, request, render_template, redirect, url_for

def generate_text_with_gemini_flash(api_key, prompt):

    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel('gemini-2.0-flash-lite-preview-02-05') 

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('jokegen.html')

@app.route('/makejoke', methods=['POST'])
def upload_file():

    api_key = ''
    input_text = request.form['input_text']
    prompt = f"Opowiedz krótki żart na temat {input_text}"
    generated_text = generate_text_with_gemini_flash(api_key, prompt)

    html_body = f'<body bgcolor="lightgray"><h3>{generated_text}</h3></body>'
    return html_body

if __name__ == '__main__':
    app.run(debug=True)
