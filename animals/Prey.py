from animals.Animal import *

class Prey(Animal):
    def __init__(self):
        super().__init__()
    
    def get_perception(self):
        return super().get_perception()

    def Move(self):
        return super().Move()

    def Recovery(self):
        return super().Recovery()

class Deer(Prey):
    def __init__(self):
        self.strength = super
        self.mobility = 3
        self.stamina, self.initial_stm = 6
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()

class Hare(Prey):
    def __init__(self):
        self.strength = super
        self.mobility = super
        self.stamina, self.initial_stm = 4
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()

class Zebra(Prey):
    def __init__(self):
        self.strength = super
        self.mobility = 2
        self.stamina, self.initial_stm = 5
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()

class Monkey(Prey):
    def __init__(self):
        self.strength = super
        self.mobility = 2
        self.stamina, self.initial_stm = 4
    def Move(self):
        return super().Move()
    def Recovery(self):
        return super().Recovery()