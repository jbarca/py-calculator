from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# https://www.reddit.com/r/flask/comments/afgks4/how_to_get_a_javascript_function_to_call_a_flask/
# https://freshman.tech/css-grid-calculator/

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=['POST'])
def calculate():
    expr = ""
    if request.method == 'POST':
        try:
            expr = eval(request.get_json())
        except Exception:
            expr = "Invalid expression"
    return jsonify(expr)


if __name__ == "__main__":
    app.run(debug=True)