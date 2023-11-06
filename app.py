from flask import Flask, render_template, request

app = Flask(__name)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    # Your GPT-3 interaction and response generation code goes here

    # For now, let's assume a simple response
    response = "Here's a humorous response to: " + user_input
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
