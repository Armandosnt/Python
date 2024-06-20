import random
a=['da', 'net', 'poka']
b=len(max(a))
for i in range (len(a)):
    c=b-len(a[i])
    print("*" * c + str(a[i]))