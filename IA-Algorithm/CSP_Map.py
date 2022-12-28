from map.Map import Map
from map.Cell import *
from CSP import Constraint, CSP
from typing import Dict, List, Optional




class MapConstraint(Constraint[Cell,Cell]):
    def __init__(self, cell1 : Cell, cell2 : Cell) -> None:
        super().__init__([cell1, cell2])
        self.cell1 = cell1
        self.cell2 = cell2
    
    def satisfied(self, assignment: Dict[Cell, str]) -> bool:
        # TODO: This
        pass

variables = map.cell_List 
domain = Dict[Cell,list[str]]

for var in variables:
    domain[var] = {"water", "forest", "mountain", "meadow", "plain"}

# TODO: Establish the restrictions that the map have to satisfy as is show in the next line:
# csp: CSP[Cell, str] = CSP(variables, domain)
# csp.add_constraint(MapConstraint(Cell,Cell)) 