import json
from random import randint


# Import json file
def import_json1():
    with open('memory/word_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def import_json2():
    with open('memory/respons_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def import_json3():
    with open('memory/bot_action.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def search_in_list(list_pattern, word):
    # Function related to search_in_json1. Looks for the written meanings of words in word_base
    patterns = list_pattern["patterns"]
    mining = list_pattern["mining"]

    for i in patterns:
        if i == word:
            return mining

    return False


# Checking if the user asks for any action
def checking_if_it_requires_action(user_msg):
    lst_word_action = ["marcin", "hej marcin", "ej", "czuwasz", "jestes"]
    lst_word_responses = ["tak", "słucham"]

    for i in lst_word_action:
        if i == user_msg:
            response = lst_word_responses[randint(0, len(lst_word_responses)-1)]
            return response
    return False


# Searching in the word database
def search_in_json1(word):
    data = import_json1()

    for a, b in data.items():
        for c, d in b.items():
            for e, f in d.items():
                asd = search_in_list(f, word)
                if asd is not False:
                    return asd


def search_mining(list_mining):
    # Searching for the meaning of the word (sentences) that have been recognized
    data = import_json2()

    for i in range(0, len(list_mining)):
        data = data[list_mining[i]]

    return data[randint(0, len(data) - 1)]
