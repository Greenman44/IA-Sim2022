import random
from Tools import Position
from numpy import sum

class Animal(object):
    def __init__(self, pos_x, pos_y):
        super(Animal,self).__setattr__("data",{"vision" : 3, "strength" : 1, "mobility" : 3, "stamina" : 3, "initial_stm" : 3})
        self.position = Position(pos_x,pos_y)
        self.icon = " A" # Icon to show in the map

    def get_perception(self, map):
        pass
    
    def random_move(self, moves, map):
        move = random.choice(list(moves.keys()))
        new_pos = Position(move[0], move[1])
        self.Move(map, new_pos, moves[move])
        

    def Move(self, map, new_pos, expen_stamina):
        index = map[self.position].animals.index(self)
        map[self.position].animals.pop(index)
        self.position = new_pos
        self.stamina -= expen_stamina - 1
        map[self.position].animals.append(self)
    
    def choose_action(self):
        actions = list(self.fcm.get_action_concepts())
        sum_actions = sum(actions)
        for i in range(len(actions)):
            actions[i] = actions[i] / sum_actions
        r = random.random()
        inf = 0
        sup = 1
        for i in range(len(actions)):
            if actions[i] > inf and actions[i] < r:
                inf = actions[i]
            if actions[i] < sup and actions[i] > r:
                sup = actions[i]
        try:
            return actions.index(inf)
        except:
            return 0


    
    def Interaction(self, map, pos):
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
        stamDict = {(self.position.x,self.position.y) : 0}
        distDict = {(self.position.x,self.position.y) : 0}
        self.ActionsSetDFS(map,self.position.x,self.position.y,stamDict,self.data["stamina"],self.data["mobility"],distDict,1)        
        return stamDict,distDict   
    
    def ActionsSetDFS(self, map, cx, cy, stamina,stam, mob,distances,cdistance):
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
                try:
                    if cdistance < distances[(nx,ny)]:
                        distances[(nx,ny)] = cdistance
                except:
                    distances[(nx,ny)] = cdistance
                self.ActionsSetDFS(map, nx,ny,stamina,cstam,mob + map[cx,cy].restrictions["mobility"],distances,cdistance + 1)