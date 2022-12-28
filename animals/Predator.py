from animals.Animal import *
from animals.Prey import *
from map.Map import Map
from map.Cell import *

class Predator(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
    
    def get_perception(self, map):
        pass

    def Interaction(self, map: Map, pos):
        animals = map[pos].animals
        if animals != None:
            self.Combat(animals, map, pos)

    def Combat(self, animals, map, pos):
        # TODO: Make a best stocastic combat with strength and another prop
        new_animal=set()
        new_icon=[]
        for animal in animals:
            r = random.random()
            if r > 0.5:
                new_animal.add(self)
                new_icon.append(self.icon)
                if len(new_icon)!=len(new_animal):
                    new_icon.remove(self.icon)
            else:
                new_animal.add(animal)
                new_icon.append(animal.icon)
                new_animal.add(self)
                new_icon.append(self.icon)
                if len(new_icon) != len(new_animal):
                    new_icon.remove(self.icon)
                    
        map[pos].animals = new_animal
        map[pos].icon = new_icon

    
    def Move(self,map,play):
        return super().Move(map,play)
    
    def Recovery(self):
        return super().Recovery()

class Lion(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " L"
        self.strength = 3
        self.mobility = 5
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 6
        map[posx,posy].icon.append(self.icon)

    def Interaction(self, map: Map, pos):
        return super().Interaction(map, pos)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Wolf(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " W"
        self.strength = 2
        self.mobility = 8
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 8
        map[posx,posy].icon.append(self.icon)

    def Interaction(self, map: Map, pos):
        return super().Interaction(map, pos)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Tiger(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " T"
        self.strength = 3
        self.mobility = 5
        self.stamina = 7
        self.vision = 8
        self.initial_stm = 7
        map[posx,posy].icon.append(self.icon)

    def Interaction(self, map: Map, pos):
        return super().Interaction(map, pos)
    def Move(self, map, play):
        return super().Move(map, play)
    def Recovery(self):
        return super().Recovery()
