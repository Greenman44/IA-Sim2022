from animals.Animal import *
from Tools import K_BFS_Vision
from .FCM_package.FCM_Prey import FCM_Prey

class Prey(Animal):
    def __init__(self, posx, posy):
        super().__init__(posx, posy)
        self.fcm = FCM_Prey()
        self.vision = 4

    def get_perception(self, map):
        current_vision = (
            self.vision + map[self.pos_x, self.pos_y].restrictions["vision"]
        )
        cells_around = K_BFS_Vision(self.pos_x, self.pos_y, current_vision)
        close_pred, close_food = self.get_close_predFood(cells_around, map)
        local_food = map[self.pos_x, self.pos_y].food
        self._update_sens_concepts(close_pred, close_food, local_food, map.get_max_food()[0])
        for i in range(3):
            self.fcm.update_concepts()
    
    

    def make_action(self, action):
        actions = {
            0 : self.escape(),
            1 : self.search_food(),
            2 : self.explore(),
            3 : self.wait(),
            4 : self.eat()
        }
        return actions[action]
    
    def escape(self,map):
        move = random.choice(self.ActionsSet(map))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        map[move[0],move[1]].animals.append(self)
    
    def search_food(self,map):
        move = random.choice(self.ActionsSet(map))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        map[move[0],move[1]].animals.append(self)

    def explore(self,map):
        move = random.choice(self.ActionsSet(map))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        map[move[0],move[1]].animals.append(self)
    
    def wait(self,map):
        move = random.choice(self.ActionsSet(map))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        map[move[0],move[1]].animals.append(self)

    def eat(self,map):
        move = random.choice(self.ActionsSet(map))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        map[move[0],move[1]].animals.append(self)

    def _update_sens_concepts(self, close_pred, close_food, local_food, max_food):
        sens = self.fcm._sens_index_params
        # pred
        self.fcm.concepts[sens["pred_close"][0]] = self.fcm.fuzzy(
            close_pred,
            (
                self.vision / sens["pred_close"][1],
                2 * (self.vision / sens["pred_close"][1])
            )
        )
        self.fcm.concepts[sens["pred_far"][0]] = self.fcm.fuzzy(
            close_pred,
            (
                self.vision / sens["pred_close"][1],
                2 * (self.vision / sens["pred_close"][1])
            ),
            inv=True,
        )
        #food
        self.fcm.concepts[sens["food_close"][0]] = self.fcm.fuzzy(
            close_food,
            (
                self.vision / sens["food_close"][1],
                2 * (self.vision / sens["food_close"][1])
            )
        )
        self.fcm.concepts[sens["food_far"][0]] = self.fcm.fuzzy(
            close_food,
            (
                self.vision / sens["food_far"][1],
                2 * (self.vision / sens["food_far"][1])
            ),
            inv=True
        )
        #Energy
        self.fcm.concepts[sens["energy_low"][0]] = self.fcm.fuzzy(
            self.stamina,
            (
                self.initial_stm / sens["energy_low"][1],
                2 * (self.initial_stm / sens["energy_low"][1])
            )
        )
        self.fcm.concepts[sens["energy_high"][0]] = self.fcm.fuzzy(
            self.stamina,
            (
                self.initial_stm / sens["energy_high"][1],
                2 * (self.initial_stm / sens["energy_high"][1])
            ),
            inv = True
        )
        #Local_food
        self.fcm.concepts[sens["food_local_high"][0]] = self.fcm.fuzzy(
            local_food,
            (
                max_food / sens["food_local_high"][1],
                2 * (max_food/ sens["food_local_high"][1])
            ),
            inv = True
        )
        self.fcm.concepts[sens["food_local_low"][0]] = self.fcm.fuzzy(
            local_food,
            (
                max_food / sens["food_local_low"][1],
                2 * (max_food/ sens["food_local_low"][1])
            )
        )

    

    def get_close_predFood(self, cells_around: dict, map):
        close_pred_distance = 10
        close_food_distance = 10
        for cell in cells_around.keys():
            if (
                map[self.pos_x, self.pos_y].predator_in()
                and cells_around[cell] < close_pred_distance
            ):
                close_pred_distance = cells_around[cell]
            if map[cell].food > 0 and close_food_distance < close_food_distance:
                close_food_distance = cells_around[cell]

        if map[self.pos_x, self.pos_y].predator_in():
            close_pred_distance = 0
        return close_pred_distance, close_food_distance

    def Move(self, map, play):
        return super().Move(map, play)
    def Interaction(self, map: Map, pos):
        map[pos].animals.add(self)
        if map[pos].food != 0:
            self.Recovery()
        map[pos].icon.append(self.icon)

    def Recovery(self):
        return super().Recovery()


class Deer(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " D"
        self.mobility = 7
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 9
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Hare(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " H"
        self.mobility = 6
        self.stamina = 4
        self.initial_stm = 4
        self.vision = 4
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Zebra(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " Z"
        self.mobility = 4
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 5
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Monkey(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " M"
        self.mobility = 4
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 6
        map[posx,posy].icon.append(self.icon)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()
