year = int(input('назовите год рождения А.С. Пушкина '))
if year != 1799:
    while year != int(1799):
        year = int(input('назовите год рождения А.С. Пушкина '))
day = str(input('назовите день рождения А.С. Пушкина '))
if day != '26 мая':
    while day != str('26 мая'):
        day = str(input('назовите день рождения А.С. Пушкина '))
print('Верно')