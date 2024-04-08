#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

# Ensures strict_slashes are set to False for all routes globally.
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
