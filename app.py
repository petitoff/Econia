import json
from brain import run_chat

with open('memory/typespecific_responses.json') as json_file:
    data = json.load(json_file)
    print(data)


def test_get_msg_user():
    while True:
        user_msg = input("You: ")
        bot_msg = run_chat.get_msg(user_msg)
        print(f"Marcin: {bot_msg}")


test_get_msg_user()
