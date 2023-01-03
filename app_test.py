from generators.Map_Generator import gen_map
from Simulation.Prey_vs_Predator import *
from iAalgorithm.SimulatedAnnealing import SimulatedAnnealingEcoSystem
# import numpy as np

map = gen_map(15,15,10,4,30,30)
# map.pretty_self()
# print("***********************************")
# preys, preds = run(20,map, participants)
# print("PREYS*****************")
# print(preys)
# print("*********************************")
# print("PREDS*****************")
# print(preds)

map.pretty_self()

sim = SimulatedAnnealingEcoSystem(map, map.participants[len(map.participants)- 1].fcm.causal_graph, n_iterations=20, sim_steps=10)
sim.run()







