
import spacy
import random
import requests
model = spacy.load('en_core_web_lg')


# mots = ["python", "programmation", "intelligence", "machine", "apprentissage"]
# secret = random.choice(mots)
#secret = "pizza"


def Select_secret():
    secret = requests.get("https://random-word-api.herokuapp.com/word")
    data = secret.json()
    token_secret = model(data[0])


    if (token_secret.has_vector):
        print(token_secret[0])
        Home(token_secret)
    else:
        Select_secret()



def New_Test(token_secret):
    given_word = input("votre nouveau essai : ")

    if (model(given_word).has_vector):
        token_given_word = model(given_word)
        similarity = token_given_word.similarity(token_secret)
        Test_Similarity(similarity, token_given_word, token_secret)
    else:
        print("Ce mot n'est pas référencé, pensez à écrire en anglais !")
        New_Test(token_secret)

def Test_Similarity(similarity, token_given_word, token_secret):
    if similarity == 1:
        print('gagné !')
        print('rejoué ?!')
        response = input()
        if (response == "yes"):
            Select_secret()
        else:
            if (response == "no"):
                print("Tans pis ... bye")
            else:
                print("Je n'ai pas compris ... on va faire genre qu'on sais jamais vu !")
                Select_secret()
    else:
        message = "le mot " + token_given_word.text + " est a " + str(round(similarity * 100, 2)) + " °C"
        print(message)
        New_Test(token_secret)


def Start(token_secret):
    given_word = input("votre mot : ")

    if(model(given_word).has_vector):
        token_given_word = model(given_word)
        similarity = token_given_word.similarity(token_secret)
        Test_Similarity(similarity, token_given_word, token_secret)
    else:
        print("Ce mot n'est pas référencé, pensez à écrire en anglais !")
        New_Test(token_secret)




def Home(token_secret):
    print("Welcome sur le jeu Cemantix, souhaitez-vous jouer ?!  (yes / no) ")
    response = input()

    if(response == "yes"):
        Start(token_secret)
    else:
        if(response == "no"):
            print("Tans pis ... bye")
        else:
            print("Je n'ai pas compris ... on va faire genre qu'on sais jamais vu !")
            Home(token_secret)




Select_secret()