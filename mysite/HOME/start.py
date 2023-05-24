from flask import Flask, send_from_directory
#import sys

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory('HTML', "index.html")

@app.route("/<path:name>")
def start(name):
    return send_from_directory('HTML', name)

#if __name__ == "__main__":
#    application.run(host='0.0.0.0')
