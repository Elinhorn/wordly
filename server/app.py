from flask import Flask, render_template, request, jsonify
from words import get_random_word

app = Flask(__name__)

the_word = get_random_word()
right_letters = ""
wrong_letters = ""


@app.route("/")
def home():
    # när rätt ord är gissat ska ett nytt ord randomisas
    word_len = word_length()
    # gör en funktion som bestämmer antal försök, kanske beroende på hur långt ordet är
    return render_template("index.html", length=word_len)


@app.route("/process", methods=["POST"])
def process():
    user_input = request.form.get("user_input")
    # felhantering av user_input / bör göras på frontend också ?
    answer = check_word(user_input)
    # en funktion som räknar ner hur många försök det är kvar
    return jsonify({"right": answer[0], "wrong": answer[1], "correct": answer[2]})


def word_length():
    global the_word
    return len(the_word)


def check_word(user_input):
    global the_word
    global right_letters
    global wrong_letters

    if user_input == the_word:
        return right_letters, wrong_letters, True

    for c in user_input:
        if c in the_word:
            if c not in right_letters:
                right_letters += c
        else:
            if c not in wrong_letters:
                wrong_letters += c

    return right_letters, wrong_letters, False


if __name__ == "__main__":
    app.run(debug=True)
