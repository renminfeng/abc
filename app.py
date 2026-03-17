from flask import Flask, render_template, request

from calculator_core import evaluate_expression

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    result = None
    error = None

    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            result = evaluate_expression(expression)
        except Exception as exc:
            error = str(exc)

    return render_template("calculator.html", expression=expression, result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
