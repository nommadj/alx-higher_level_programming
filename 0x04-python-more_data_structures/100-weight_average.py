#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    weighted_sum = sum(score * weight for score, weight in my_list)
    sum_weights = sum(weight for _, weight in my_list)

    return weighted_sum / sum_weights
