from animals.Animal import *
from Tools import K_BFS_Vision
from .FCM_package.FCM_Predator import FCM_Predator
import random
class Predator(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.vision = 7
        self.mobility = 5
        self.initial_stm = 7
        self.stamina = 7
        self.fcm = FCM_Predator() 
    
    def get_perception(self, map):
        current_vision = (
            self.vision + map[self.pos_x, self.pos_y].restrictions["vision"]
        )
        cells_around = K_BFS_Vision(self.pos_x, self.pos_y, current_vision, map)
        close_pred, close_food = self.get_close_preyFood(cells_around, map)
        local_food = map[self.pos_x, self.pos_y].pred_food
        self.update_sens_concepts(close_pred, close_food, local_food, map.get_max_food()[0])
        for i in range(3):
            self.fcm.update_concepts()
        print(self.fcm.concepts)

    def get_close_preyFood(self, cells_around: dict, map):
        close_pred_distance = 10
        close_food_distance = 10
        for cell in cells_around.keys():
            distance = abs(self.pos_x - cell[0]) + abs(self.pos_y - cell[1])
            if (
                map[cell].predator_in()
                and  distance < close_pred_distance
            ):
                close_pred_distance = distance
            if cell != (self.pos_x,self.pos_y) and map[cell].food > 0 and distance < close_food_distance:
                close_food_distance = distance

        if map[self.pos_x, self.pos_y].prey_in():
            close_pred_distance = 0
        return close_pred_distance, close_food_distance

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
        moves, other = self.ActionsSet(map)
        move = random.choice(list(moves.keys()))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        self.stamina -= moves[move] - 1
        map[move[0],move[1]].animals.append(self)

    def Interaction(self, map, pos):
        animals = map[pos].animals
        if animals != None:
            self.Combat(animals, map, pos)

    def Combat(self, animals, map, pos):
        # TODO: Make a best stocastic combat with strength and another prop
        new_animal=set()
        new_icon=[]
        for animal in animals:
            r = random.random()
            if r > 0.5:
                new_animal.add(self)
                new_icon.append(self.icon)
                if len(new_icon)!=len(new_animal):
                    new_icon.remove(self.icon)
            else:
                new_animal.add(animal)
                new_icon.append(animal.icon)
                new_animal.add(self)
                new_icon.append(self.icon)
                if len(new_icon) != len(new_animal):
                    new_icon.remove(self.icon)
                    
        map[pos].animals = new_animal
        map[pos].icon = new_icon

    
    def search_food(self,map):
        moves, other = self.ActionsSet(map)
        move = random.choice(list(moves.keys()))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        self.stamina -= moves[move] - 1
        map[move[0],move[1]].animals.append(self)   
        

    def explore(self,map):
        moves, other = self.ActionsSet(map)
        move = random.choice(list(moves.keys()))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        self.stamina -= moves[move] - 1
        map[move[0],move[1]].animals.append(self)   
    
    def wait(self,map):
        moves, other = self.ActionsSet(map)
        move = random.choice(list(moves.keys()))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        self.stamina -= moves[move] - 1
        map[move[0],move[1]].animals.append(self)   

    def eat(self,map):
        moves, other = self.ActionsSet(map)
        move = random.choice(list(moves.keys()))
        index = map[self.pos_x,self.pos_y].animals.index(self)
        map[self.pos_x,self.pos_y].animals.pop(index)
        self.pos_x = move[0]
        self.pos_y = move[1]
        self.stamina -= moves[move] - 1
        map[move[0],move[1]].animals.append(self)

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
