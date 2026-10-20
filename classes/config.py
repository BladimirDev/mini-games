from classes.config_reader import ConfigReader

import importlib

class Config:
    def __init__(self):
        config_reader = ConfigReader()

        self.game_list_dict = {}
        self.game_dict = config_reader.games_dict

        self.create_game_list_dict()

    def create_game_list_dict(self):
        cnt = 1
        for game in self.game_dict:
            self.game_list_dict[cnt] = game
            cnt += 1

    def show_game_list(self):
        for number in self.game_list_dict:
            print(number, "-", self.game_list_dict[number])

    def get_game_path(self, option):
        return self.game_dict[self.game_list_dict[option]]

    def run_game(self, path: str):
        module = importlib.import_module(path)

        if hasattr(module, "main"):
            module.main()
        else:
            print("This game not exists")

config = Config()