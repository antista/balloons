import math

import balloons_counter.constants as const


def count(weight, measure=const.DEFAULT_MEASURE):
    if measure == "gram":
        return math.ceil(weight / const.BALLOON_CARRYING)
    elif measure == "kilogram":
        return math.ceil((weight * const.GRAMS_IN_KILOGRAM) / const.BALLOON_CARRYING)
    elif measure == "tonne":
        return math.ceil((weight * const.KILOGRAMS_IN_TONNE * const.GRAMS_IN_KILOGRAM)
                         / const.BALLOON_CARRYING)
    else:
        return None


def convert(weight, measure):
    if measure == 'gram' and weight >= const.GRAMS_IN_KILOGRAM and not weight % const.GRAMS_IN_KILOGRAM:
        measure = 'kilogram'
        weight //= const.GRAMS_IN_KILOGRAM
    if measure == 'kilogram' and weight >= const.KILOGRAMS_IN_TONNE and not weight % const.KILOGRAMS_IN_TONNE:
        measure = 'tonne'
        weight //= const.KILOGRAMS_IN_TONNE
    return weight, measure
