import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")

words_dict =  {row.letter: row.code for (_, row) in df.iterrows()}


def generate_phonetic_word():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [words_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
        generate_phonetic_word()
    else:
        print(output_list)

generate_phonetic_word()