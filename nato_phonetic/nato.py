# TODO: input a name, word etc. to get the phonetic of it as output --done
# e.g. input = Raj out = [Romeo, Alpha, Juliet]
# The csv contains the phonetic codes w.r.t each alphabet
import pandas as pd

df = pd.read_csv('./nato_phonetic_alphabet.csv')
letters = df.letter.to_list()
codes = df.code.to_list()

while True:
    user_input = input("Enter a word to get Nato codes: \n")
    print([df[df['letter'] == alpha].code.item() for alpha in user_input.upper()])
    prompt = input("Do you want to continue?: \n")
    if prompt == "no":
        break



