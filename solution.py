import random
from classes import recipe
def new_solution(recipes: list[recipe]):
    solution = random.sample(recipes, 21)
    return solution
