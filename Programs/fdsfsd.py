def linear_search (array , n):
    index = 0
    for a in array:
        if a == n:
            return index      
        index += 1
    return None

result = linear_search(Array , 73)
print(result)
