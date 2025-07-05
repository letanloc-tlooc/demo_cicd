from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask CI/CD with Render!"

@app.route("/hi")
def hihi():
    return "hi cái nữa nè"

@app.route("/xinchao")
def hii():
    return "hi hoài luôn"

@app.route("/xin")
def te():
    return "yêu bé Ngọc"