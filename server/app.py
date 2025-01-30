from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    user_input = request.form.get("user_input")
    check_word()
    return jsonify({"message": f"you entered: {user_input}"})


# Check is input word is the correct word
def check_word():
    print("test")


if __name__ == "__main__":
    app.run(debug=True)
