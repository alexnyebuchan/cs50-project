
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == 'POST':
        ingredients = request.form.get("ingredients")
        print(ingredients)
        return redirect('/')



    

if __name__ == "__main__":
    app.run(debug=True)
