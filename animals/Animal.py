import random
from Tools import Position
from numpy import sum

class Animal:
    def __init__(self, pos_x, pos_y):
        self.vision = 3 
        self.strength = 1 
        self.mobility = 3
        self.stamina = 3
        self.initial_stm = 3
        self.position = Position(pos_x,pos_y)
        self.icon = " A" # Icon to show in the map

    def get_perception(self, map):
        pass

    def drop_meat(self, map):
        map[self.position].food += self.meat_dropped if (map[self.position].food + self.meat_dropped) <= map.get_max_food()[0] else map.get_max_food()[0] - self.meat_dropped 


    def random_move(self, moves, map):
        if len(moves) == 0:
            # print("********************")
            # print(f"{self} NO PUDE MOVERME")
            # print("********************")
            self.stamina -= 1
            if self.stamina < 0:
                self.drop_meat(map)
            return
        move = random.choice(list(moves.keys()))
        new_pos = Position(move[0], move[1])
        self.Move(map, new_pos, moves[move])
        
    def _get_farthest_pos(self, moves_distance : dict, pos_average : tuple):
        pass

    def Move(self, map, new_pos, expen_stamina):
        # print("********************")
        # print(f"{self} ESTOY MOVIENDOME A LA CASILLA: ({new_pos.x}, {new_pos.y})")
        # print("********************")
        index = map[self.position].animals.index(self)
        map[self.position].animals.pop(index)
        self.position = new_pos
        self.stamina = expen_stamina - 1
        if self.stamina < 0:
            self.drop_meat(map)
            return
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
        if sup == 1:
            return actions.index(inf)
        if inf == 0:
            return 0
        
        return actions.index(sup)

    
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


    def __getitem__(self, key):
        try:
            return self.__getattr__(key)
        except:
            raise KeyError

    def __str__(self) -> str:
        return type(self).__name__ + " " + str((self.position.x,self.position.y))
   

    def Recovery(self):
        self.stamina += self.initial_stm - self.stamina


    def ActionsSet(self,map):                
        stamDict = {(self.position.x,self.position.y) : 0}
        distDict = {(self.position.x,self.position.y) : 0}
        self.ActionsSetDFS(map,self.position.x,self.position.y,stamDict,self.stamina,self.mobility,distDict,1)        
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