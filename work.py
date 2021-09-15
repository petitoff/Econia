def msg_text_unification(msg_user):
    msg_user = msg_user.replace(" ", "")
    msg_user = msg_user.lower()

    dct_polish_special_characters = {
        "ą": "a", "ć": "c", "ę": "e", "ł": "l",
        "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}

    dct_special_characters = {"!", "?", ".", ",",
                              "<", ">", "/", ";", "(", ")", ":", '"', "'", ":"}

    # Searching for Polish characters in the text and finding their equivalents in asci without Polish characters.
    asci_table = msg_user.maketrans(dct_polish_special_characters)
    # Translate characters from an ascii array to normal text.
    translate_from_asci = msg_user.translate(asci_table)

    # Removes characters from text if they are in the dictionary.
    translate_from_asci = translate_from_asci.translate(
        {ord(i): None for i in dct_special_characters})

    return translate_from_asci


print(msg_text_unification("Siemka ż!"))
