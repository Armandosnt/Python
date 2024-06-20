res = []
for x in range(1, 9, 2):
    res.append(x)
    res = [x**3 for x in range(1, 9, 2)]
    print(res) 