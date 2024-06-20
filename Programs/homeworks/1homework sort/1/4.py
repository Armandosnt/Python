from itertools import pairwise
 
a = [9, 4, 1, 6]
print(*min(pairwise(sorted(a)), key=lambda x: x[1] - x[0]))