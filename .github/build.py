import json
import random

def get_productive_words():
    with open("work.json", "r") as work_file:
        data = json.load(work_file)
        return data["work"][random.randint(0, len(data["work"]) - 1)]

if __name__ == '__main__':
    try:
        with open("productive.txt", "r") as file:
            current_word = file.read().strip()
    except FileNotFoundError:
        current_word = ""

    word = get_productive_words()
    while word == current_word:
        word = get_productive_words()

    with open("productive.txt", "w") as file:
        file.write(word)