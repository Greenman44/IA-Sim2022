from animals.Animal import *
from map.Map import Map
from Tools import K_BFS

class Prey_vs_Predator:
    def __init__(self, map: Map , animals: list[Animal]):
        self.map = map
        self.animals = animals

    def Actions(self, current_animal: Animal):
        return K_BFS(current_animal.pos_x, current_animal.pos_y, current_animal.data["mobility"], self.map,False)

    # def Result(): 
    #     pass
    
    # def Utility():
    #     pass

    def Is_Terminal(self, animals: list[Animal]):
        if len(animals) == 1:
            return True
        return False
        