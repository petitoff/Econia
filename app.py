from brain import Chat


def test_get_msg_user():
    run_chat = Chat()
    while True:
        user_msg = input("You: ")
        bot_msg = run_chat.get_msg(user_msg)
        print(f"Marcin: {bot_msg}")


test_get_msg_user()
