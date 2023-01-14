from classes import product, recipe, storage
import neighborhood
import solution
import main
from  SE import SE_children_and_parents, SE_children_replace_parents
import random
import numpy as np

test_storage = storage({})

for i in range(10):
    test_storage.add_product(test_storage,main.product_database[i])

print('done')
new_solution = solution.new_solution(test_storage,main.recipe_database)
neighborhood = neighborhood.neighborhood(new_solution)
weight = np.arange(0,100,3)
solution = SE_children_and_parents(main.objective,neighborhood,weight)
