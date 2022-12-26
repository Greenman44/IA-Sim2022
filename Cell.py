
class Cell:
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    
class CellOfWater(Cell):
    def __init__(self, x, y):
        self.typeOfCell = "water"
        super().__init__(x, y)
