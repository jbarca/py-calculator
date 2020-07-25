from flask import Flask, render_template, request

app = Flask(__name__)

first_num = None
second_num = None


# TODO: Add 'operand' variable that denotes which operand will be used in the
# calculation. When first_num and second_num are both not None and '=' is clicked
# perform the calculation

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
    print("adding numbers")
    return (''), 204


@app.route("/subtract", methods=['POST'])
def subtract():
    print("subtracting numbers")
    return (''), 204


@app.route("/mutliply", methods=['POST'])
def multiply():
    print("multiplying numbers")
    return (''), 204


@app.route("/divide", methods=['POST'])
def divide():
    print("dividing numbers")
    return (''), 204


if __name__ == "__main__":
    app.run(debug=True)