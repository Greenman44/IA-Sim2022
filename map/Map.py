import random

from animals.Prey import Prey
from animals.Predator import Predator
from .Cell import Cell
from colorama import Fore, Back, Style

class Map:
    def __init__(self, col_amount : int, row_amount : int, max_prey_food, max_pred_food):
        self.col = col_amount
        self.row = row_amount
        self.max_prey_food = max_prey_food
        self.max_pred_food = max_pred_food
        self.cell_List = []
        self.participants = []
        self.Builder_self()
    
    def Builder_self(self, map = []):
        if len(map) > 0:
            self.cell_List = map
            return
        for i in range(self.row):
            self.cell_List.append([])
            for j in range(self.col):
                self.cell_List[i].append(Cell())
            

    def get_max_food(self):
        return (self.max_prey_food, self.max_pred_food)

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

    def SetAnimalDistribution(self,numPreys, numPredators):
        for i in range(numPreys):
            x = random.randint(0,self.row - 1)
            y = random.randint(0,self.col - 1)
            prey = Prey(x,y)       
            self[x,y].animals.append(prey)
            self.participants.append(prey)

        for i in range(numPredators):
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.col - 1)
            pred = Predator(x,y)
            self[x,y].animals.append(pred)
            self.participants.append(pred)
                
    def SetGrassDistribution(self ,grassprob = 0.18):
        for i in range(self.row):
            for j in range(self.col):
                prob = (random.randint(0,self.row*self.col)) /(self.row * self.col)
                if prob > grassprob:
                    self[i,j].food += random.randint(0,self.max_prey_food)


    def __getitem__(self, items):
        if len(items) == 2 and items[0] >= 0 and items[1] >= 0:
            return self.cell_List[items[0]][items[1]]
        raise IndexError() 

    def __setitem__(self, *items, value):
        if len(items) == 2 and items[0] >= 0 and items[1] >= 0:
            self.cell_List[items[0]][items[1]] = value
        raise IndexError()   


