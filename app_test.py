from map.Map import Map
from map.Cell import Cell
from animals.Animal import Animal
from animals.Predator import * 
from animals.Prey import *
from typing import Dict, List, Optional
from iAalgorithm.CSP_Map import *
from iAalgorithm.CSP import CSP, Constraint
from colorama import Fore, Back, Style
from map.MapGen import MapGenerate
import numpy as np
from Tools import Position

# import numpy as np


map = Map(5,5)
map.Builder_Map()
vara = RandomCellForGenerate(map,400)
variables = ["lista1", "lista2", "lista3", "lista4", "lista5"]
domain : Dict[str,list[str]] = {}
monkey = Monkey(0,0)

map[0,0].animals.append(monkey)

for var in variables:
    domain[var] = {"water", "forest", "mountain", "meadow", "plain"}

csp: CSP[str, str] = CSP(variables,domain)

Create_Constraint_for_Map(variables,csp,0)



solution = csp.backtracking_search()

ConvertListCell_in_SolutionCell(solution,vara,map)

listOfCell = [] 
i=0
for lista in map.cell_List:
    listOfCell.append([])
    for cell in lista:
        listOfCell[i].append(cell)
    i+=1

for i in range(len(listOfCell)):
    for j in range(len(listOfCell[i])):
        if j==len(listOfCell[i])-1:
            if listOfCell[i][j].animals != None:
                print(listOfCell[i][j].animals[0].icon)
            if listOfCell[i][j].icon == "P":
                print(Fore.YELLOW,listOfCell[i][j].icon)
            elif listOfCell[i][j].icon == "W":
                print(Fore.BLUE,listOfCell[i][j].icon)
            elif listOfCell[i][j].icon == "M":
                print(Fore.MAGENTA,listOfCell[i][j].icon)
            elif listOfCell[i][j].icon == "F":
                print(Fore.RED,listOfCell[i][j].icon)
            elif listOfCell[i][j].icon == "H":
                print(Fore.GREEN,listOfCell[i][j].icon)
        else:
            if listOfCell[i][j].animals != None:
                print(listOfCell[i][j].animals[0].icon, end="")
            if listOfCell[i][j].icon == "P":
                print(Fore.YELLOW, listOfCell[i][j].icon, end="")
            elif listOfCell[i][j].icon == "W":
                print(Fore.BLUE, listOfCell[i][j].icon, end="")
            elif listOfCell[i][j].icon == "M":
                print(Fore.MAGENTA, listOfCell[i][j].icon, end="")
            elif listOfCell[i][j].icon == "F":
                print(Fore.RED, listOfCell[i][j].icon, end="")
            elif listOfCell[i][j].icon == "H":
                print(Fore.GREEN, listOfCell[i][j].icon, end="")


