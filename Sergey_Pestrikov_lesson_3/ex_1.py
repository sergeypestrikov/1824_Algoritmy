# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9

# list = [0]*8

# for i in range(2, 100):
#    for j in range(2, 10):
#        if i % j == 0:
#            list[j-2] += 1
# i = 0
# while i < len(list):
#    print(i + 2, ' - ', list[i])
#    i += 1

for i in range(2, 10):
    print(f'Чисел кратных {i} count: {99 // i}')