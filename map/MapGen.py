from map.Cell import Cell, ForestCell, WaterCell, PlainCell, MeadowCell, MountainCell
import numpy as np
import random

class MapGenerate :
    def __init__(self, map, cellTypes = [ForestCell, WaterCell, PlainCell,MeadowCell, MountainCell]):
        self.map = map
        self.numRows = len(map)
        self.numCols = len(map[0])
        self.cellTypes = cellTypes
    

    def generate(self):
        dx = [1,-1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
       
        for i in range(self.numRows):
            for j in range(self.numCols):
                numTypes = [0 for i in range(len(self.cellTypes))]
                if self.map[i][j].typeOfCell == "cell":   
                    for k in range(len(dx)):
                        if self.correctIndex(i,j, i + dx[k], j + dy[k]):
                                if(type(self.map[i + dx[k]][j + dy[k]]) != Cell):
                                    ct = self.cellTypes.index(type(self.map[i + dx[k]][ j + dy[k]]))
                                    numTypes[ct] += 1
                            
                    toTake = [i for i in self.cellTypes]
                    for z in range(len(self.cellTypes)):
                        for x in  range(int(numTypes[z])):
                            toTake.append(self.cellTypes[z])
                    self.map[i][j] = random.choice(toTake)()
        return self.map          

    def correctIndex(self, x, y, dx, dy):
        return 0 <= x + dx < self.numRows and 0 <= y + dy < self.numCols