def sortItems(items):
    for i in range(len(items)-1):
        for j in range(len(items)-(i+1)):
            if (items[j+1] < items[j]):
                aux = items[j]
                items[j] = items[j+1]
                items[j+1] = aux

    return items