import json


# Basic Search
def search_in_json1(word, main):
    with open('memory/word_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)

        if main == "question":
            data = data["questions"]

        for a, b in data.items():
            for c, d in b.items():
                for e, f in d.items():
                    pattern = e
                    mining = f
