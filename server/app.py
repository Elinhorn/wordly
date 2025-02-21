from flask import Flask, render_template, request, jsonify, session
from words import get_random_word
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")


@app.route("/")
def home():
    if (
        "the_word" not in session
        or session.get("correct")
        or session.get("attempts") == 0
    ):
        session["the_word"] = get_random_word()
        session["right_letters"] = []
        session["wrong_letters"] = []
        session["correct"] = False
        session["attempts"] = 5

    word_len = len(session["the_word"])
    attempts_left = session.get("attempts", 5)
    return render_template("index.html", length=word_len, attempts=attempts_left)


@app.route("/process", methods=["POST"])
def process():

    attempts_left = session.get("attempts", 5)

    attempts_left -= 1

    session["attempts"] = attempts_left

    if attempts_left == 0:
        return jsonify({"game_over": True, "attempts": attempts_left})

    user_input = request.form.get("user_input")
    answer = check_word(user_input)

    if answer[2]:
        return jsonify(
            {
                "right": list(answer[0]),
                "wrong": list(answer[1]),
                "correct": answer[2],
                "attempts": attempts_left,
            }
        )

    return jsonify(
        {
            "right": list(answer[0]),
            "wrong": list(answer[1]),
            "correct": answer[2],
            "attempts": attempts_left,
        }
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
