from brain import run_chat


def test_get_msg_user():
    while True:
        user_msg = input("You: ")
        bot_msg = run_chat.get_msg(user_msg)
        print(f"Marcin: {bot_msg}")


test_get_msg_user()
