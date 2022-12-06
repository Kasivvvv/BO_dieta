import numpy as np


class product:
    def __init__(self, name:str, price:float, amount: float = 0):
        self.name = name
        self.price = price


class storage:
    def __init__(self, product: product):
        self.product = product
        
    
    def pop(self, item:product, to_pop:float):
    
    def get_product(self, ):