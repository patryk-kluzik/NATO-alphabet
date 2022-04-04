import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# ----- updating project to handle exceptions ----- #

def spell_word():
    word = input("Enter a word: ").upper()

    try:
        result = [nato_alphabet[character] for character in word]
    except KeyError:
        print("Sorry, text you entered is invalid. Please only use letters in the alphabet")
        spell_word()
    else:
        print(result)


spell_word()
