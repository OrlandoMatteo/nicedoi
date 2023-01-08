from flask import Flask, request, render_template
import json
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    headers = {"Accept": "application/citeproc+json"}
    r = requests.get(data["url"], headers=headers)
    output = r.json()
    return json.dumps(output)
