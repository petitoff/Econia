import json


def import_json():
    with open('memory/word_base.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def search_in_list(list_pattern, word):
    print(list_pattern)
    patterns = list_pattern["patterns"]
    mining = list_pattern["mining"]

    # print(patterns)
    # print(mining)

    for i in patterns:
        if i == word:
            return mining

    return False


data_json = import_json()


def search_json():
    for a, b in data_json.items():
        for c, d in b.items():
            for e, f in d.items():
                asd = search_in_list(f, "czesc")
                if asd is not False:
                    return asd


print(search_json())
