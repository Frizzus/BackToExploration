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
    

def sort_with_priority(tuples:list[tuple]) -> list[tuple]:
    """
    insertion sorting for sorting our tuple of feature path and priority
    """
    res = tuples

    for i in range(len(res)):
        current_value = res[i]
        position = i

        while position>0 and (res[position-1][1]>current_value[1] or (res[position-1][1]==current_value[1] and res[position-1][0]>current_value[0])):
            res[position]=res[position-1]
            position = position-1


        res[position]=current_value

    return res
                
def str_only_checking(ls:list) -> bool:
    not_allowed_types:list[type] = [int, float, tuple, dict, bool]
    ls_types = []

    for item in ls:
        ls_types.append(type(item))

    for item in not_allowed_types:
        if item in ls_types:
            return False
    return True

def no_double(ls:list) -> list:
    res = []

    for x in ls:
        if x not in res:
            res.append(x)

    return res