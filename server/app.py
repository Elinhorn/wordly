from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

right_letters = ""
wrong_letters = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    user_input = request.form.get("user_input")
    # check if the word is correct if not run progam
    answer = check_word(user_input)
    return {"right": f"{answer[0]}", "wrong": f"{answer[1]}"}


# Check is input word is the correct word
def check_word(user_input):
    the_word = "hund"

    for c in user_input:
        if c in the_word:
            global right_letters
            if c not in right_letters:
                right_letters += c
        else:
            global wrong_letters
            if c not in wrong_letters:
                wrong_letters += c

    print(f"these are the right letters {right_letters}")
    return right_letters, wrong_letters

    # if user_input == the_word:
    #    print("right word!!")
    #    return "right word!!"
    # else:
    #    print("wrong word :( ")
    #    return "wrong word!! :("


if __name__ == "__main__":
    app.run(debug=True)
