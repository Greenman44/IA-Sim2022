from map.Map import Map
from map.Cell import Cell
import random


class Animal(object):
    def __init__(self, pos_x, pos_y):
        super(Animal,self).__setattr__("data",{"vision" : 3, "strength" : 1, "mobility" : 2, "stamina" : 2, "initial_stm" : 2})
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.icon = "A" # Icon to show in the map

    def get_perception(self, map):
        pass
    
    def Move(self, map, play):
        self.Interaction(map, play)
        # map[play] = self.icon # The value of the currente animal to draw the map
        return map
    
    def chose_action(self):
        actions = self.fcm.get_action_concepts()
        max = 0
        max_index = 0
        for i in range(len(actions)):
            change_action = False
            if actions[i] > max:
                change_action = True
            elif actions[i] == max:
                #TODO: decidir si cambiar de accion en base a una probabilidad
                pass
            if change_action:
                max = actions[i]
                max_index = i
        return max_index
    
    def Interaction(self, map: Map, pos):
        animal = map[pos].animal
        r = random.random()
        if animal != None:
            if animal.strength < self.strength: # This could be changed for a stocastic thing
                map[pos].animal = self
                map[pos].toString = self.icon
            elif animal.strength == self.strength:
                if r < 0.5:
                    map[pos].animal = self
                    map[pos].toString = self.icon
        elif map[pos].food != 0:
            map[pos].toString = self.icon
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


   

    def Recovery(self):
        self.stamina += self.initial_stm - self.stamina


    def ActionsSet(self,map):                
        stamDict = {(self.pos_x,self.pos_y) : 0}
        self.ActionsSetDFS(map,self.pos_x,self.pos_y,stamDict,self.data["stamina"],self.data["mobility"])        
        return stamDict   
    
    def ActionsSetDFS(self, map, cx, cy, stamina,stam, mob):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(len(dx)):
            son = None
            nx = cx + dx[i]
            ny = cy + dy[i]
            try:
                son = map[nx,ny]
            except:
                continue
            if (stam + map[cx,cy].restrictions["stamina"]) > 0 and (mob + map[cx,cy].restrictions["mobility"] ) >= 0 :
                cstam = stam + map[cx,cy].restrictions["stamina"]
                try:
                    if cstam < stamina[(nx,ny)]:
                        stamina[(nx,ny)] = cstam
                except: 
                    stamina[(nx,ny)] = cstam
                self.ActionsSetDFS(map, nx,ny,stamina,cstam,mob + map[cx,cy].restrictions["mobility"] )