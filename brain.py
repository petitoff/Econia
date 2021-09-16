

class Chat:
    def __init__(self):
        msg_user = ""  # Variable holding the message sent by the user.
        self.msg_bot = ""  # Variable holding the message the bot will send.

    def get_msg(self, msg):
        run_brain.brain_main(msg)
        return self.msg_bot


class Brain:
    def __init__(self):
        self.data_msg_user_contex = []

    def brain_main(self, user_msg):
        self.put_in_dct(user_msg)

        self.cleaning_special_characters()

        self.basic_search()
        self.looking_for_possible_meaning()

        print(self.data_msg_user_contex)

    def put_in_dct(self, user_msg):
        self.data_msg_user_contex.append(
            {"textMain": user_msg.replace(" ", "")})

        user_msg = self.msg_text_unification(user_msg)

        if user_msg[-1] == "?":
            kind = "question"
        elif user_msg[-1] == "!":
            kind = "order"
        elif user_msg[-1] == ".":
            kind = "claim"
        else:
            kind = None

        self.data_msg_user_contex[-1].update(
            {"textUni": user_msg, "kind": kind})

    def msg_text_unification(self, user_msg):
        user_msg = self.data_msg_user_contex[-1]["textMain"]
        user_msg = user_msg.lower()

        dct_polish_special_characters = {
            "ą": "a", "ć": "c", "ę": "e", "ł": "l",
            "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}

        # Searching for Polish characters in the text and finding their equivalents in asci without Polish characters.
        asci_table = user_msg.maketrans(dct_polish_special_characters)
        # Translate characters from an ascii array to normal text.
        translate_from_asci = user_msg.translate(asci_table)
        return translate_from_asci

    def cleaning_special_characters(self):
        translate_from_asci = self.data_msg_user_contex[-1]["textUni"]

        dct_special_characters = {"!", "?", ".", ",",
                                  "<", ">", "/", ";", "(", ")", ":", '"', "'", ":"}

        translate_from_asci = translate_from_asci.translate(
            {ord(i): None for i in dct_special_characters})

        self.data_msg_user_contex[-1].update(
            {"textUniSepcial": translate_from_asci})

    def context(self):
        pass

    def basic_search(self):
        msg_user = self.data_msg_user_contex[-1]["textUniSepcial"]

    def looking_for_possible_meaning(self):
        if self.data_msg_user_contex[-1]["kind"] == "question":
            pass


run_chat = Chat()
run_brain = Brain()
