import numpy as np
import random
from classes import recipe
import main
import limits

def neighborhood(current_solution : list[recipe], amount:int = 100):
    neighborhood = []

    for _ in range(amount):
        index_of_recipe = random.randint(0,20)
        neighbor = random.sample(current_solution,index_of_recipe)
        while 1:
            recipes = random.sample(main.recipe_database,21 - index_of_recipe)
            new_neighbor = neighbor + recipes
            
            if limits.acceptabiliy(new_neighbor):
                break
            else:
                new_neighbor = []

        neighborhood.append(new_neighbor)
       
    return neighborhood
