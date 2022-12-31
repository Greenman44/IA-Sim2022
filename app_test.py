from map.Map import Map
from map.Cell import Cell
from animals.Animal import Animal
from animals.Predator import * 
from animals.Prey import *
from typing import Dict, List, Optional
from iAalgorithm.CSP_Map import *
from iAalgorithm.CSP import CSP, Constraint
from colorama import Fore, Back, Style


# import numpy as np

# a = np.array([3,1, 0])
# b = np.array([[0,0,1], [0,0,-1], [0,0,0]])
# b[0,0] = 1
# print(np.argmax(a))

map = Map(5,5)
map.Builder_Map()
vara = RandomCellForGenerate(map,5)
variables = ["lista1", "lista2", "lista3", "lista4", "lista5"]
domain : Dict[str,list[str]] = {}



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
        listOfCell[i].append(cell.icon)
    i+=1

for i in range(len(listOfCell)):
    for j in range(len(listOfCell[i])):
        if j==len(listOfCell[i])-1:
            if listOfCell[i][j] == "P":
                print(Fore.YELLOW,listOfCell[i][j])
            elif listOfCell[i][j] == "W":
                print(Fore.BLUE,listOfCell[i][j])
            elif listOfCell[i][j] == "M":
                print(Fore.MAGENTA,listOfCell[i][j])
            elif listOfCell[i][j] == "F":
                print(Fore.RED,listOfCell[i][j])
            elif listOfCell[i][j] == "H":
                print(Fore.GREEN,listOfCell[i][j])
            else:
                print(Fore.WHITE,""+listOfCell[i][j])
        else:
            if listOfCell[i][j] == "P":
                print(Fore.YELLOW, listOfCell[i][j], end="")
            elif listOfCell[i][j] == "W":
                print(Fore.BLUE, listOfCell[i][j], end="")
            elif listOfCell[i][j] == "M":
                print(Fore.MAGENTA, listOfCell[i][j], end="")
            elif listOfCell[i][j] == "F":
                print(Fore.RED, listOfCell[i][j], end="")
            elif listOfCell[i][j] == "H":
                print(Fore.GREEN, listOfCell[i][j], end="")
            else:
                print(Fore.WHITE,""+listOfCell[i][j], end="")

# Make a boolean mask for vara to create the kind of cells that the csp give us 


