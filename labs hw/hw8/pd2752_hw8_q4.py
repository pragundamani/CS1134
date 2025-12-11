#q4 answer pd2752
def find_min_abs_difference(bst):
    mindiff = float('inf')
    prev = None
    for val in bst:
        if prev is not None:
            diff = val - prev
            if diff < mindiff:
                mindiff = diff
        prev = val
    return mindiff
