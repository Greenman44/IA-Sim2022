from .Cell import Cell
from colorama import Fore, Back, Style

class Map:
    def __init__(self, col_amount : int, row_amount : int):
        self.col = col_amount
        self.row = row_amount
        self.cell_List = []
        self.Builder_self()
    
    def Builder_self(self, map = []):
        if len(map) > 0:
            self.cell_List = map
            return
        for i in range(self.row):
            self.cell_List.append([])
            for j in range(self.col):
                self.cell_List[i].append(Cell())
            
    def IA_Cell_Builder(self):
        # TODO: Implemnt an IA for create the feature of every cell in the self
        pass

    def get_max_food(self):
        return 20, 20

    def pretty_self(self):
        for i in range(self.row):
            for j in range(self.col):
                if j==self.col-1:
                    # if self[i,j].animals != None:
                    #     print(self[i,j].animals[0].icon)
                    if self[i,j].icon == "P":
                        print(Fore.YELLOW,self[i,j].icon)
                    elif self[i,j].icon == "W":
                        print(Fore.BLUE,self[i,j].icon)
                    elif self[i,j].icon == "M":
                        print(Fore.MAGENTA,self[i,j].icon)
                    elif self[i,j].icon == "F":
                        print(Fore.RED,self[i,j].icon)
                    elif self[i,j].icon == "H":
                        print(Fore.GREEN,self[i,j].icon)
                else:
                    # if self[i,j].animals != None:
                    #     print(self[i,j].animals[0].icon, end="")
                    if self[i,j].icon == "P":
                        print(Fore.YELLOW, self[i,j].icon, end="")
                    elif self[i,j].icon == "W":
                        print(Fore.BLUE, self[i,j].icon, end="")
                    elif self[i,j].icon == "M":
                        print(Fore.MAGENTA, self[i,j].icon, end="")
                    elif self[i,j].icon == "F":
                        print(Fore.RED, self[i,j].icon, end="")
                    elif self[i,j].icon == "H":
                        print(Fore.GREEN, self[i,j].icon, end="")


    def __getitem__(self, items):
        if len(items) == 2 and items[0] >= 0 and items[1] >= 0:
            return self.cell_List[items[0]][items[1]]
        raise IndexError() 

    def __setitem__(self, *items, value):
        if len(items) == 2 and items[0] >= 0 and items[1] >= 0:
            self.cell_List[items[0]][items[1]] = value
        raise IndexError()   


