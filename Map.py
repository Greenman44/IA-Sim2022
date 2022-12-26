from Cell import Cell

class Map:
    def __init__(self, col_amount:int,row_amount:int):
        self.col = col_amount
        self.row = row_amount
        self.cell_List=[[Cell]]
    
    def Builder_Map(self):
        for i in range(self.row):
            for j in range(self.col):
                self.cell_List[i,j] = Cell(i,j)
    
    def IA_Cell_Builder(self):
        # TODO: Implemnt an IA for create the feature of every cell in the map
        pass
    
class TestMap(Map):
    def __init__(self, testMap:list[list[Cell]]):
        self.cell_List = testMap 
