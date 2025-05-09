import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")

words_dict =  {row.letter: row.code for (_, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()

# result = [word for (key, word) in words_dict.items() if key.upper() in user_input]
output_list = [words_dict[letter] for letter in user_input]
print(output_list)