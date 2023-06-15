number = int(input("Введите число: "))

if number % 2 == 0:
    print("Число", number, "является четным.")
else:
    print("Число", number, "является нечетным.")

if number > 0:
    print("Число", number, "является положительным.")
elif number < 0:
    print("Число", number, "является отрицательным.")
else:
    print("Число равно нулю.")
    
if number > 10:
    print("Число", number, "больше 10.")
elif number < 10:
    print("Число", number, "меньше 10.")
else:
    print("Число равно 10.")
