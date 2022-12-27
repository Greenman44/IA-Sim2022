
class Cell:
    def __init__(self):
        self.food = 0
        self.animal = None
        self.restrictions = [0,0,0]
class WaterCell(Cell):
    def __init__(self):
        self.typeOfCell = "water"
        super().__init__(self)
        self.restrictions = [0,-2,-3]
        
class ForestCell(Cell):
    def __init__(self):
        self.typeOfCell = "forest"
        super().__init__(self)
        self.restrictions = [-2,-2,0]
class MountainCell(Cell):
    def __init__(self):
        self.typeOfCell = "mountain"
        super().__init__(self)
        self.restrictions = [0,-2,-2]
class MeadowCell(Cell):
    def __init__(self):
        self.typeOfCell = "meadow"
        super().__init__(self)
        self.restrictions = [-1,0,0]
        self.food += 10
class PlainCell(Cell):
    def __init__(self):
        self.typeOfCell = "plain"
        super().__init__(self)
        
                