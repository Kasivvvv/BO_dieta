import numpy as np
import limits
import random
from  classes import recipe,product

def products_from_recipes(recipies : list[recipe]):
    list_of_products = []
    for recipe in recipies:
        list_of_products.append(recipe.ingredients)
    return list_of_products

def SE_children_replace_parents_rank(objective, neighborhood:list[list[recipe]], weights: list[float],weeks:int =1, N_iter : int  = 500,  mu:int = 20, lam:int = 100):
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial populationgi
    population = neighborhood
    # perform the search
    solution = []
    products = []
    for i in range(weeks):
        best, best_eval = neighborhood[0], 1e-10
        for epoch in range(N_iter):
            
        # evaluate fitness for the population
            scores = [objective(c,weights) for c in population]
        # rank scores in ascending order
            ranks = np.argsort(np.argsort(scores))
        # select the indexes for the top mu ranked solutions
            selected = [ i for i,_ in enumerate(ranks) if ranks[i] >=lam- mu]
        # create children from parents
            children = list()
            for i in selected:
        # check if this parent is the best solution ever seen
                if scores[i] > best_eval and limits.acceptabiliy(best):
                    best, best_eval = population[i], scores[i]
                    # create children for parent
                    child = []
                for _ in range(n_children):
                    while 1:
                        random_selected = random.sample(selected,1)
                        random_id = random.randint(0, 20)
                        child = population[i][:random_id] + population[random_selected[0]][random_id:-1]
                        if limits.acceptabiliy(child):
                            children.append(child)
                            break
        # replace population with children
            population = children

        products.append(products_from_recipes(best))
        solution.append([best, best_eval])

    return solution, products

def SE_children_and_parents_rank(objective, neighborhood:list[list[recipe]], weights: list[float],weeks:int =1, N_iter : int  = 10, mu:int = 20, lam:int = 100):
    best, best_eval = neighborhood[0], 1e-10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    solution = []
    for i in range(weeks):
        for epoch in range(N_iter):
        # evaluate fitness for the population
            scores = [objective(c,weights) for c in population]
        # rank scores in ascending order
            ranks = np.argsort(np.argsort(scores))
        # select the indexes for the top mu ranked solutions
            selected = [ i for i,_ in enumerate(ranks) if ranks[i] >=lam- mu]
        # create children from parents
            children = list()
            for i in selected:
        # check if this parent is the best solution ever seen
                if scores[i] > best_eval and limits.acceptabiliy(best) and len(children)<lam:
                    children.append(population[i])
                    best, best_eval = population[i], scores[i]
                    i+=1
                    print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
                    # create children for parent
                child = []
                for _ in range(n_children):
                    if  len(children)>=lam:
                        break
                    while 1:
                        random_selected = random.sample(selected,1)
                        random_id = random.randint(0, 20)
                        child = population[i][:random_id] + population[random_selected[0]][random_id:-1]
                        if limits.acceptabiliy(child):
                            children.append(child)
                            break
        # replace population with children
            population = children
            products = products_from_recipes(best)

        products.append(products_from_recipes(best))
        solution.append([best, best_eval])
    return solution, products

# TO DO: Dorobić ruletkę 
def SE_children_and_parents_rulette(objective, neighborhood:list[list[recipe]], weights: list[float],weeks:int =1, N_iter : int  = 10,  mu:int = 20, lam:int = 100):
    best, best_eval = neighborhood[0], 1e-10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    solution = []
    for i in range(weeks):
        for epoch in range(N_iter):
        # evaluate fitness for the population
            scores = [objective(c,weights) for c in population] #tutj se mamy wagi  [2,3,4,5]
            sum_scores = np.sum(scores)
            percent_scores = [i/sum_scores for i in scores] #tutaj mamy procetnowy udzial w kolejności wag pupulajcji [14.3, 21.4, 28.3, 35.7]
            index_list = np.linspace(0, lam-1,lam, dtype=int)
        
            selected = list(np.random.choice(index_list,mu, p=percent_scores))
            
    # create children from parents
            children = list()
            for i in selected:
        # check if this parent is the best solution ever seen
                if scores[i] > best_eval and limits.acceptabiliy(best) and len(children)<lam:
                    children.append(population[i])
                    best, best_eval = population[i], scores[i]
                    print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
                    # create children for parent
                child = []
                for _ in range(n_children):
                    if  len(children)>=lam:
                        break
                    while 1:
                        random_selected = random.sample(selected,1)
                        random_id = random.randint(0, 20)
                        child = population[i][:random_id] + population[random_selected[0]][random_id:-1]
                        if limits.acceptabiliy(child):
                            children.append(child)
                            break
        # replace population with children
            population = children
            products = products_from_recipes(best)
        solution.append([best,products, best_eval])
    return solution

def SE_children_replace_parents_rulette(objective, neighborhood:list[list[recipe]], weights: list[float],weeks:int =1, N_iter : int  = 10, mu:int = 20, lam:int = 100):
    best, best_eval = neighborhood[0], 1e-10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    solution = []
    for i in range(weeks):
        for epoch in range(N_iter):
        # evaluate fitness for the population
            scores = [objective(c,weights) for c in population] #tutj se mamy wagi  [2,3,4,5]
            sum_scores = np.sum(scores)
            percent_scores = [i/sum_scores for i in scores] #tutaj mamy procetnowy udzial w kolejności wag pupulajcji [14.3, 21.4, 28.3, 35.7]
            index_list = np.linspace(0, lam-1,lam, dtype=int)
            selected = list(np.random.choice(index_list,mu, p=percent_scores))
    # create children from parents
            children = list()
            for i in selected:
        # check if this parent is the best solution ever seen
                if scores[i] > best_eval and limits.acceptabiliy(best):
                    best, best_eval = population[i], scores[i]
                    print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
                    # create children for parent
                child = []
                for _ in range(n_children):
                    while 1:
                        random_selected = random.sample(selected,1)
                        random_id = random.randint(0, 20)
                        child = population[i][:random_id] + population[random_selected[0]][random_id:-1]
                        if limits.acceptabiliy(child):
                            children.append(child)
                            break
        # replace population with children
            population = children
            products = products_from_recipes(best)

        solution.append([best,products, best_eval])
    return solution