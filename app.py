from os import environ

from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

from openai import OpenAI

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == 'POST':
        ingredients = request.form.get("ingredients")

        req = "Here is what's in my kitchen: " + ingredients + ". What recipes can I make? Please provide only 3, with a brief description of the dish."

        client = OpenAI(api_key=environ.get('API_KEY'))

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": req}
        ]
        
        )
        responses = completion.choices[0].message.content.split('\n')

        
        print(responses)
        
        
        return render_template("index.html", responses=responses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()

    if request.method == "GET":
        return render_template('login.html')
    elif request.method == 'POST':
        return
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()

    if request.method == "GET":
        return render_template('register.html')
    elif request.method == 'POST':
        return
    
if __name__ == "__main__":
    app.run(debug=True)
