
class Cell:
    def __init__(self):
        self.food = 0
        self.animal = None
        self.restrictions = {
            "vision" : 0,
            "mobility" :  -1,
            "stamina" : 0 
        }
        
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
        self.restrictions["mobility"] = -1
        
        
class PlainCell(Cell):
    def __init__(self):
        self.typeOfCell = "plain"
        super().__init__(self)
        self.restrictions["mobility"] = -1
        
        
                