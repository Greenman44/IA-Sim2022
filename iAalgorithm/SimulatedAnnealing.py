import random
import math
import copy
from Simulation.Prey_vs_Predator import run
from pandas import DataFrame
class SimulatedAnnealingEcoSystem(object):

    def __init__(self,map, vectorizedFCM, n_iterations = 30,sim_steps = 20, a = 0.99, t_0= 10**9):
        self.distances  = vectorizedFCM
        self.n_iterations = n_iterations
        self.sim_steps = sim_steps
        self.map = map
        self.a = a
        self.t_0 = t_0
        self.Cscore = -1
        self.Nscore = -1
        self.iteration = 0
        
    def run(self):
        current_path = self.distances
        all_time_shortest_path = (-1, "placeholder", -1)
        t = self.t_0
        currentMap = copy.deepcopy(self.map)
        self.Cscore = self.path_dist(currentMap,current_path)
        dictOfScore = {}
        for i in range(self.n_iterations):
            dictOfScore[i] = []
        for i in range(self.n_iterations):
            self.iteration = i
            currentMap = copy.deepcopy(self.map)
            next_path = self.succesor(current_path)
            self.Nscore = self.path_dist(currentMap,next_path)
            # print(next_path)
            
            if self.Cscore > all_time_shortest_path[2]:
                all_time_shortest_path = (i, current_path ,self.Cscore)  
            
            if self.acceptance_probability(self.Cscore, self.Nscore, t) >= random.random():
                current_path = next_path
                self.Cscore = self.Nscore
                
            t = self.temperature(t)
            
            dictOfScore[i].append(self.Cscore)
            dictOfScore[i].append(all_time_shortest_path[2])

            df = DataFrame(all_time_shortest_path[1])
            with open("Result_Of_Plays/simulation_" + str(i) + ".txt", "a") as file:
                file.write("\n"+df.to_string())
                file.close()
            # print("ITERACION*******************************")
            # print(i)
            # print("BEST SOLUTION**********************************")
            # print(all_time_shortest_path[1])
            # print("SCORE*******************************")
            # print(self.Cscore, all_time_shortest_path[2])
        df = DataFrame(data=dictOfScore)
        with open("Result_Of_Plays/Simulated_Annealing.txt", "w")as file:
            file.write(df.to_string())
            file.close()
        return all_time_shortest_path
    
    def path_dist(self, currentMap,nextVec):
        parts = currentMap.participants
        parts[len(parts) - 1].fcm.causal_graph = nextVec
        preys,predator = run(self.sim_steps,currentMap,parts)

        return predator[len(parts) - 1]["steps"] + predator[len(parts) - 1]["stamina"]

    def temperature(self, t):
        
        return t * self.a

                         
    def acceptance_probability(self, current_dist, next_dist, temp):
         if next_dist > current_dist:
            return 1.0
         return math.exp((next_dist-current_dist)/temp)
    
    def succesor(self, path):
        for i in range(4):
            j = random.randint(0,7)
            k = random.randint(0,3)
            path[j,k] = random.uniform(path[j,k] - 2, path[j,k] + 2)
        for i in range(4):
            j = random.randint(7,11)
            k = random.randint(4,8)
            path[j,k] = random.uniform(path[j,k] - 2, path[j,k] + 2)
        return path