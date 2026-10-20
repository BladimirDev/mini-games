import random


class App:
    def __init__(self):
        self.choices_dict = {
            1: "rock",
            2: "paper",
            3: "scissors"
        }

        self.actors_choices = [0, 0]
        self.try_again = None


    def show_instructions(self):
        print("Nesse jogo, você irá inserir uma das opções abaixo e aleatóriamente o algoritmo fará uma escolha, dependendo do resultado você vai ganhar ou perder!")

    def show_choices(self):
        print("0 - Get Out")
        for choice in self.choices_dict:
            print(choice, "-", self.choices_dict[choice])

    def initial(self):
        print("\n~ Jo Ken Po! -----------------------")
        self.show_instructions()

    def input_choice(self):
        while True:
            try:
                choice = int(input("Insira o número da sua escolha!: "))
            except ValueError:
                choice = None
            if choice in [1, 2, 3]:
                break
            print("Por favor, insira um valor correto!")
        self.actors_choices[0] = choice

    def machine_choice_randomize(self):
        self.actors_choices[1] = random.randint(1, 3)

    def show_actors_choices(self):
        print("Usuário: %s" %self.choices_dict[self.actors_choices[0]])
        print("Máquina: %s" %self.choices_dict[self.actors_choices[1]])

    def set_result(self,):
        user_choice = self.actors_choices[0]
        machine_choice = self.actors_choices[1]

        match self.actors_choices[0]:
            case 1:
                match machine_choice:
                    case 2:
                        return False
                    case 3:
                        return True

            case 2:
                match machine_choice:
                    case 1:
                        return True
                    case 3:
                        return False
            case 3:
                match machine_choice:
                    case 1:
                        return False
                    case 2:
                        return True
        return None

    def show_final_message(self):
        if self.set_result() is None:
            print("EMPATE\n")
            return

        if self.set_result():
            print("Parabéns, Você Venceu!\n")
            return
        print("Boa tentativa, mas a Máquina Venceu!\n")

    def show_try_again_message(self):
        print("Jogar de novo? y/n")

    def input_try_again(self):
        while True:
            choice = input("Tentar de novo? y/n: ")
            if choice in ["y", "n"]:
                break
            print("Escolha uma opção válida!")
        self.try_again = choice == "y"


    def run(self):
        self.initial()

        while True:
            self.show_choices()
            self.input_choice()
            self.machine_choice_randomize()
            self.show_actors_choices()
            self.show_final_message()
            self.input_try_again()

            if not self.try_again:
                break



def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()