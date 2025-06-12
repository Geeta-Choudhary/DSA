def migratoryBirds(arr):
    # Write your code here
    max_count=0
    bird_id=0
    types=[1,2,3,4,5]
    for i in types:
        current_count=arr.count(i)
        if current_count > max_count:
            max_count = current_count
            bird_id = i
        elif current_count == max_count and i < bird_id:
            bird_id = i
    return bird_id