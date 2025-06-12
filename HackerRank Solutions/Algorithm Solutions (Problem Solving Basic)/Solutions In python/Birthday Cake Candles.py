def birthdayCakeCandles(candles):
    # Write your code here
    max=candles[0]
    max_count=1
    
    for i in range (1,candles_count):
        if candles[i] > max:
            max= candles[i]
            max_count = 1
        elif candles[i] == max :
            max_count +=1
    return max_count