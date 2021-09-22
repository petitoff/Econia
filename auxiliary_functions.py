import json
from random import randint


# Basic Search
def import_json1():
    with open('memory/word_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def import_json2():
    with open('memory/respons_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def search_in_list(list_pattern, word):
    patterns = list_pattern["patterns"]
    mining = list_pattern["mining"]

    for i in patterns:
        if i == word:
            return mining

    return False


def search_in_json1(word):
    data = import_json1()

    for a, b in data.items():
        for c, d in b.items():
            for e, f in d.items():
                asd = search_in_list(f, word)
                if asd is not False:
                    return asd


def search_mining(list_mining):
    data = import_json2()

    list_response = data[list_mining[0]][list_mining[1]]
    return list_response[randint(0, len(list_response)-1)]
