def selection_sort(num_list):
    result = []
    while num_list:
        result.append(num_list.pop(num_list.index(max(num_list))))
    return result
    
a = list(map(int, input().split()))
print(*selection_sort(a))