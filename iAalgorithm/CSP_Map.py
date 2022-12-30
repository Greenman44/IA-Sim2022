from map.Cell import *
from .CSP import Constraint, CSP
from typing import Dict, List, Optional
from random import randint, random
from Tools import *



# TODO: Untested
class MapConstraint(Constraint[str,str]):
    def __init__(self, string1: str, string2:str) -> None:
        super().__init__([string1,string2])
        self.cell_list1 = string1
        self.cell_list2 = string2
    
    def satisfied(self, assignment: Dict[str,str]) -> bool:
        if self.cell_list1 not in assignment or self.cell_list2 not in assignment:
            return True
        
        return assignment[self.cell_list1] != assignment[self.cell_list2]

def RandomCellForGenerate(map, amountofCells:int):
        temp: tuple(int,int)
        randomCells = [[]]
        listOfConstraintCells = []
        for i in range(4):
            posRow = randint(0,len(map.cell_List)-1)
            posCol = randint(0,len(map.cell_List[0])-1)
            restricCell = K_BFS_Vision(posRow,posCol,amountofCells,map)
            for pos in restricCell.keys():
                listOfConstraintCells.append(map[int(pos[0]),int(pos[1])])
            randomCells.append(listOfConstraintCells)
            listOfConstraintCells.clear()
            i += 1
        return randomCells

def Create_Constraint_for_Map(cellsConstr, csp: CSP, i:int):
    j = i + 1
    k=1
    if i == len(cellsConstr):
        return
    while k != len(cellsConstr):
        try:
            csp.add_constraint(MapConstraint(cellsConstr[i],cellsConstr[i+k]))
            k+=1
        except:
            k+=1
    return Create_Constraint_for_Map(cellsConstr,csp, j)


# class GeneratorConstraint:
#     def __init__(self, map: Map):
#         self.map = map
#         self.randomCells: set = [tuple(int,int)]
    
#     def SelectCellForGenerate(self, map: Map):
#         temp: tuple(int,int)
#         listOfConstraintCells = []
#         for i in range(5):
#             temp = (randint(0,len(map.cell_List)),randint(0,len(map.cell_List[0])))
#             self.randomCells.add()
#             restricCell = K_BFS_Vision(temp[0],temp[1],1,map)
#             self.map.cell_List.remove(restricCell.keys)
#             listOfConstraintCells.append(restricCell.keys)
        
#         return restricCell


