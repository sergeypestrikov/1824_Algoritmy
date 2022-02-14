# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def get_average(a: int, b:int, c: int) -> int:
    if a > b and a < c:
        return a
    else:
        if b > a and b < c:
            return b
        else:
            return c

print(get_average(1, 5, 10))