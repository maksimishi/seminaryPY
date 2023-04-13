import random
count_of_watermelon = int(input('Введите кол-во арбуов: '))
mim_weight = 30000
max_weight = 1
for i in range (count_of_watermelon):
    weight_of_watermellon = random.randint(1, 25000)
    print(f'Вес арбуза {i+1}: {weight_of_watermellon}')
    if weight_of_watermellon > max_weight:
        max_weight = weight_of_watermellon
    if weight_of_watermellon < mim_weight:
        mim_weight = weight_of_watermellon
print(f'Для себя: {max_weight}\n Для тёщи: {mim_weight}')