from os import environ

from flask import Flask, render_template, request, redirect

from openai import OpenAI

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == 'POST':
        ingredients = request.form.get("ingredients")

        req = "Here is what's in my kitchen: " + ingredients + ". What dishes could I make? Please provide a short list."

        client = OpenAI(api_key=environ.get('API_KEY'))

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": req}
        ]
        )
        print(completion.choices[0].message)

        return redirect('/')



    

if __name__ == "__main__":
    app.run(debug=True)
