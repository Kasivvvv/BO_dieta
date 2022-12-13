from neighborhood import sum_of_nutritious
from classes import recipe

def is_fullfied_conditions(recipes: list[recipe], cal: list[int], fat: list[int], carbs: list[int], protein: list[int]):
    cal_sum, fat_sum, carbs_sum, protein_sum = sum_of_nutritious(recipes)
    if cal_sum < cal[0] or cal_sum > cal[1]:
        return False
    elif fat_sum < fat[0] or fat_sum > cal[1]:
        return False
    elif carbs_sum < carbs[0] or carbs_sum > carbs[1]:
        return False
    elif protein_sum < protein[0] or protein_sum > protein[1]:
        return False
    else:
        return True