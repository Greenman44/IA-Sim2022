from map.Map import Map
from Tools import K_BFS

map = Map(5,5)
map.Builder_Map()

print(K_BFS(2, 2, 2, map))
