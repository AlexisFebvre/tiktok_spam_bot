from random import shuffle, randint
from time import sleep

def do_sentence():
    subject_type = randint(1, 6)
    if subject_type == 1:
        subject = ["Je"]
        verb = ["sors", "mange"]
    elif subject_type == 2:
        subject = ["Tu"]
        verb = ["sors", "manges"]
    elif subject_type == 3:
        subject = ["Il", "Elle", "On", "Alexis", "Sandra", "Maxime", "Ta mère", "Ton père", "Ton chien", "Ton chat"]
        verb = ["sort", "mange"]
    elif subject_type == 4:
        subject = ["Nous", "Mes amis et moi", "Ma famille et moi"]
        verb = ["sortons", "mangons"]
    elif subject_type == 5:
        subject = ["Vous", "Vous autres", "Sandra et toi"]
        verb = ["sortez", "mangez"]
    elif subject_type == 6:
        subject = ["Ils", "Elles", "Les chiens", "Les chats", "Les familles", "Johana et Deni", "Maxime et Gontran"]
        verb = ["sortent", "mangent"]
    cod = ["un chat", "des mouchoir", "dehors", "un ordinateur"]
    
    shuffle(subject)
    shuffle(verb)
    shuffle(cod)
    sentence = subject[0] + " " + verb[0] + " " + cod[0] + "."
    return sentence