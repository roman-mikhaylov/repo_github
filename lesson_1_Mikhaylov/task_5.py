profit = int(input('Введите выручку вашей фирмы '))
expenses = int(input('Введите издержки вашей фирмы '))
if profit-expenses > 0:
    print(f'Финансовый результат - Прибыль {profit - expenses}')
    print(f'Рентабельность - {((profit - expenses) / profit) * 100} %')
    workers = int(input('Сколько сотрудников работает в ващей фирме \n'))
    print(f'Прибыль фирмы расчете на одного сотрудника {(profit - expenses) / workers}')
else:
    print('Финансовый результат - Убыток')
