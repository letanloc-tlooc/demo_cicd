from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask CI/CD with Render!"

@app.route("/hi")
def hihi():
    return "hi cái nữa nè"

@app.route("/xinchao")
def hihi():
    return "hi hoài luôn"