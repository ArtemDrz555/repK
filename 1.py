def decorator(func):
    def wrapper(v0, v, t):
        try:
            a=(v-v0)/t
        except ZeroDivisionError:
            print('время не должно быть равна 0')
        except TypeError:
            print('запишите числа')
        func(v0, v, t)
        s=v0*t+(a*t**2)/2
        print(s, '- расстояние')
        return wrapper



@decorator
def uskr(v0, v, t):
    a=(v-v0)/t
    print(a, '-ускорение')
    return a
uskr(15, 25, 5)
