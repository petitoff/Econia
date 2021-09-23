from brain import run_brain
from brain import speak


# run_brain.speach_recognation()


# def test_get_msg_user():
#     while True:
#         user_msg = input("You: ")
#         bot_msg = run_chat.get_msg(user_msg)
#         print(f"Marcin: {bot_msg}")


def test_get_voice_user():
    # speak("Dzień dobry proszę pana.")
    # speak("W czym mogę pomóc?")
    while True:
        # user_msg = run_brain.speach_recognation()  # The function returns what it heard. Otherwise None.
        user_msg = input(": ")
        if user_msg is not None:
            bot_msg = run_brain.brain_main(user_msg)
            print(bot_msg)
            speak(bot_msg)


# test_get_msg_user()
test_get_voice_user()
