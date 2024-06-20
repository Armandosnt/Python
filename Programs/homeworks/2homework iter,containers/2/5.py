from itertools import chain, permutations
 
s = "".join(filter(str.isalpha, input()))
result = tuple(chain.from_iterable(frozenset(map("".join, permutations(s, r))) for r in range(1, len(s) + 1)))
print(len(result))
print(*result, sep="\n")