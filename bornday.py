year = int(input('назовите год рождения А.С. Пушкина '))
if year == 1799:
    day = str(input('а день рождения? '))
    if day == '26 мая':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
