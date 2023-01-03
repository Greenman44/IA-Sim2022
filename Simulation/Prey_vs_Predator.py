from animals.Prey import Prey
from animals.Predator import Predator
from pandas import DataFrame

simulation = 0
def run(steps, map, participants):
    dictOfPlays = {}
    global simulation
    for i in range(len(participants)):
        dictOfPlays[i] = []
    step = 1
    preys = {i : {"stamina" : participants[i].stamina,
                    "steps": 0} for i in range(len(participants)) if type(participants[i]) is Prey}
    preds = {i : {"stamina" : participants[i].stamina,
                    "steps": 0} for i in range(len(preys), len(participants))}
    while step <= steps:
        for i in range(len(participants)):
            if(participants[i].stamina < 0):
                if(type(participants[i]) is Prey):
                    preys[i]["stamina"] = participants[i].stamina
                else:
                    preds[i]["stamina"] = participants[i].stamina
                dictOfPlays[i].append("0")
                continue
            participants[i].get_perception(map)
            action = participants[i].choose_action()
            participants[i].make_action(action, map)
            dictOfPlays[i].append(DFActions(action,participants[i]))
            if(type(participants[i]) is Prey):
                preys[i]["stamina"] = participants[i].stamina
                preys[i]["steps"] = step
            else:
                preds[i]["stamina"] = participants[i].stamina
                preds[i]["steps"] = step
        step+=1
    
    df = DataFrame(data=dictOfPlays)
    with open("Result_Of_Plays/simulation_" + str(simulation) + ".txt", "w")as file:
        file.write(df.to_string())
        file.close()
    simulation += 1
    return preys, preds

def DFActions(action, animal):
    if isinstance(animal,Prey) and action == 0:
        return "ESTOY ESCAPANDO " + str(animal)
    elif isinstance(animal, Predator) and action == 0:
        return "ESTOY ESCAPANDO " + str(animal)
    elif action == 1:
        return "ESTOY BUSCANDO COMIDA " + str(animal) 
    elif action == 2:
        return "ESTOY EXPLORANDO " + str(animal)
    elif action == 3:
        return "ESTOY ESPERANDO " + str(animal)
    elif action == 4:
        return "ESTOY COMIENDO " + str(animal)
