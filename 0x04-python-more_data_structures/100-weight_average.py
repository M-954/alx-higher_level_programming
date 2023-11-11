#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_score_sum = sum(score * weight for score, weight in my_list)
    weight_sum = sum(weight for _, weight in my_list)

    if weight_sum == 0:
        return 0

    return weight_score_sum / weight_sum
