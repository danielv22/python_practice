from typing import List

def getMinumumAmountOfChange(coins: List[int]) -> int:
    coins.sort()

    currentAmount: int = 0

    for coin in coins:
        if coin > currentAmount + 1:
            return currentAmount + 1

        currentAmount += coin

    return currentAmount+1

# Test
array = [5, 7, 1, 1, 2, 3, 22]

try:
    response = getMinumumAmountOfChange(array)
    print(response) # Output: 20
except Exception as e:
    print(e.exception)