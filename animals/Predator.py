from animals.Animal import *
from Tools import K_BFS_Vision
from .FCM_package.FCM_Predator import FCM_Predator

class Predator(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.vision = 8
        self.fcm = FCM_Predator() 
    
    def get_perception(self, map):
        current_vision = (
            self.vision + map[self.pos_x, self.pos_y].restrictions["vision"]
        )
        cells_around = K_BFS_Vision(self.pos_x, self.pos_y, current_vision)
        close_pred, close_food = self.get_close_predFood(cells_around, map)
        local_food = map[self.pos_x, self.pos_y].pred_food
        self.update_sens_concepts(close_pred, close_food, local_food, map.get_max_food()[0])
        for i in range(3):
            self.fcm.update_concepts()


    def make_action(self, action):
        actions = {
            0 : self.hunt(),
            1 : self.search_food(),
            2 : self.explore(),
            3 : self.wait(),
            4 : self.eat()
        }
        return actions[action]
    #TODO: action methods
    def hunt(self):
        pass
    
    def search_food(self):
        pass

    def explore(self):
        pass
    
    def wait(self):
        pass

    def eat(self):
        pass

    def update_sens_concepts(self, close_pred, close_food, local_food, max_food):
        sens = self.fcm._sens_index_params
        # pred
        self.fcm.concepts[sens["prey_close"][0]] = self.fcm.fuzzy(
            close_pred,
            (
                self.vision / sens["prey_close"][1],
                2 * (self.vision / sens["prey_close"][1])
            )
        )
        self.fcm.concepts[sens["prey_far"][0]] = self.fcm.fuzzy(
            close_pred,
            (
                self.vision / sens["prey_close"][1],
                2 * (self.vision / sens["prey_close"][1])
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
    
    def Move(self,map,play):
        return super().Move(map,play)
    
    def Recovery(self):
        return super().Recovery()

class Lion(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.strength = 3
        self.mobility = 5
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 6
        self.icon = "L"
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Wolf(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.strength = 2
        self.mobility = 8
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 8
        self.icon = "W"
    def Move(self,map,play):
        return super().Move(map,play)

    def Recovery(self):
        return super().Recovery()

class Tiger(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.strength = 3
        self.mobility = 5
        self.stamina = 7
        self.initial_stm = 7
        self.icon = "T"
    def Move(self, map, play):
        return super().Move(map, play)
    def Recovery(self):
        return super().Recovery()
