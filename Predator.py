from Animal import *

class Predator(Animal):
    def __init__(self):
        super().__init__()
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()

class Lion(Predator):
    def __init__(self):
        self.strength = 3
        self.movility = 3
        self.stamina, self.initial_stm = 4
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()

class Wolf(Predator):
    def __init__(self):
        self.strength = 2
        self.movility = 4
        self.stamina, self.initial_stm = 3
    def Move(self):
        return super().Move()

    def Recovery(self):
        return super().Recovery()

class Tiger(Predator):
    def __init__(self):
        self.strength = 3
        self.movility = 3
        self.stamina,self.initial_stm = 5
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()
