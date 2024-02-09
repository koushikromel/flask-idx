import os
import random

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('web/index.html')

@app.route("/test")
def testing():
    name_list = ["Koushik", "Romel", "Ronaldo"]
    return random.choice(name_list)

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 80)))
