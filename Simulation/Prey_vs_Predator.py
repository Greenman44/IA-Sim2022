from animals.Prey import Prey
from animals.Predator import Predator
def run(steps, map, participants):
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
                continue
            
            participants[i].get_perception(map)
            action = participants[i].choose_action()
            participants[i].make_action(action, map)
            if(type(participants[i]) is Prey):
                preys[i]["stamina"] = participants[i].stamina
                preys[i]["steps"] = step
            else:
                preds[i]["stamina"] = participants[i].stamina
                preds[i]["steps"] = step
        step+=1
    return preys, preds    

            
