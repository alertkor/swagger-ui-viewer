import requests
from flask import Flask
from flask import render_template, request
from urllib.parse import urlparse, parse_qs


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    return requests.get(request.args.get('url'), verify=False).content


app.run(port=5001, use_reloader=True)
