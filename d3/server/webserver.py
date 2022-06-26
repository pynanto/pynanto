from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Up & Running2!</p>"


app.run(host="0.0.0.0", port=5020, debug=False, use_reloader=True)
