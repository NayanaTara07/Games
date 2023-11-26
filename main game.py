import random
print("CHOOSE A CATEGORY")
print(categories)
category = input()
question_number = random.choice(questions)
print(list(df[category].iloc[question_number].keys())[0] + "\n")
question_word = list(df[category].iloc[question_number].values())[0].lower()
dashes = len(question_word.replace(" ", ""))
wrong = 0
word = building_question(question_word)
entered_letters = []
print(word + "\n")
while wrong != 8 and dashes != 0:
    letter = input()
    if letter in entered_letters:
        print(f"LETTER ALREADY TRIED\nTRY ANOTHER\n{8 - wrong} CHANCES LEFT\n" + word + "\n")
    elif letter in question_word:
        entered_letters.append(letter)
        word = new_word(word, letter, question_word)
        dashes -= question_word.count(letter)
        print("\n" + word + "\n")
    else:
        entered_letters.append(letter)
        wrong += 1
        print(f"INCORRECT\nTRY AGAIN\n{8 - wrong} CHANCES LEFT")
        print(word + "\n")
if wrong == 8:
    print("LEVEL FAILED")
else:
    print("LEVEL PASSED")