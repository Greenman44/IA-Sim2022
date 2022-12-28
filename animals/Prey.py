from animals.Animal import *
from animals.Predator import *

class Prey(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
    
    def get_perception(self, map):
        pass

    def Interaction(self, map: Map, pos):
        map[pos].animals.add(self)
        if map[pos].food != 0:
            self.Recovery()
        map[pos].icon.append(self.icon)

    def Move(self,map,play):
        return super().Move(map,play)

    def Recovery(self):
        return super().Recovery()

class Deer(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " D"
        self.mobility = 7
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 9
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Hare(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " H"
        self.mobility = 6
        self.stamina = 4
        self.initial_stm = 4
        self.vision = 4
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Zebra(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " Z"
        self.mobility = 4
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 5
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Monkey(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " M"
        self.mobility = 4
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 6
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()