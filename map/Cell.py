from animals.Predator import Predator
from animals.Prey import Prey


class Cell:
    def __init__(self, food = 0, pred_food = 0):
        self.pred_food = pred_food
        self.food = food
        self.animals = []
        self.typeOfCell = "cell"
        self.restrictions = {
            "vision" : 0,
            "mobility" :  -1,
            "stamina" : 0 
        }
        self.icon = 'C'
    
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
        super().__init__()
        self.typeOfCell = "water"
        self.restrictions["mobility"] = -2
        self.restrictions["stamina"] = -3
        self.icon = 'W'
        
class ForestCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "forest"
        self.restrictions["vision"] = -2
        self.restrictions["mobility"] = -2
        self.icon = 'F'

class MountainCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "mountain"
        self.restrictions["mobility"] = -2
        self.restrictions["stamina"] = -2
        self.icon = 'M'

class MeadowCell(Cell):
    
    def __init__(self):
        super().__init__()
        self.typeOfCell = "meadow"
        self.restrictions["vision"] = -1
        self.icon = 'H'
        
        
class PlainCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "plain"
        self.icon = 'P'
        
        
                