string_1 = 'a a a b c a a d c d d'

str_list = string_1.split()
print(str_list)
list_1 = []
for i in range(len(str_list)):
    if str_list[i] in list_1:
        print(f'{str_list[i]}_{list_1.count(str_list[i])}', end=' ')
    else:
        print(str_list[i], end=' ')
    list_1.append(str_list[i])
