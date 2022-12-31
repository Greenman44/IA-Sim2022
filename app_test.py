from map.Map import Map
from map.Cell import Cell
from animals.Animal import Animal
from animals.Predator import * 
from animals.Prey import *
from typing import Dict, List, Optional
from iAalgorithm.CSP_Map import *
from iAalgorithm.CSP import CSP, Constraint


# import numpy as np

# a = np.array([3,1, 0])
# b = np.array([[0,0,1], [0,0,-1], [0,0,0]])
# b[0,0] = 1
# print(np.argmax(a))

map = Map(6,6)
map.Builder_Map()
vara = RandomCellForGenerate(map,1)
variables = ["lista1", "lista2", "lista3", "lista4", "lista5"]
domain : Dict[str,list[str]] ={}


for var in variables:
    domain[var] = {"water", "forest", "mountain", "meadow", "plain"}

csp: CSP[str, str] = CSP(variables,domain)

Create_Constraint_for_Map(variables,csp,0)



solution = csp.backtracking_search()

ConvertListCell_in_SolutionCell(solution,vara,map)

listOfCell = [] 

for lista in map.cell_List:
    for cell in lista:
        listOfCell.append(cell.typeOfCell)

print(listOfCell)

# Make a boolean mask for vara to create the kind of cells that the csp give us 


