n = int(input("Введите количество долек шоколадки по горизонтали: "))
m = int(input("Введите количество долек шоколадки по вертикали: "))
k = int(input("Введите количество долек, которое нужно отломить: "))

if k % 2 == 0:
    if (n % 2 == 0) or (m % 2 == 0):
        print("Можно отломить", k, "долек.")
    else:
        print("Нельзя отломить", k, "долек.")
else:
    if n * m >= k and (n % 2 == 1 or m % 2 == 1):
        print("Можно отломить", k, "долек.")
    else:
        print("Нельзя отломить", k, "долек.")
