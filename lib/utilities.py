import random

def weighted_choice(values:list, weights:list[int], over:int) -> any:
    weights_sum:int = 0
    weights_ranges:list[int] = []

    for nb in weights:
        weights_sum += nb
        weights_ranges.append(weights_sum)
        if nb < 0:
            raise ValueError("Values in weights must be positives : "+str(nb))

    if weights_sum != over:
        raise ValueError("The values in |weights| do not add up to |over| : "+str(over))

    random_value:int = random.randint(1, over)

    for index in range(len(weights_ranges)):
        if random_value <= weights_ranges[index]:
            return values[index]
    
