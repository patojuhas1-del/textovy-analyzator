# Projekt 1: Textový analyzátor

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123" 
}

username = input("username:")
password = input("password:")
if username in registered_users and registered_users[username] == password:
    print("-" * 40)
    print("Welcome to the app,", username)
    print("We have", len(TEXTS), "texts to be analyzed.")
    print("-" * 40)
    text_number = input("Enter a number btw. 1 and " + str(len(TEXTS)) + " to select: ")
    if not text_number.isdigit():
        print("Input is not a number, terminating the program")
    elif int(text_number) < 1 or int(text_number) > len(TEXTS):
        print("There are only", len(TEXTS), "texts, terminating the program")
    else:
        index = int(text_number) - 1
        selected_text = TEXTS[index]
        words = selected_text.split()    
        print("-" * 40)
        print("There are", len(words), "words in the selected text.")
        title_words = 0
        upper_words = 0
        lower_words = 0
        numbers = 0
        total = 0
        lengths = {}
        for word in words:
            if word.istitle():
                title_words = title_words + 1
            if word.isupper():
                upper_words = upper_words + 1
            if word.islower():
                lower_words = lower_words + 1
            if word.isdigit():
                numbers = numbers + 1
                total = total + int(word)
            clean_word = word.strip(",.")
            length = len(clean_word)
            if length in lengths:
                lengths[length] = lengths[length] + 1
            else:
                lengths[length] = 1
        print("There are", title_words, "titlecase words.")
        print("There are", upper_words, "uppercase words.")
        print("There are", lower_words, "lowercase words.")
        print("There are", numbers, "numeric strings.")
        print("The sum of all the numbers", total)
        print("-" * 40)
        width = max(lengths.values()) + 4
        print("LEN|" + "OCCURRENCES".center(width) + "|NR.")
        print("-" * 40)
        for length in sorted(lengths):
            print(str(length).rjust(3) + "|" + ("*" * lengths[length]).ljust(width) + "|" + str(lengths[length]))     
else:
    print("unregistered user, terminating the program..")

