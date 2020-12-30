import random

def randselect(items):
    random_index = random.randint(0, len(items))
    return items[random_index]
