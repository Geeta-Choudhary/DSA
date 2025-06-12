def divisibleSumPairs(n, k, ar):
    # Write your code here
    count_pair=0
    for i in range(n):
        for j in range(i+1,n):
            total = ar[i]+ ar[j]
            if total%k==0:
                count_pair+=1
    return count_pair