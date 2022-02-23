# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

def swap_min_max(arr: list):
    ind_min = 0
    ind_max = 0

    for i in range(len(arr)):
        if arr[i] > arr[ind_max]:
            ind_max = i
        elif arr[i] < arr[ind_min]:
            ind_min = i

    sum = 0
    if ind_max < ind_min:
        ind_min, ind_max = ind_max, ind_min

    for i in range(ind_min + 1, ind_max):
        sum += arr[i]
    return sum

print(swap_min_max([1, 2, 3, 4]))
print(swap_min_max([4, 2, 1, 3])) # - Влад, не понимаю, почему считает 2 вместо 5
print(swap_min_max([1, 1, 5, 8]))