import random
from random import randint
from collections import Counter

class GameLogic:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def calculate_score(kept_dice):
        score = 0
        x = Counter(kept_dice)
        num_keys = list(x.items())

        #Straight Scoring
        if x[1] == 1 & x[2] == 1 & x[3] == 1 & x[4] == 1 & x[5] == 1 & x[6] == 1:
            score = 1500
            return score

        #Three pair scoring
        if len(num_keys) == 3:
            if num_keys[0][1] == 2 & num_keys[1][1] == 2 & num_keys[2][1] == 2:
                score = 1500
                return score

        #Three or more of a kind
        for pairs in num_keys:
            num = 0
            i = 3
            if pairs[0] != 1:
                if pairs[1] >= 3:
                    num = pairs[0] * 100
                    if pairs[1] > 3:
                        while i < pairs[1]:
                            num += pairs[0] * 100
                            i += 1
            score += num

        #One scoring
        if x[1] > 2:
            score += int(round(((189.196 * x[1] ** 1.74457) - 229.844), -3))
        if 0 < x[1] <= 2:
            score += x[1] * 100

        #Five scoring
        if 0 < x[5] <= 2:
            score += x[5]*50

        return score


    @staticmethod
    def roll_dice(num):
        dice_set = []
        while len(dice_set) < num:
            dice_set.append(random.randint(1,6))

        return tuple(dice_set)