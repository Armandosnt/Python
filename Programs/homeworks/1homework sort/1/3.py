n = int(input())
arr = [int(input()) for _ in range(n)]
a = sorted(arr, reverse=True)
print(sum(a[::3]) + sum(a[1::3]))