import json


def search_in_json1(word):
    with open('memory/word_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)

        if word[-1]["kind"] == "question":
            data_question = data["questions"]

            for a, b in data_question.items():
                print(a)
                print(b)
