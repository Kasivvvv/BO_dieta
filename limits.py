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

def acceptabiliy(solution : list[recipe]):
    is_solution_acceptable = 0
    calories = is_calories_ok(solution, 15000, 16000)
    fat = is_fat_ok(solution, 7*135, 7*140)
    carbs = is_carbs_ok(solution, 7*70,7*80)
    protein = is_protein_ok(solution,70*7,80*7)
    
    if calories and fat and carbs and protein:
        is_solution_acceptable = 1

    return is_solution_acceptable