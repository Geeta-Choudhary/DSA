def birthday(s, d, m):
    # Write your code here
    count_pair =0
    for i in range(len(s)-m+1):
        segment_sum =s[i:i+m]   
        if sum(segment_sum) == d:
            count_pair +=1
        
    return count_pair