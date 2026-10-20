import random

try:
    from projects.adivinhe_o_numero.config import config
except ModuleNotFoundError:
    from config import config

class App:
    def __init__(self):
        self.number = random.randint(config.min_number, config.max_number)
        self.user_number = 0
        self.attempts = 0

    def show_instructions(self):
        print(config.instructions_message)

    def input_number(self):
        while True:
            try:
                number = int(input(config.input_number_message))
            except ValueError:
                print(config.no_valid_number_message)
                continue
            if number > config.max_number or number < config.min_number:
                print(config.out_of_range_message)
                continue
            self.user_number = number
            return True

    def initial(self):
        print("\n~", config.tittle_text,"----------------------------")
        self.show_instructions()
        self.input_number()

    def attempt(self):

        if self.user_number < self.number:
            print(config.larger_attempt_message)

        if self.user_number > self.number:
            print(config.smaller_attempt_message)

        self.attempts += 1

        if self.user_number == self.number:
            self.victory()
            return True
        self.input_number()
        return False


    def victory(self):
        print(config.victory_message)
        print(config.attempts_message1,  self.attempts, config.attempts_message2)

    def run(self):

        self.initial()

        while True:
            if self.attempt():
                break

def main ():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
