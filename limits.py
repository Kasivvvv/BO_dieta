from neighborhood import sum_of_nutritious
from classes import recipe

def is_calories_ok(recipes: list[recipe], cal_min: int, cal_max: int):
    cal_sum, fat_sum, carbs_sum, protein_sum = sum_of_nutritious(recipes)
    if cal_sum < cal_min or cal_sum > cal_max:
        return False
    else:
        return True
def is_fat_ok(recipes: list[recipe], fat_min: int, fat_max: int):
    cal_sum, fat_sum, carbs_sum, protein_sum = sum_of_nutritious(recipes)
    if fat_sum < fat_min or fat_sum > fat_max:
        return False
    else:
        return True

def is_carbs_ok(recipes: list[recipe], carbs_min: int, carbs_max: int):
    cal_sum, fat_sum, carbs_sum, protein_sum = sum_of_nutritious(recipes)
    if carbs_sum < carbs_min or carbs_sum > carbs_max:
        return False
    else:
        return True

def is_protein_ok(recipes: list[recipe], protein_min: int, protein_max: int):
    cal_sum, fat_sum, carbs_sum, protein_sum = sum_of_nutritious(recipes)
    if protein_sum < protein_min or protein_sum > protein_max:
        return False
    else:
        return True