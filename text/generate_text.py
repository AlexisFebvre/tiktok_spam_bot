from random import randint, shuffle
from json import load

def do_sentence():
    subject = randint(0, 5)
    if subject == 0:
        subject = "je"
    elif subject == 1:
        subject = "tu"
    elif subject == 2:
        subject = "il"
    elif subject == 3:
        subject = "nous"
    elif subject == 4:
        subject = "vous"
    elif subject == 5:
        subject = "ils"

    path = f"assets/words.json"
    sentence = "default"


    with open(path, 'r') as json_data:
        words = load(json_data)
        verb = words[subject]["verbe"]
        subject = words[subject]["sujet"]
        cod = words["cod"]
        shuffle(cod)
        shuffle(verb)
        shuffle(subject)
        sentence = f"{subject[0]} {verb[0]} {cod[0]}."
    return sentence


