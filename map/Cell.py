from animals.Predator import Predator
from animals.Prey import Prey

class Cell:
    def __init__(self, food = 0, pred_food = 0):
        self.pred_food = pred_food
        self.food = food
        self.animals = []
        self.restrictions = {
            "vision" : 0,
            "mobility" :  -1,
            "stamina" : 0 
        }
        self.icon = [" C"]
    
    def __str__(self):
        if self.animal != None:
            return self.animal.icon
        else:
            return self.icon 

    def predator_in(self):
        for ani in self.animals:
            if type(ani) is Predator:
                return True
        return False
        
    def prey_in(self):
        for ani in self.animals:
            if type(ani) is Prey:
                return True
        return False
        
    # def __repr__(self):
    #     l=[]
    #     for animal in self.animals:
    #         l.append(animal.icon)
    #     return str(l)

        
class WaterCell(Cell):
    def __init__(self):
        self.typeOfCell = "water"
        super().__init__(self)
        self.restrictions["mobility"] = -2
        self.restrictions["stamina"] = -3
        
class ForestCell(Cell):
    def __init__(self):
        self.typeOfCell = "forest"
        super().__init__(self)
        self.restrictions["vision"] = -2
        self.restrictions["mobility"] = -2

class MountainCell(Cell):
    def __init__(self):
        self.typeOfCell = "mountain"
        super().__init__(self)
        self.restrictions["mobility"] = -2
        self.restrictions["stamina"] = -2

class MeadowCell(Cell):
    
    def __init__(self):
        self.typeOfCell = "meadow"
        super().__init__(self)
        self.restrictions["vision"] = -1
        
        
class PlainCell(Cell):
    def __init__(self):
        self.typeOfCell = "plain"
        super().__init__(self)
        
        
                