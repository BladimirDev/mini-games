from classes.config import config
import os


class App:
    def __init__(self):
        self.option = None

        pass

    def show_menu(self):
        print("Please, choice a game!")
        print("0 - Get Out")
        config.show_game_list()

    def input_option(self):
        while True:
            try:
                option = int(input("Option: "))
            except ValueError:
                print("Errado! Insira um número válido!")
                continue
            if option < 0 or option > len(config.game_list_dict):
                print("Errado! Insira um número válido!")
                continue
            self.option = option
            return option

    def run_game(self, option):

        path = config.get_game_path(option)
        config.run_game(path)

    def run(self):
        while True:
            self.show_menu()
            option = self.input_option()
            if option == 0:
                break
            self.run_game(option)


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
