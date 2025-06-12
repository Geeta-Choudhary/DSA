def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valleys = 0

    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1  # Came up to sea level from a valley
        elif step == 'D':
            altitude -= 1

    return valleys