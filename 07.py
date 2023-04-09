year = int(input('Введите год чтобы узнать высокосный или нет'))

if year % 4 == 0 and year % 100!=0 or year % 400==0:
    print('Yes')
else:
    print('No')