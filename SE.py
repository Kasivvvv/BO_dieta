import numpy as np
import limits
import random
from  classes import recipe

def SE_children_replace_parents_rank(objective, neighborhood:list[list[recipe]], weights: list[float], N_iter : int  = 10,  mu:int = 20, lam:int = 500):
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    for epoch in range(N_iter):
    # evaluate fitness for the population
        scores = [objective(c,weights) for c in population]
    # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))
    # select the indexes for the top mu ranked solutions
        selected = [i for i,_ in enumerate(ranks) if ranks[i] > mu]
    # create children from parents
        children = list()
        for i in selected:
    # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
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
    return [best, best_eval]

def SE_children_and_parents_rank(objective, neighborhood:list[list[recipe]], weights: list[float], N_iter : int  = 10, mu:int = 20, lam:int = 100):
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    for epoch in range(N_iter):
    # evaluate fitness for the population
        scores = [objective(c,weights) for c in population]
    # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))
    # select the indexes for the top mu ranked solutions
        selected = [i for i,_ in enumerate(ranks) if ranks[i] < mu]
    # create children from parents
        children = list()
        for i in selected:
    # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
                children.append(population[i])
                best, best_eval = population[i], scores[i]
                i+=1
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
    return [best, best_eval]

def SE_children_replace_parents_rulette(objective, neighborhood:list[list[recipe]], weights: list[float], N_iter : int  = 10,  mu:int = 20, lam:int = 500):
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    for epoch in range(N_iter):
    # evaluate fitness for the population
        scores = [objective(c,weights) for c in population]
    # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))
    # select the indexes for the top mu ranked solutions
        selected = [i for i,_ in enumerate(ranks) if ranks[i] > mu]
    # create children from parents
        children = list()
        for i in selected:
    # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
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
    return [best, best_eval]

def SE_children_and_parents_rulette(objective, neighborhood:list[list[recipe]], weights: list[float], N_iter : int  = 10, mu:int = 20, lam:int = 100):
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = neighborhood
    # perform the search
    for epoch in range(N_iter):
    # evaluate fitness for the population
        scores = [objective(c,weights) for c in population]
    # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))
    # select the indexes for the top mu ranked solutions
        selected = [i for i,_ in enumerate(ranks) if ranks[i] < mu]
    # create children from parents
        children = list()
        for i in selected:
    # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
                children.append(population[i])
                best, best_eval = population[i], scores[i]
                i+=1
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
    return [best, best_eval]