def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        a = num_list[i]
        pos = i
        while pos > 0 and num_list[pos - 1] > a:
            num_list[pos] = num_list[pos - 1]
            pos -= 1
        num_list[pos] = a
 
 
arr = [1, 4, 2, 3, 4]
insertion_sort(arr)
print(arr)