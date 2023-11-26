""" A dataframe of dictionaries is made is from the data of questions and answers with keys of dictionaries as questions and values as answers."""

import pandas as pd
df = pd.DataFrame({"Space": space, "Geography": geography, "Animals": animals, "Science": science, "Sports": sports, "Facts": facts,
                   "Instruments": instruments, "Movies": movies, "Indian Cities": indian_cities,
                   "Indian Athletes": Indian_athletes, "Mythology": Purana})
df

"""The original answer word is changed to question word by substituting letters by "-"."""

import re
def building_question(question_word: str) -> str:
    return re.sub("\w", "-", question_word)

""" Everytime the guessed letter is correct the below function replaces blanks with the respective letter in the respective places."""

def new_word(word: str, letter: str, a: str) -> str:
    for index in range(0, len(a)):
        if a[index] == letter:
            word = word[:index] + letter + word[index + 1:]
    return word

categories = ["Space", "Geography", "Animals", "Science", "Sports", "Facts",
              "Instruments", "Movies", "Indian Cities", "Indian Athletes", "Mythology"]
questions = [0, 1, 2, 3, 4]
