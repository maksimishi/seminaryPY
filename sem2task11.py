a = int(input('Введите число: '))

i = 1
fib = 0
prev = 0


1
while fib < a:
    if i == 1:
        fib=0
    if i ==2:
        fib = 1
    temp=fib
    fib += prev
    prev = temp
    i+=1


if a == fib:
    print(i)
else:
    print(-1)