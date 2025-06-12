def diagonalDifference(arr):
    # Write your code here
    sum_1 = 0  # Primary diagonal sum
    sum_2 = 0  # Secondary diagonal sum
    n = len(arr)  # Assuming square matrix (arr_rows == arr_columns)

    for i in range(n):
        sum_1 += arr[i][i]                 # Primary diagonal
        sum_2 += arr[i][n - 1 - i]         # Secondary diagonal

    return abs(sum_1 - sum_2)              # Absolute difference
