class WordsReader:
    def __init__(self):
        self.words_file = "projects/enforcado/words_list.txt"
        self.words_list = []
        self.read_word_file()


    def read_word_file(self):
        with open(self.words_file, "r", encoding="utf-8") as file:
            for line in file:
                if line is not None:
                    self.words_list.append(line.strip())

    def show_all_words(self):
        for word in self.words_list:
            print(word)

words_reader = WordsReader()
words_reader.show_all_words()
