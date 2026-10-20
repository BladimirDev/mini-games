import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_file_lines(relative_path):
    path = os.path.join(BASE_DIR, relative_path)
    with open(path, 'r', encoding='utf-8') as archive:
        return [line for line in archive if line.strip()]


class ConfigReader:
    def __init__(self, language):
        self.configs_dict = {}
        self.brute_configs = []
        self.language_path = "languages/ptbr.txt"

        self.language_dict = {
            "en": "languages/en.txt",
            "es": "languages/es.txt",
            "ptbr": "languages/ptbr.txt"
        }

        self.set_language_path(language)
        self.organize_config_dict()

    def set_language_path(self, language):
        if language in self.language_dict:
            self.configs_dict["language"] = language
            self.language_path = self.language_dict[language]
            return True
        return False

    def read_launch_config(self):
        self.brute_configs.extend(read_file_lines("config.txt"))

    def read_configs(self):
        self.brute_configs.extend(read_file_lines(self.language_path))

    def organize_config_dict(self):
        self.read_launch_config()
        self.read_configs()

        for line in self.brute_configs:
            parts = line.strip().split(": ", 1)
            if len(parts) != 2:
                continue
            option, content = parts
            self.configs_dict[option] = content

    def show_configs(self):
        for line in self.configs_dict:
            print(line + ": " + self.configs_dict[line])

    def get_config(self, option):
        content = self.configs_dict.get(option)

        if content is None:
            return "!!! Empty !!!"
        return content


class Config:
    LANGUAGES = ("en", "es", "ptbr")

    def __init__(self):

        self.language = ""
        self.initial_config()

        configs = ConfigReader(self.language)

        self.tittle_text = configs.get_config("tittle_text")
        self.instructions_message = configs.get_config("instructions_message")
        self.min_number = int(configs.get_config("min_number"))
        self.max_number = int(configs.get_config("max_number"))
        self.input_number_message = configs.get_config("input_number_message") + " "
        self.larger_attempt_message = configs.get_config("larger_attempt_message")
        self.smaller_attempt_message = configs.get_config("smaller_attempt_message")
        self.victory_message = configs.get_config("victory_message")
        self.attempts_message1 = configs.get_config("attempts_message1")
        self.attempts_message2 = configs.get_config("attempts_message2")
        self.choice_language_message = configs.get_config("choice_language_message")
        self.no_valid_number_message = configs.get_config("no_valid_number_message")
        self.out_of_range_message = configs.get_config("out_of_range_message")

    def set_language(self):
        message = "Please, choice your language (en / es / ptbr)"
        for line in read_file_lines("config.txt"):
            option, _, content = line.strip().partition(": ")
            if option == "choice_language_message":
                message = content

        while True:
            language = input(message + ": ").strip().lower()
            if language in self.LANGUAGES:
                self.language = language
                return

    def initial_config(self):
        self.set_language()


config = Config()
