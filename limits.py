from classes import recipe

def sum_of_nutritious(recipes:list[recipe]):
    calories = 0
    fat = 0
    carbs = 0
    protein = 0
   
    for i in range(len(recipes)):
        calories += recipes[i].calories
        fat += recipes[i].fat
        carbs += recipes[i].carbs
        protein += recipes[i].protein

    return calories, fat, carbs, protein

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
    calories = is_calories_ok(solution, 10000, 15000)
    fat = is_fat_ok(solution, 1200, 1900)
    carbs = is_carbs_ok(solution, 45*21,21*60)
    protein = is_protein_ok(solution,25*21,40*21)
    
    if calories and fat and carbs and protein:
        is_solution_acceptable = 1

    return is_solution_acceptable