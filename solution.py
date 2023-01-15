import random
from classes import recipe, storage

def new_solution(products: storage, recipes: list[recipe],weeks:int = 1):
    to_use = len(products.products) // 2
    while 1:
        solution = random.sample(recipes, weeks*21)
        used_products = []
        for recipe in solution:
            for ingredient in recipe.ingredients:
                if ingredient[0] in products.products.keys() and ingredient[0] not in used_products:
                    used_products.append(ingredient[0])
        if len(used_products) >= to_use:
            break
    return solution

