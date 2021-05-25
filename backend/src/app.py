from flask import Flask


app = Flask(__name__)

@app.route("/")
def Home():
    return "Hello"


app.run(port = 8080, debug = True)
