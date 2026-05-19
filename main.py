# Import
from flask import Flask, render_template,request, redirect
import os
from datetime import datetime

app = Flask(__name__)

# Uruchamianie strony z treścią
@app.route('/')
def index():
    return render_template('index.html')


# Umiejętności dynamiczne
@app.route('/', methods=['POST'])
def process_form():
    # umiejetnosci
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    # feedback

    email = request.form.get('email')
    text = request.form.get('text')

    if email and text:
    
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f'Time: {time}\n')
            f.write(f'Email: {email}\n')
            f.write(f'Text: {text}\n')
            f.write('===========================\n')

    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)
