from flask import Flask, render_template, request, jsonify, session
from words import get_random_word

app = Flask(__name__)
app.secret_key = "super_secret_key"


@app.route("/")
def home():
    if "the_word" not in session or session.get("correct"):
        session["the_word"] = get_random_word()
        session["right_letters"] = []
        session["wrong_letters"] = []
        session["correct"] = False

    word_len = len(session["the_word"])
    return render_template("index.html", length=word_len)


@app.route("/process", methods=["POST"])
def process():
    user_input = request.form.get("user_input")
    answer = check_word(user_input)
    return jsonify(
        {"right": list(answer[0]), "wrong": list(answer[1]), "correct": answer[2]}
    )


def check_word(user_input):
    the_word = session["the_word"]
    right_letters = set(session["right_letters"])
    wrong_letters = set(session["wrong_letters"])

    if user_input == the_word:
        session["correct"] = True
        return list(right_letters), list(wrong_letters), True

    for c in user_input:
        if c in the_word:
            right_letters.add(c)
        else:
            wrong_letters.add(c)

    session["right_letters"] = list(right_letters)
    session["wrong_letters"] = list(wrong_letters)
    return list(right_letters), list(wrong_letters), False


if __name__ == "__main__":
    app.run(debug=True)
