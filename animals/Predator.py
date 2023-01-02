from animals.Animal import *
from Tools import K_BFS_Vision
from .FCM_package.FCM_Predator import FCM_Predator
from animals.Prey import Prey

import random
class Predator(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.vision = 7
        self.mobility = 6
        self.initial_stm = 15
        self.stamina = 15
        self.fcm = FCM_Predator() 
    
    def get_perception(self, map):
        current_vision = (
            self.vision + map[self.pos_x, self.pos_y].restrictions["vision"]
        )
        cells_around = K_BFS_Vision(self.pos_x, self.pos_y, current_vision, map)
        self.close_prey, self.close_food = self.get_close_preyFood(cells_around, map)
        local_food = map[self.position].pred_food
        self.update_sens_concepts(self.close_prey[0][1], self.close_food[0][1], local_food, map.get_max_food()[0])
        for i in range(3):
            self.fcm.update_concepts()
        print(self.fcm.concepts)

    def get_close_preyFood(self, cells_around: dict, map):
        close_prey_distance_list = []
        close_prey_position_list = []
        close_food_distance_list = []
        close_food_position_list = []
        for cell in cells_around.keys():
            distance = self.position.get_distance(cell)
            if (
                map[cell].prey_in()
            ):
                close_prey_distance_list.append(distance)
                close_prey_position_list.append(cell)
            if cell != (self.position.x,self.position.y) and map[cell].pred_food > 0:
                close_food_distance_list.append(distance)
                close_food_position_list.append(cell)

        return (
            list(zip(close_prey_position_list, close_prey_distance_list)), 
            list(zip(close_food_position_list, close_food_distance_list))
        )

    def make_action(self, action,map):
        actions = {
            0 : self.hunt,
            1 : self.search_food,
            2 : self.explore,
            3 : self.wait,
            4 : self.eat
        }
        return actions[action](map)

    #TODO: action methods
    def hunt(self,map):
        if(self.close_prey[0][1] == 0): #current cell have a prey
            current_preys = [prey for prey in map[self.position] if type(prey) is Prey]
            self.fight(random.choice(current_preys), map)
            return
        moves_stamina, moves_distance = self.ActionsSet(map)
        for prey in self.close_prey:
            if prey[0] in moves_stamina:
                self.Move(map, prey, moves_stamina[prey])
                return
        self.random_move(moves_stamina, map)

    def fight(self, prey, map):
        norm_opponentStrength = prey.strength / (self.strength + prey.strength)
        r = random.random()
        
        if r > norm_opponentStrength:
            prey.stamina = -1
            prey_index = map[self.position].animals.index(prey)
            map[self.position].animals.pop(prey_index)
            map[self.position].pred_food += prey.meat_dropped

        self.stamina -= prey.strength
            
    def search_food(self,map):
        moves_stamina, moves_distance = self.ActionsSet(map)
        for cell in self.close_food:
            if cell[0] in moves_stamina:
                self.Move(map, cell[0], moves_stamina[cell[0]])
                return
        self.random_move(moves_stamina, map)    
        

    def explore(self,map):
        moves, other = self.ActionsSet(map)
        self.random_move(moves, map)
    
    def wait(self,map):
        self.stamina -= 1   

    def eat(self,map):
        food_need = self.initial_stm - self.stamina
        map[self.position].pred_food -= food_need
        if map[self.position].pred_food < 0:
            self.stamina = self.initial_stm + map[self.position].pred_food
            map[self.position].pred_food = 0
        else:
            self.stamina = self.initial_stm

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

    
    def Recovery(self):
        return super().Recovery()

class Lion(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " L"
        self.strength = 3
        self.mobility = 5
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 6
        map[posx,posy].icon.append(self.icon)

    def Interaction(self, map, pos):
        return super().Interaction(map, pos)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Wolf(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " W"
        self.strength = 2
        self.mobility = 8
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 8
        map[posx,posy].icon.append(self.icon)

    def Interaction(self, map, pos):
        return super().Interaction(map, pos)
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Tiger(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.icon = " T"
        self.strength = 3
        self.mobility = 5
        self.stamina = 7
        self.vision = 8
        self.initial_stm = 7
        map[posx,posy].icon.append(self.icon)

    def Interaction(self, map, pos):
        return super().Interaction(map, pos)
    def Move(self, map, play):
        return super().Move(map, play)
    def Recovery(self):
        return super().Recovery()
