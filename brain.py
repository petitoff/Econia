import json


class Chat:
    def __init__(self):
        self.msg_user = ""  # Variable holding the message sent by the user.
        self.msg_bot = ""  # Variable holding the message the bot will send.

    def get_msg(self, msg):
        self.msg_user = msg
        self.msg_analyze()
        return self.msg_bot

    def msg_analyze(self):
        self.msg_text_unification()

        run_brain.put_in_dct(self.msg_user)

        self.msg_bot = self.msg_user
        return

    def msg_text_unification(self):
        self.msg_user = self.msg_user.replace(" ", "")
        self.msg_user = self.msg_user.lower()

        dct_polish_special_characters = {
            "ą": "a", "ć": "c", "ę": "e", "ł": "l",
            "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}

        dct_special_characters = {"!", "?", ".", ",",
                                  "<", ">", "/", ";", "(", ")", ":", '"', "'", ":"}

        # Searching for Polish characters in the text and finding their equivalents in asci without Polish characters.
        asci_table = self.msg_user.maketrans(dct_polish_special_characters)
        # Translate characters from an ascii array to normal text.
        translate_from_asci = self.msg_user.translate(asci_table)

        # Removes characters from text if they are in the dictionary.
        # translate_from_asci = translate_from_asci.translate(
        #     {ord(i): None for i in dct_special_characters})

        self.msg_user = translate_from_asci


class Brain:
    def __init__(self):
        self.data_msg_user_contex = []

    def brain_main(self):
        self.cleaning_special_characters()

    def put_in_dct(self, user_msg):
        if user_msg[-1] == "?":
            kind = "question"
        elif user_msg[-1] == "!":
            kind = "order"
        elif user_msg[-1] == ".":
            kind = "claim"
        else:
            kind = None

        self.data_msg_user_contex.append({"text": user_msg, "kind": kind})
        self.brain_main()

    def cleaning_special_characters(self):
        translate_from_asci = self.data_msg_user_contex[-1]["text"]

        dct_special_characters = {"!", "?", ".", ",",
                                  "<", ">", "/", ";", "(", ")", ":", '"', "'", ":"}

        translate_from_asci = translate_from_asci.translate(
            {ord(i): None for i in dct_special_characters})

        self.data_msg_user_contex[-1].update(
            {"text": translate_from_asci})


run_chat = Chat()
run_brain = Brain()
