from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# TODO: Determine calculation for POST data

@app.route("/")
def index():
    return render_template("index.html")


def add():
    return None


def subtract():
    return None


def multiply():
    return None


def divide():
    return None


@app.route("/calculate", methods=['POST'])
def calculate():
    if request.method == 'POST':
        print(request.get_json())
    return (''), 204


if __name__ == "__main__":
    app.run(debug=True)