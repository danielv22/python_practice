from typing import List

def getMinumumAmountOfChange(coins: List[int]) -> int:
    coins.sort()

    currentAmount: int = 0

    for coin in coins:
        if coin > currentAmount + 1:
            return currentAmount + 1

        currentAmount += coin

    return currentAmount+1