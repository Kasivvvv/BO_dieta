import numpy as np
import random
from classes import product, recipe, storage
import neighborhood
import solution
import pandas as pd

RECIPE_DATABASE_LEN = 26
PRODUCT_DATABASE_LEN = 26
recipe_database_csv = pd.read_csv('C:/Users/kasia/OneDrive/Dokumenty/Kasia/Studia/BO/BO_dieta/recipe_database.csv')
product_database_csv = pd.read_csv('C:/Users/kasia/OneDrive/Dokumenty/Kasia/Studia/BO/BO_dieta/product_database.csv')

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

        

product_database = []
recipe_database = []

for index,row in product_database_csv.iterrows():
    name = row['product_name']
    price = row['price']
    product_database.append(product(name, price))

for index,row in recipe_database_csv.iterrows():
    name = row['recipe_name']
    ingredients = row['ingredients']
    calories = row['calories']
    fat = row['fat']
    carbs = row['carbs']
    protein = row['protein ']
    recipe_to_add = recipe(name, ingredients,calories,fat,carbs,protein)
    
    recipe_database.append(recipe_to_add)
print(recipe_database)

