import datetime
import os
 
from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/api")
def index():
    return Response("hello", mimetype="application/json", status=200)

if __name__ == "__main__":
    app.run(debug=True, port=5000)