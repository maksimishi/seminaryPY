S = int(input("Введите сумму двух чисел: "))
P = int(input("Введите произведение двух чисел: "))

D = S*S - 4*P
if D < 0:
    print("Нет решений")
else:
    Y1 = (S + D**0.5) / 2
    Y2 = (S - D**0.5) / 2
    X1 = S - Y1
    X2 = S - Y2
    print("Ответы: ", int(X1), int(Y1), int(X2), int(Y2))
