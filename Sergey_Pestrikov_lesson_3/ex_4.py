# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

def min_twice(arr: list):
    first_min = max(arr)
    second_min = first_min

    for num in arr:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif num < second_min:
            second_min = num

    return first_min, second_min

print(min_twice([1, 1, 2, 3]))
print(min_twice([1, 3, 4, 5]))
print(min_twice([4, 5, 2, 3]))