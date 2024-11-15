from general import sortItems
import re

def lookForNAndDelete(elemLts, s: int):
    result = []

    if s >= 0 or s <= 9:
        strS = str(s)
    else:
        raise ValueError('El valor de "s" debe estar entre 0 y 9')

    for item in elemLts:
        strItem = str(item)

        if not re.match(r'^[0-9]+$', strItem):
            raise ValueError('La lista debe contener solo valores numéricos.')

        if strS in strItem and len(strItem) >= 1:
            value = strItem.replace(strS, '')

            if value:
                result.append(int(value))
        else:
            result.append(int(item))

    return sortItems(result)

# Test
array = [1, 2, 3, 4, 5, 8]
s = 8

try:
    response = lookForNAndDelete(array, s)
    print(response) # Output: [1, 2, 3, 4, 5]
except Exception as e:
    print(e.exception)