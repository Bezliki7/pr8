sum = 0

while (not sum):
    try:
        firstNumber, secondNumber = int(input("Введите 1 число ")), int(input("Введите 2 число "))
        sum += firstNumber + secondNumber
    except ValueError:
        print("Неверный ввод!")

print(sum)