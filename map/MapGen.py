from map.Cell import Cell, ForestCell, WaterCell, PlainCell, MeadowCell, MountainCell
import numpy as np
import random

class MapGenerate :
    def __init__(self, numRows, numCols, cellTypes = [ForestCell, WaterCell, PlainCell,MeadowCell, MountainCell]):
        self.numRows = numRows
        self.numCols = numCols
        self.cellTypes = cellTypes
    

    def generate(self):
        dx = [1,-1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
        tmap = [[0 for i in range(self.numCols)] for i in range(self.numRows)]
        for i in range(self.numRows):
            for j in range(self.numCols):
                numTypes = [0 for i in range(len(self.cellTypes))]
                for k in range(len(dx)):
                    if self.correctIndex(i,j, i + dx[k], j + dy[k]):
                        if(tmap[i + dx[k]][j + dy[k]] != 0):
                           ct = self.cellTypes.index(type(tmap[i + dx[k]][ j + dy[k]]))
                           numTypes[ct] += 1
                toTake = [i for i in self.cellTypes]
                for z in range(len(self.cellTypes)):
                    for x in  range(int(numTypes[z])):
                        toTake.append(self.cellTypes[z])
                tmap[i][j] = random.choice(toTake)()
        return tmap          

    def correctIndex(self, x, y, dx, dy):
        return 0 <= x + dx < self.numRows and 0 <= y + dy < self.numCols