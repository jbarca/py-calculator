from flask import Flask, render_template, request

app = Flask(__name__)


# TODO: Create and AJAX post request in the HTML file and use that to send
# a post message to the calculate function with the value of the display

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/handle_number", methods=['POST'])
def handle_number():
    request_dict = request.form.to_dict()
    for key, value in request_dict.items():
        print(value)
    return (''), 204


@app.route("/add", methods=['POST'])
def add():
    return (''), 204


@app.route("/subtract", methods=['POST'])
def subtract():
    return (''), 204


@app.route("/mutliply", methods=['POST'])
def multiply():
    return (''), 204


@app.route("/divide", methods=['POST'])
def divide():
    return (''), 204


@app.route("/calculate", methods=['POST'])
def calculate():
    print("calculating")


if __name__ == "__main__":
    app.run(debug=True)