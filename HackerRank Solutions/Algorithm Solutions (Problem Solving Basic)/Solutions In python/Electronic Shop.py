def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    price=[]
    for i in keyboards:
        for j in drives:
            total=i+j
            price.append(total)
    max_affordable = -1
    for i in price:
        if i <= b and i > max_affordable:
            max_affordable = i
    return max_affordable
