from map.Map import Map
from map.Cell import Cell
from animals.Animal import Animal
from animals.Predator import * 
from animals.Prey import *
from Tools import K_BFS

map = Map(5,5)
map.Builder_Map()

print(K_BFS(2,2, 4, map))

monkey = Monkey(2,2)
tiger = Tiger(2,1)

map[2,1].animal = tiger
map[2,2].animal = monkey

tiger.Move(map,(2,2))


print(map[2,2].animal)

