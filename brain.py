from auxiliary_functions import search_in_json1

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition

"""Preparation of text-to-speech conversion."""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class Chat:
    def __init__(self):
        msg_user = ""  # Variable holding the message sent by the user.
        self.msg_bot = ""  # Variable holding the message the bot will send.

    def get_msg(self, msg):
        run_brain.brain_main(msg)
        return self.msg_bot


class Brain:
    def __init__(self):
        self.data_msg_user_context = []

    def brain_main(self, user_msg):
        self.put_in_dct(user_msg)

        self.cleaning_special_characters()

        self.basic_search()
        self.looking_for_possible_meaning()

        print(self.data_msg_user_context)

    def put_in_dct(self, user_msg):
        self.data_msg_user_context.append(
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

        self.data_msg_user_context[-1].update(
            {"textUni": user_msg, "kind": kind})

    def msg_text_unification(self, user_msg):
        user_msg = self.data_msg_user_context[-1]["textMain"]
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
        translate_from_asci = self.data_msg_user_context[-1]["textUni"]

        dct_special_characters = {"!", "?", ".", ",",
                                  "<", ">", "/", ";", "(", ")", ":", '"', "'", ":"}

        translate_from_asci = translate_from_asci.translate(
            {ord(i): None for i in dct_special_characters})

        self.data_msg_user_context[-1].update(
            {"textUniSepcial": translate_from_asci})

    def context(self):
        pass

    def basic_search(self):
        msg_user = self.data_msg_user_context[-1]["textUniSepcial"]

    def looking_for_possible_meaning(self):
        # If the basic context is specified then check if the sentence is meaningless in the database.
        if self.data_msg_user_context[-1]["kind"] is not None:
            if self.data_msg_user_context[-1]["kind"] == "question":
                search_in_json1(self.data_msg_user_context, "question")

    def speach_recognation(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='pl-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return None
        return query


run_chat = Chat()
run_brain = Brain()
