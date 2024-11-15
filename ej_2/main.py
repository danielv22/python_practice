from general import sortItems
import re

def squareNumbers(elemLts, s: int):
    result = []

    if s >= 0 and s <= 9:
        max_flag = s*11
    else:
        raise ValueError('El valor de "s" debe estar entre 0 y 9')

    for elem in elemLts:
        try:
            # Intenta convertir el elemento a entero
            num = int(elem)
        except ValueError:
            raise ValueError('La lista debe contener solo valores numéricos.')

        square = num ** 2

        if square < max_flag:
            result.append(square)

    return sortItems(result)