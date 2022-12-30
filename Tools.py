

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

                

