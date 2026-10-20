class ConfigReader:
    def __init__(self):
        self.games_list_file = "game_list.txt"
        self.brute_game_list = []
        self.games_dict = {}
        self.games_names_list = []

        self.read_games_list_file()
        self.organize_game_list()

    def read_games_list_file(self):
        with open(self.games_list_file, "r", encoding='utf-8') as file:
            for line in file:
                if line is not None:
                    self.brute_game_list.append(line)

    def organize_game_list(self):
        for line in self.brute_game_list:
            parts = line.strip().split(": ", 1)
            if len(parts) != 2:
                continue
            name, path = parts
            self.games_dict[name] = path
