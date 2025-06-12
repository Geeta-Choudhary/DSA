def breakingRecords(scores):
    highest_score = scores[0]
    lowest_score = scores[0]
    high_count = 0
    low_count = 0

    for score in scores[1:]:
        if score > highest_score:
            highest_score = score
            high_count += 1
        elif score < lowest_score:
            lowest_score = score
            low_count += 1

    return(high_count, low_count)