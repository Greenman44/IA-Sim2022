from map.Map import Map
from iAalgorithm.CSP import CSP
from iAalgorithm.CSP_Map import *

def gen_map(rows, columns, preys_amount, preds_amount, max_prey_food, max_pred_food):
    map = Map(rows, columns, max_prey_food, max_pred_food)

    vara = RandomCellForGenerate(map,int((rows*columns)/3))
    variables = ["lista1", "lista2", "lista3", "lista4", "lista5"]
    domain : Dict[str,list[str]] = {}


    for var in variables:
        domain[var] = {"water", "forest", "mountain", "meadow", "plain"}

    csp: CSP[str, str] = CSP(variables,domain)

    Create_Constraint_for_Map(variables,csp,0)
    solution = csp.backtracking_search()
    ConvertListCell_in_SolutionCell(solution,vara,map)
    map.SetGrassDistribution()
    participants = map.SetAnimalDistribution(preys_amount, preds_amount)
    return map, participants