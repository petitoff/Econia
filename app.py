import json
from brain import run_chat

# with open('memory/typespecific_responses.json', encoding="utf-8") as json_file:
#     data = json.load(json_file)
#     print(data["questions"]["casual1"])


def test_get_msg_user():
    while True:
        user_msg = input("You: ")
        bot_msg = run_chat.get_msg(user_msg)
        print(f"Marcin: {bot_msg}")


test_get_msg_user()
