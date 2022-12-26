from Cell import Cell


class Animal:
    def __init__(self, current_Cell):
        self.strength = 1
        self.movility = 1
        self.stamina = 2
        self.initial_stm = 2
        self.current_Cell = current_Cell
    
    def Move(self):
        pass
    def Recovery(self):
        # TODO: Recovery the stamina if the agente pass his turn or if he ate in his turn
        self.stamina+=self.initial_stm - self.stamina





