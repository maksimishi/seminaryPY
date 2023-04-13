number = input("Введите номер билета: ")
digits = [int(digit) for digit in number]  # разбиваем номер на отдельные цифры
# сравниваем сумму первых трех цифр с суммой последних трех
if sum(digits[:3]) == sum(digits[3:]):
    print("Билет", number, "является счастливым!")
else:
    print("Билет", number, "не является счастливым.")
