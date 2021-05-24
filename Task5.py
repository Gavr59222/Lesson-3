import sys

result = 0
while True:
    line = input("Введите числа или нажмите q для выхода: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result +=number

            print(f"Сумма чисел равна: {result}")
        except:
            if token == 'q':
                print(f"Сумма чисел равна: {result}. Программа завершена")
                exit(0)
            else:
                print(f"Сумма чисел равна: {result}. Ошибка ввода", file=sys.stderr)
                exit(1)
