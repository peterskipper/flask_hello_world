
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def in_the_beginning():
    return "This is the root. Visit '<heroku app name>/hello' to get started"

@app.route("/hello")
def hello_world():
	return "Hello World"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a random picture from the internet.  Flask and Heroku appear to work.
        </p>
        <img src="https://allcutegirls.files.wordpress.com/2009/10/sririta-jensen-24-cute-girls.jpg"/>
        """.format(name)
    return html

if __name__ == "__main__":
	app.run()
