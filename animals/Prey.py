from animals.Animal import *
from Tools import K_BFS_Vision
from .FCM_package.FCM_Prey import FCM_Prey
import numpy as np
class Prey(Animal):
    def __init__(self, posx, posy):
        super().__init__(posx, posy)
        self.fcm = FCM_Prey()
        self.strength = 2
        self.vision = 3
        self.mobility = 4
        self.initial_stm = 15
        self.stamina = 15
        self.meat_dropped = 20

    def get_perception(self, map):
        current_vision = (
            self.vision + map[self.position].restrictions["vision"]
        )
        cells_around = K_BFS_Vision(self.position.x, self.position.y, current_vision, map)
        self.close_pred, self.close_food = self.get_close_predFood(cells_around, map)
        local_food = map[self.position].food
        self._update_sens_concepts(
            self.close_pred[0][1] if len(self.close_pred) > 0 else 20,
            self.close_food[0][1] if len(self.close_food) > 0 else 20,
            local_food,
            map.get_max_food()[0]
        )

        for i in range(3):
            self.fcm.update_concepts()

    
    
    def make_action(self, action, map):
        actions = {
            0 : self.escape,
            1 : self.search_food,
            2 : self.explore,
            3 : self.wait,
            4 : self.eat
        }
        return actions[action](map)
    
    def escape(self,map):
        print("********************")
        print(f"{self} ESTOY ESCAPANDO")
        print("********************")
        moves_stamina, moves_distance = self.ActionsSet(map)
        if len(self.close_pred) == 0:
            self.random_move(moves_stamina, map)
            return
        average_x = 0
        average_y = 0
        for pred in self.close_pred:
            average_x += pred[0][0]
            average_y += pred[0][1]
        pos_average = (
            int(np.round(average_x/len(self.close_pred))), 
            int(np.round(average_y/len(self.close_pred)))
        )
        moves = self._get_farthest_pos(moves_distance , pos_average)
        moves_toMake = {i : moves_stamina[i] for i in moves}
        self.random_move(moves_toMake, map)

    def search_food(self,map):
        print("********************")
        print(f"{self} ESTOY BUSCANDO COMIDA")
        print("********************")
        moves_stamina, moves_distance = self.ActionsSet(map)
        for cell in self.close_food:
            if cell[0] in moves_stamina:
                self.Move(map, Position(cell[0][0], cell[0][1]), moves_stamina[cell[0]])
                return
        self.random_move(moves_stamina, map) 

    def explore(self,map):
        print("********************")
        print(f"{self} ESTOY EXPLORANDO")
        print("********************")
        moves, other = self.ActionsSet(map)
        moves.pop((self.position.x, self.position.y))
        self.random_move(moves, map)
    
    def wait(self,map):
        print("********************")
        print(f"{self} ESTOY ESPERANDO")
        print("********************")
        self.stamina -= 1
        if self.stamina < 0:
            self.drop_meat(map)

    def eat(self,map):
        food_need = self.initial_stm - self.stamina
        if map[self.position].food == 0:
            self.stamina-=1
            if self.stamina < 0:
                self.drop_meat(map)
            return
        food = map[self.position].food - food_need
        if food < 0:
            self.stamina += map[self.position].food
            map[self.position].food = 0
        else:
            self.stamina = self.initial_stm
        print("********************")
        print(f"{self} ESTOY COMIENDO: {self.stamina}")
        print("********************")


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
                1.5 * (self.initial_stm / sens["energy_low"][1])
            )
        )
        self.fcm.concepts[sens["energy_high"][0]] = self.fcm.fuzzy(
            self.stamina,
            (
                self.initial_stm / sens["energy_high"][1],
                1.5 * (self.initial_stm / sens["energy_high"][1])
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

    def _get_farthest_pos(self, moves_distance : dict, pos_average : tuple):
        result_moves = []
        max_distance = 0
        for cell in moves_distance.keys():
            pos = Position(cell[0], cell[1])
            distance = pos.get_distance(pos_average) 
            if distance > max_distance:
                max_distance = distance
                result_moves.clear()
                result_moves.append(cell)
            elif distance == max_distance:
                result_moves.append(cell)
        
        return result_moves
    
    def get_close_predFood(self, cells_around: dict, map):
        close_pred_distance_list = []
        close_pred_position_list = []
        close_food_distance_list = []
        close_food_position_list = []
        for cell in cells_around.keys():
            distance = self.position.get_distance(cell)
            if (
                map[cell].predator_in()
            ):
                close_pred_distance_list.append(distance)
                close_pred_position_list.append(cell)
            if cell != (self.position.x,self.position.y) and map[cell].food > 0:
                close_food_distance_list.append(distance)
                close_food_position_list.append(cell)

        return (
            list(zip(close_pred_position_list, close_pred_distance_list)), 
            list(zip(close_food_position_list, close_food_distance_list))
        )

    def Interaction(self, map, pos):
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
        
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()
