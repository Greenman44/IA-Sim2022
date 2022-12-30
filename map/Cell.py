from animals.Predator import Predator


class Cell:
    def __init__(self):
        self.pred_food = 0
        self.food = 0
        self.animals = set()
        self.typeOfCell = "celda"
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
        for ani in self.animal:
            if ani is Predator:
                return True
        return False
        
    def __repr__(self):
        l=[]
        for animal in self.animals:
            l.append(animal.icon)
        return str(l)

        
class WaterCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "water"
        self.restrictions["mobility"] = -2
        self.restrictions["stamina"] = -3
        
class ForestCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "forest"
        self.restrictions["vision"] = -2
        self.restrictions["mobility"] = -2

class MountainCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "mountain"
        self.restrictions["mobility"] = -2
        self.restrictions["stamina"] = -2

class MeadowCell(Cell):
    
    def __init__(self):
        super().__init__()
        self.typeOfCell = "meadow"
        self.restrictions["vision"] = -1
        
        
class PlainCell(Cell):
    def __init__(self):
        super().__init__()
        self.typeOfCell = "plain"
        
        
                