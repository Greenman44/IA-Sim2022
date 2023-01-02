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


map = Map(10,10)

vara = RandomCellForGenerate(map,20)
variables = ["lista1", "lista2", "lista3", "lista4", "lista5"]
domain : Dict[str,list[str]] = {}


for var in variables:
    domain[var] = {"water", "forest", "mountain", "meadow", "plain"}

csp: CSP[str, str] = CSP(variables,domain)

Create_Constraint_for_Map(variables,csp,0)



solution = csp.backtracking_search()

ConvertListCell_in_SolutionCell(solution,vara,map)
map.pretty_self()








