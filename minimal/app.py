#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello Codefellows!'

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
