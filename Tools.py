<<<<<<< Updated upstream
from random import randint, random
from  typing import Tuple
=======
from random import randint, next

>>>>>>> Stashed changes
def K_BFS_Vision(init_x, init_y, k, map):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    queue = [(init_x, init_y)]
    distance = {
        (init_x, init_y) : 0
    }
    
    while len(queue) > 0:
        current_pos = queue.pop(0)
        for i in range(len(dx)):
            new_pos = (current_pos[0] + dx[i], current_pos[1] + dy[i])
            try:
               cell = map[new_pos]
            except IndexError:
                continue
            current_distance = distance[current_pos] + 1
            if current_distance > k: 
                break
            if not new_pos in distance.keys():
                distance[new_pos] = current_distance
                queue.append(new_pos)
    
    return distance

def DFS_Rare_For_Generate_Cells(init_x, init_y, k, map):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    queue = [(init_x, init_y)]
    way = {(init_x,init_y):0}

    param = k

    while len(queue) > 0:
        current_pos = queue.pop(0)
        if param==0:
            break
        for i in range(3):
            new_pos = (current_pos[0] + dx[randint(0,len(dx)-1)], current_pos[1] + dy[randint(0,len(dy)-1)])
            try:
                cell = map[new_pos]
            except IndexError:
                continue
            if not new_pos in way.keys():
                queue.append(new_pos)
                way[new_pos] = 0
        param-=1
    
    return way

<<<<<<< Updated upstream
class Position:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

    def get_distance(self, pos):
        diff_x = abs(self.x - pos[0])
        diff_y = abs(self.y - pos[1])
        return diff_x + diff_y            

    def get_direction(self, pos):
        diff_x = pos[0] - self.x
        diff_y = pos[1] - self.y
        dir_x = diff_x/abs(diff_x) if diff_x != 0 else 0
        dir_y = diff_y/abs(diff_y) if diff_y != 0 else 0
        return int(dir_x), int(dir_y)
=======
            
def AnimalDistribution(map,numPreys, numPredators):
    numCols = len(map[0])
    numRows = len(map) 
    for i in range(numPreys):
        x = randint(0,numRows - 1)
        y = randint(0,numCols - 1)       
        map[x][y] = "AQUI SE CREA LA PRESA"
    
    for i in range(numPredators):
        x = randint(0, numRows - 1)
        y = randint(0, numCols - 1)
        map[x][y] = "AQUI SE CREA EL DEPREDADOR"

                
def GrassDistribution(map ,grassprob = 18, maxgrass = 20):
    for i in len(map):
        for j in range(len(map[0])):
            prob = next(0,(len(map) * next(0,len(map))) /(len(map) * next(0,len(map)) ))
            if prob > grassprob:
                map[i][j] += next(0,maxgrass)
>>>>>>> Stashed changes
