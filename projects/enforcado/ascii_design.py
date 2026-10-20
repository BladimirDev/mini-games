class Design:
    def __init__(self):
        self.desings = [
            """
                    
                    |
                    |
                    |
                    |
                    |
                   _|_
            """,
            """
                    _______
                    |     |
                    |
                    |
                    |
                    |
                   _|_
            """,
            """  
                     _______
                     |     |
                     |     O
                     |
                     |
                     |
                    _|_
            """,
            """  
                     _______
                     |     |
                     |     O
                     |    /|
                     |     |
                     |
                    _|_
            """,
            """  
                     _______
                     |     |
                     |     O
                     |    /|l
                     |     |
                     |
                    _|_
            """,
            """  
                     _______
                     |     |
                     |     O
                     |    /|l
                     |     |
                     |    /
                    _|_
            """,
            """  
                     _______
                     |     |
                     |     O
                     |    /|l
                     |     |
                     |    / L
                    _|_
            """,
        ]

        self.actual_design = """"""
        self.actual_design_key = 0
        self.died = False

        self.set_actual_design(0)

    def set_actual_design(self, number):
        self.actual_design = self.desings[number]
        self.actual_design_key = number
        self.died = False

    def set_next_design(self):
        last = len(self.desings) - 1
        if self.actual_design_key < last:
            self.actual_design_key += 1
            self.actual_design = self.desings[self.actual_design_key]

        if self.actual_design_key == last:
            self.died = True

    def show_design(self):
        print(self.actual_design)

designs = Design()