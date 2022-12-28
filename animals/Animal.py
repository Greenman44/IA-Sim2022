from map.Map import Map
from map.Cell import Cell
import random


class Animal(object):
    def __init__(self, pos_x, pos_y):
        super(Animal,self).__setattr__("data",{"vision" : 3, "strength" : 1, "mobility" : 2, "stamina" : 2, "initial_stm" : 2})
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.icon = "A" # Icon to show in the map

    def get_perception(self):
        pass
    
    def Move(self, map, play):
        self.Interaction(map, play)
        # map[play] = self.icon # The value of the currente animal to draw the map
        return map
    
    def Interaction(self, map: Map, pos):
        animal = map[pos].animal
        r = random.random()
        if animal != None:
            if animal.strength < self.strength: # This could be changed for a stocastic thing
                map[pos].animal = self
            elif animal.strength == self.strength:
                if r < 0.5:
                    map[pos].animal = self
        elif map[pos].food != 0:
            self.Recovery()
        else:
            map[pos] = self.icon

    def __setattr__(self, attr, value):
        self.data[attr]=value

    def __getattr__(self, attr):
        try:
            return self.data[attr]
        except KeyError:
            raise AttributeError

    def __getitem__(self, key):
        try:
            return self.__getattr__(key)
        except:
            raise KeyError


    def __setitem__(self, key, value):
        try:
            self.__setattr__(key, value)
        except:
            raise KeyError

    def Recovery(self):
        self.stamina += self.initial_stm - self.stamina





