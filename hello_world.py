from flask import Flask

app = Flask(__name__)

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
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/200/300">
    """
    return html.format(name.title())

if __name__ == "__main__":
	app.run()
