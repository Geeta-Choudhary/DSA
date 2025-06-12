def miniMaxSum(arr):
    # Write your code here
    for i in range(0,len(arr)-1):
        for j in range (0,len(arr)-i-1):
            if (arr[j] > arr[j + 1]) :
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            
    min = 0
    max = 0

#Minimum sum: first 4 elements
    for i in range(0,4):
        min += arr[i]
    

#Maximum sum: last 4 elements
    for  i in range(1,5):
        max += arr[i]
    

    print(f"{min} {max}")