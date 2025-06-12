def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    n=len(arr)
    
    for i in range(n):
        if (arr[i] > 0):
            positive_count+=1
        elif (arr[i]<0):
            negative_count +=1
        elif (arr[i] == 0):
            zero_count +=1
    pos_frac=positive_count / n
    neg_frac=negative_count/n
    zero_frac=zero_count/n
    
    print("{:.6f}".format(pos_frac))
    print("{:.6f}".format(neg_frac))
    print("{:.6f}".format(zero_frac))