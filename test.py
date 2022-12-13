from classes import product, recipe, storage
import neighborhood
import solution
import main

new_solution = solution.new_solution(main.recipe_database)
neighborhood.neighborhood(new_solution,1800*7, 70*7,135*7,70*7)
