from Generators.Map_Generator import gen_map
from Simulation.Prey_vs_Predator import run
# import numpy as np

map, participants = gen_map(50,50,200,20,30,30)
map.pretty_self()
print("***********************************")
preys, preds = run(20,map, participants)
print("PREYS*****************")
print(preys)
print("*********************************")
print("PREDS*****************")
print(preds)






