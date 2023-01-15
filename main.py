import numpy as np
import random
from classes import product, recipe, storage
import neighborhood
import solution
import pandas as pd

RECIPE_DATABASE_LEN = 26
PRODUCT_DATABASE_LEN = 26
recipe_database_csv = pd.read_csv('C:/Users/kasia/OneDrive/Dokumenty/Kasia/Studia/BO/BO_dieta/recipe_database.csv')
print(recipe_database_csv['Title'])

def objective(list_of_recipes:list[recipe], weights:list[float]): # weights = [calories_weight, fat_weight, carb_weight, protein_weight]
    calories_sum= 0
    fat_sum = 0
    carb_sum = 0
    protein_sum = 0
    
    for i in range(len(list_of_recipes)):
        calories_sum += list_of_recipes[i].calories
        fat_sum += list_of_recipes[i].fat
        carb_sum += list_of_recipes[i].carbs
        protein_sum += list_of_recipes[i].protein
        
    f_x = (weights[0]*calories_sum + weights[1]*fat_sum + weights[2]*carb_sum + weights[3]*protein_sum)/sum(weights)
    
    return f_x

        
if __name__ == "__main__":
    product_database = []
    recipe_database = []

    for i in range(PRODUCT_DATABASE_LEN):
        name = chr(97+i)
        product_database.append(product(name, random.randint(1, 100)))


    for index,row in recipe_database_csv.iterrows():
        name = row['name']
        recipe_to_add = recipe(name, random.choices(product_database, k=random.randint(1, 9)),
                                        random.randint(300, 700), random.randint(20, 90), random.randint(30, 60),
                                        random.randint(10, 40))
        
        recipe_database.append(recipe_to_add)

