time = int(input('Введите время в секундах: '))
hour = time//3600
minute = time % 3600//60
sek = time % 60
if len(str(hour)) == 1:
    hour = '0'+str(hour)
if len(str(minute)) == 1:
    minute = '0'+str(minute)
if len(str(sek)) == 1:
    sek = '0'+str(sek)
print(f'{hour}:{minute}:{sek}')


