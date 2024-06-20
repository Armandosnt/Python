#from random import randint

#N = 10
#array = [ ]

#for number in range(N):
    #array.append(randint(1,99))
    

#print(array)

def linear_search (array , n):
    index = 0
    for a in array:
        if a == n:
            return index      
        index += 1
    return None

result = linear_search(array, 73)
print(result)



    