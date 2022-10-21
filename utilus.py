from random import randint
import re


def roll_dice(how_many):
    result = randint(1, how_many)
    return result

def how_many_sides(callback: str):
    x = re.sub('[d\s]', '', callback)
    x = int(x)
    return x