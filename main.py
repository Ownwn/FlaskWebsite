from flask import Flask
import requests


app = Flask(__name__)


def fetch(url):
    return requests.get(url).json()


@app.route("/")
def index():
    return "index page"


@app.route("/bazaar")
def bazaar():

    bazaar_1 = fetch("https://api.hypixel.net/skyblock/bazaar")
    return bazaar_1


@app.route("/hello")
def hello_world():
    content = f'''<p>Hello, World!</p>
    {str(5 * 6)}'''

    return content


app.run(host='0.0.0.0', debug=True)
