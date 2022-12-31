# from map.Map import Map
# from map.Cell import Cell
# from animals.Animal import Animal
# from animals.Predator import * 
# from animals.Prey import *


from map.Map import Map
from map.Cell import Cell
from animals.Prey import Prey
from animals.Predator import Predator



matrix = [
    [Cell(food = 10), Cell(food= 10), Cell(food= 10), Cell(food= 10), Cell(food= 10)],
    [Cell(food = 10), Cell(food= 5), Cell(food= 5), Cell(food= 5), Cell(food= 10)],
    [Cell(food = 10), Cell(food= 5), Cell(food= 3), Cell(food= 5), Cell(food= 10)],
    [Cell(food = 10), Cell(food= 5), Cell(food= 5), Cell(food= 5), Cell(food= 10)],
    [Cell(food = 10), Cell(food= 10), Cell(food= 10), Cell(food= 10), Cell(food= 10)]
]


map = Map(5,5)
map.Builder_Map(map=matrix)

participants = [Prey(2,2), Predator(4,4)]
map[2,2].animals.append(participants[0])
map[4,4].animals.append(participants[1])

steps = 0
while steps < 2:
    for animal in participants:
        animal.get_perception(map)
        action = animal.choose_action()
        animal.make_action(action, map)

print(map)