# from map.Map import Map
# from map.Cell import Cell
# from animals.Animal import Animal
# from animals.Predator import * 
# from animals.Prey import *


import numpy as np

a = np.array([3,1, 0])
b = np.array([[0,0,1], [0,0,-1], [0,0,0]])
b[0,0] = 1
print(np.argmax(a))
