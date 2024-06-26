def UpperBound(A, key): 
    left = -1 
    right = len(A) 
    while right > left + 1: 
        middle = (left + right) // 2 
        if A[middle] > key: 
            right = middle 
        else: 
            left = middle 
    return right

result = UpperBound(A, 73)
print(result)