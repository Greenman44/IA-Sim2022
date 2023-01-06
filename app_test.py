from Generators.Map_Generator import gen_map
from Simulation.Prey_vs_Predator import *
from iAalgorithm.SimulatedAnnealing import SimulatedAnnealingEcoSystem
from os import getcwd, mkdir

#create folder to store results
try:
    mkdir(getcwd() + "/Result_Of_Plays")
except:
    pass 


#change parameters to generate other map
map = gen_map(15,15, preys_amount= 10,preds_amount=4,max_pred_food=30, max_prey_food=30)

map.pretty_self()

#change n_iterations and sim_steps to see other result
sim = SimulatedAnnealingEcoSystem(map, map.participants[len(map.participants)- 1].fcm.causal_graph, n_iterations=30, sim_steps=10)
sim.run()







