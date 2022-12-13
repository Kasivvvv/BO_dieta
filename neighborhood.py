import solution
import numpy as np
import random
from classes import recipe
import acceptability
import main

def sum_of_nutritious(recipes:list[recipe]):
    calories = 0
    fat = 0
    carbs = 0
    protein = 0
    for i in range(len(recipes)):
        calories += recipes[i].calories
        fat += recipes[i].fat
        carbs += recipes[i].carbs
        protein += recipes[i].protein

    return calories, fat, carbs, protein

def neighborhood(current_solution : list[recipe],calories:int, fat:int, carbs:int, protein:int, amount:int = 10):
    neighborhood = np.ndarray()

    for i in range(amount+1):
        index_of_recipe = random.randint(0,20)
        recipes  = random.sample(current_solution,index_of_recipe)
        np.append(neighborhood, np.ndarray(recipes))
        current_calories, current_fat, current_carbs, current_protein = sum_of_nutritious(neighborhood)
        calories -= current_calories
        fat -= current_fat
        carbs -= current_carbs
        protein -= current_protein

        while 1:
            recipes  = random.sample(main.recipe_database,21 - index_of_recipe)
            new_neighborhood =  np.append(neighborhood, np.ndarray(recipes))

            if acceptability.acceptabiliy(new_neighborhood):
                break
            else:
                new_neighborhood = neighborhood