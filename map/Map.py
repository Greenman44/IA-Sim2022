from .Cell import Cell

class Map:
    def __init__(self, col_amount : int, row_amount : int):
        self.col = col_amount
        self.row = row_amount
        self.cell_List = []
    
    def Builder_Map(self, map = []):
        if len(map) > 0:
            self.cell_List = map
            return
        for i in range(self.row):
            self.cell_List.append([])
            for j in range(self.col):
                self.cell_List[i].append(Cell())
            
    def IA_Cell_Builder(self):
        # TODO: Implemnt an IA for create the feature of every cell in the map
        pass

    def get_max_food(self):
        return 20, 20


    def __getitem__(self, items):
        if len(items) == 2 and items[0] >= 0 and items[1] >= 0:
            return self.cell_List[items[0]][items[1]]
        raise IndexError() 

    def __setitem__(self, *items, value):
        if len(items) == 2 and items[0] >= 0 and items[1] >= 0:
            self.cell_List[items[0]][items[1]] = value
        raise IndexError()   


