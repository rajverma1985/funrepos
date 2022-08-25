# TODO: Create a letter using starting_letter.txt

class Letter:
    def __init__(self):
        self.word = "[name]"
        self.input_path = "./Input/Names/invited_names.txt"
        self.output = "f'./Output/ReadyToSend/Letter_for_{name}.txt'"
        self.write_letter()

    def read_stuff(self):
        with open(self.input_path) as file:
            names = [line.rstrip() for line in file.readlines()]
        return names

    def write_letter(self):
        with open('./Input/Letters/starting_letter.txt') as letter:
            read_letter = letter.read()
            for name in self.read_stuff():
                new_letter = read_letter.replace('[name]', name)
                with open(f'./Output/ReadyToSend/Letter_for_{name}.txt', "w") as completed_letter:
                    completed_letter.write(new_letter)


new_letters = Letter()
