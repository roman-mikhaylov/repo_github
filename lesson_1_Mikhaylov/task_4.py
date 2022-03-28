num = input('введите целое, положительное число ')
list_num = list(num)
max_element = list_num[0]

while len(list_num) > 0:
    if int(max_element)-int(list_num[-1]) <= 0:
        max_element = list_num[-1]
    list_num.pop()
print(f'максимальная цифра в числе {num} это {int(max_element)}')
