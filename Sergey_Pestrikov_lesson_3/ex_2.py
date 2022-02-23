# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# from random import random

# n = 10
# list = [0]*n

# for i in range(n):
#    list[i] = int(random()*100)
#    print(list[i])
# print()

# min_num = min(list)
# max_num = max(list)
# index_min_num = list.index(min_num)
#index_max_num = list.index(max_num)
#print('list[%d]=%d list[%d]=%d' % (index_min_num + 1, min_num, index_max_num + 1, max_num))
#list[index_min_num], list[index_max_num] = list[index_max_num], list[index_min_num]
#for i in range(10):
#    print(list[i])
#print()

def swap_min_max(arr: list):
    ind_min = 0
    ind_max = 0

    for i in range(len(arr)):
        if arr[i] > arr[ind_max]:
            ind_max = i
        elif arr[i] < arr[ind_min]:
            ind_min = i

    arr[ind_min], arr[ind_max] = arr[ind_max], arr[ind_min]
    return arr

print(swap_min_max([1, 2, 3, 4]))
print(swap_min_max([4, 2, 1, 3]))
print(swap_min_max([1, 1, 5, 8]))
