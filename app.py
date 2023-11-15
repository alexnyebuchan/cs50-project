from os import environ
import sqlite3

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session

from werkzeug.security import check_password_hash, generate_password_hash

from openai import OpenAI

from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    user_id = session["user_id"]

    if request.method == "GET":
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        row = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        larder = row[3]
        
        return render_template('index.html', larder=larder)
    
    elif request.method == 'POST':
        ingredients = request.form.get("ingredients")

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        row = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

        if not row:
            print('Please enter a larder')
            return redirect('/larder')
        
        larder = row[3]
            
        cursor.close()
        connection.close()

        req = "Here is what's in my kitchen: " + ingredients + ". Here is my larder of staples like spices, tinned goods etc." + larder + ". What recipes can I make? Please provide only 3, with a brief description of how to make each dish."

        client = OpenAI(api_key=environ.get('API_KEY'))

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": req}
        ]
        
        )
        responses = completion.choices[0].message.content.split('\n')
        
        return render_template("index.html", responses=responses, larder=larder)
 
@app.route('/larder', methods=['GET', 'POST'])
@login_required
def larder():
    user_id = session["user_id"]

    if request.method == 'GET':
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        row = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        larder = row[3]
        return render_template('larder.html', larder=larder)
    
    elif request.method == 'POST':
        larderInput = request.form.get("larder")

        if not larderInput:
            print('Please enter a larder')
            return redirect('/')
        
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        


        cursor.execute("UPDATE users SET larder = ? WHERE id = ?",
            (larderInput, user_id)
            )
        connection.commit()
        
        cursor.close()
        connection.close()

        return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            print('no username provided')
            return redirect('/')
        elif not password:
            print('no password provided')
            return redirect('/')

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        row = cursor.execute("SELECT * FROM users WHERE name = ?", (username,)).fetchone()

        if not row:
            print('user does not exist')
            return redirect('/')

        if row[1] != username or not check_password_hash(row[2], (password)):
            print('Invalid username or password')
            return redirect('/')
        
        session["user_id"] = row[0]
            
        cursor.close()
        connection.close()

        print('Successfully logged in')

        return redirect ('/')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    session.clear()

    if request.method == "GET":
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        if not username:
            print('no username provided')
            return redirect('/')
        elif not password:
            print('no password provided')
            return redirect('/')
        elif not confirmation:
            print('no confirmation provided')
            return redirect('/')
        
        if password != confirmation:
            print('password mismatch')
            return redirect('/')

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        pre_existing = cursor.execute("SELECT name FROM users WHERE name = ?", (username,)).fetchone()

        if pre_existing:
            print('user already exists')
            return redirect('/')
        hash = generate_password_hash(password)

        cursor.execute("INSERT INTO users (name, hash, larder) VALUES (?, ?, ?)",
            (username, hash, 'salt and pepper')
            )
        connection.commit()

        cursor.close()
        connection.close()

        return redirect('/')
    
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
