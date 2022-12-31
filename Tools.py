from random import randint, random

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

            
            


                

