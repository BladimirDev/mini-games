import string

from projects.enforcado.ascii_design import designs
from projects.enforcado.reader import words_reader
import random


class App:
    def __init__(self):

        self.actual_word = ""
        self.game_word_state = []
        self.word_list = words_reader.get_words()
        self.word_desc_list = words_reader.get_desc()
        self.error_cont = 0

        self.actual_word_choice = 0
        self.select_word()
        self.actual_word_char_list = self.get_actual_word_char_list()

        self.word_actual_letters = []

        self.letters = list(string.ascii_letters)

        self.user_letter = ""
        self.winned = False

    def show_instructions(self):
        print("Bem vindo ao jogo do enforcado!")
        print("~ Nesse jogo vai ser apresentada uma palavra aleatória e você deverá adivinhá-la letra a letra ou inserindo a palavra certa!\n~ Para poder adivinhar a palavra completa você deverá inserir a palavra exata,\n  caso não for, você não receberá nenhuma pista da palavra certa!")
        pass

    def initial(self):
        print("\n~ ENFORCADO -----------------------------------")
        self.show_instructions()

    def select_word(self):
        self.actual_word_choice = random.randint(0, len(self.word_list) - 1)

        self.actual_word = self.word_list[self.actual_word_choice]
        print(self.actual_word)

        for i in range(len(self.actual_word)):
            self.game_word_state.append("_")

    def get_actual_word_char_list(self):

        array = []
        for letter in self.actual_word:
            array.append(letter)

        return array

    def set_actual_letters(self):
        for letter in self.game_word_state:
            self.word_actual_letters.append(self.game_word_state[letter])

    def input_letter(self):
        self.user_letter = ""
        letter = input("Insira uma letra ou palavra: ")
        letter = letter.lower()
        if len(letter) > 1:
            if letter == self.actual_word:
                self.winned = True
        elif len(letter) == 1:
            if letter not in self.letters:
                print("Insira uma letra válida!!")
                self.input_letter()
                return
            self.user_letter = letter
        else:
            print("Insira uma letra ou palavra!")
            self.input_letter()

    def discover_letter(self):
        if self.winned:
            return

        hit = False
        for i in range(len(self.actual_word)):
            if self.user_letter == self.actual_word_char_list[i]:
                hit = True
                self.game_word_state[i] = self.user_letter

        if "_" not in self.game_word_state:
            self.winned = True
        elif not hit:
            self.error_cont += 1
            designs.set_next_design()
            print("Você errou! Erros:", self.error_cont)

    def show_word(self):
        designs.show_design()

        #print("Palavra:", self.actual_word)
        print("Pista:", self.word_desc_list[self.actual_word_choice])

        word_status = ""
        for i in range(len(self.actual_word)):
            word_status += self.game_word_state[i]
            word_status += " "

        print("Word Status:", word_status)

    def show_word_status(self):
        print("Actual Word:", self.actual_word)
        print("User letter:", self.user_letter)

    def run(self):
        self.initial()
        while True:
            if self.winned:
                self.show_word()
                print("Parabéns!, Você ganhou e a palavra era:", self.actual_word.upper() + "!\n")
                designs.set_actual_design(0)
                return
            elif designs.died:
                self.show_word()
                print("Ops.. Você perdeu, a personagem foi enforcada :(, a palavra era:", self.actual_word.upper()+"!\n")
                designs.set_actual_design(0)
                return

            self.show_word()
            self.input_letter()
            self.discover_letter()
