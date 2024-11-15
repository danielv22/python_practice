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

# Test
array = [1, 2, 3, 4, 5, 8]
s = 8

try:
    response = squareNumbers(array, s)
    print(response) # Output: [1, 4, 9, 16, 25, 64]
except Exception as e:
    print(e.exception)