n = int(input("Введите количество монет: "))
heads = int(input("Введите количество монет, лежащих решкой вверх: "))

tails = n - heads

min_flips = min(heads, tails)

print("Минимальное количество монет, которые нужно перевернуть:", min_flips)
