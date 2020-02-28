import math

import balloons_counter.constants as const


def count(weight, measure):
    if measure == const.GRAM_SYMBOL:
        return math.ceil(weight / const.BALLOON_CARRYING)
    elif measure == const.KILOGRAM_SYMBOL:
        return math.ceil((weight * const.GRAMS_IN_KILOGRAM) / const.BALLOON_CARRYING)
    elif measure == const.TONNE_SYMBOL:
        return math.ceil((weight * const.KILOGRAMS_IN_TONNE * const.GRAMS_IN_KILOGRAM)
                         / const.BALLOON_CARRYING)
    else:
        return None
