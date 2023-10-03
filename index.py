from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/hellow_world")
def hellow_world():
    return "<h1>Hello! World.</h1>"