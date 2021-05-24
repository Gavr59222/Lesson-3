def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "нельзя делить на ноль"


print(my_func(int(input("Введите число x = ")), int(input("Введите число y = "))))
