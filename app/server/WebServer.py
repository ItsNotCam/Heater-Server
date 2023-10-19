# FLASK APP
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('static/index.html')

if __name__ == '__main__':
    IP = ""
    with open("config.json",'r') as file:
        data = json.loads(file.read())
        IP = data["IP"]

    app.run(host=IP, port=80)