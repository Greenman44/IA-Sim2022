from map.Cell import Cell
from Tools import K_BFS

class Map:
    def __init__(self, col_amount : int, row_amount : int):
        self.col = col_amount
        self.row = row_amount
        self.cell_List = []
    
    def Builder_Map(self):
        for i in range(self.row):
            self.cell_List.append([])
            for j in range(self.col):
                self.cell_List[i].append(Cell())
            
    def IA_Cell_Builder(self):
        # TODO: Implemnt an IA for create the feature of every cell in the map
        pass


    def __getitem__(self, items):
        if len(items) == 2:
            return self.cell_List[items[0]][items[1]]
        raise IndexError() 

    def __setitem__(self, *items, value):
        if len(items) == 2:
            self.cell_List[items[0]][items[1]] = value
        raise IndexError()   

    def get_cells_with_KDistance(self, init_x : int, init_y: int, k : int):
        return K_BFS(init_x, init_y, k, self)
