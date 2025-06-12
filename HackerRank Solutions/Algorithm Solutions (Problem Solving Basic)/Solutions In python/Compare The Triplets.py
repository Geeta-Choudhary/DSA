def compareTriplets(a, b):
    # Write your code here
    solution=[0,0]
    
    for i in range(3):
        if a[i]>b[i]:
            solution[0] += 1
        elif a[i]<b[i]:
            solution[1] += 1
    return solution
            