from map.Map import Map
from map.Cell import Cell
from animals.Animal import Animal
from animals.Predator import * 
from animals.Prey import *
from Tools import K_BFS

map = Map(5,5)
map.Builder_Map()
an = Animal(2,4)
print(an.ActionsSet(map))

