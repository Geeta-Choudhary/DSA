def pageCount(n, p):
    # Write your code here
    front_pages=p//2
    back_pages=n//2 - front_pages
    min_Count=min(front_pages,back_pages)
    return min_Count