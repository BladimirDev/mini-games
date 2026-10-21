class WordsReader:
    def __init__(self):
        self.words_file = "projects/enforcado/words_list.txt" #
        self.words_list = {}
        self.read_word_file()


    def read_word_file(self):
        with open(self.words_file, "r", encoding="utf-8") as file:
            for line in file:
                if line is not None:
                    line = line.strip().split(": ")
                    word = line[0]
                    desc = line[1]
                    self.words_list[word] = desc

    def get_words(self):
        list = []
        for word in self.words_list:
            list.append(word)
        return list

    def get_desc(self):
        list = []
        for word in self.words_list:
            list.append(self.words_list[word])
        return list

    def show_all_words(self):
        for word in self.words_list:
            print(word,":", self.words_list[word])

words_reader = WordsReader()
