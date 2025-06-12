def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    new_apples=[]
    new_oranges=[]
    count_apple=0
    count_orange=0
    for i in apples:
        new_apples.append(i+ a)
    for j in oranges:
        new_oranges.append(j+b)
        
    for i in new_apples:
        if i in range(s,t+1):
            count_apple +=1
            
    for i in new_oranges:
        if i in range(s,t+1):
            count_orange +=1
            
        
    print(count_apple)
    print(count_orange)