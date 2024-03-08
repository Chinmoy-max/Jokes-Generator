from flask import Flask
import pyjokes

app = Flask(__name__)

@app.route("/")
def home():
    joke = pyjokes.get_joke()
    return f'<h1 style="color:red; text-align:center; padding:20%; font-family:arial;">{joke}<h1>'

@app.route("/Multiple")
def multiple():
    jokes = pyjokes.get_jokes()
    return f'<h1 style="color:blue; text-align:center; padding:20%; font-family:arial;">{jokes}<h1>'


app.run(debug=True)