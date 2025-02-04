import random

WORD_LIST = (
    "dog",
    "elephant",
    "mango",
    "coconut",
    "book",
    "cat",
    "sea",
    "turtle",
    "cowboy",
    "music",
)


def get_random_word():
    return random.choice(WORD_LIST)
