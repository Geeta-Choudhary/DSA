def sockMerchant(n, ar):
    # Write your code here
    freq=Counter(ar)
    count_pair=0
    for i in freq:
        count_pair +=freq[i]//2
    return count_pair
            