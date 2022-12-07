import numpy as np
import random

class product:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price


class storage:
    def __init__(self):
        self.products = {}
        
    def pop_product(self, item:str, amount_to_pop:float):
        if amount_to_pop <= self.products[item]:
            self.products[item] -= amount_to_pop
        else:
            raise NameError('There is not enough product')
    
    def add_product(self, item:str, amount:float = 1):
        self.products[item] = amount
        
    
class recipe:
    def __init__(self, name:str, ingredients:list[(str, int)], calories:int, fat:int, carbs:int, protein:int):
        self.name = name
        self.ingredients = ingredients #list of tuples containing names and needed amount of ingredients
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        
        
