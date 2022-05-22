def game():
    Musk = int(input('назовите год рождения Илона Маска '))  # правильный ответ 1971
    Bezos = int(input('назовите год рождения Джеффа Безоса '))  # правильный ответ 1964
    Gates = int(input('назовите год рождения Билла Гейтса '))  # правильный ответ 1955
    Jobs = int(input('назовите год рождения Стива Джопса '))  # правильный ответ 1955
    Korolev = int(input('назовите год рождения Сергея Королева '))  # правильный ответ 1907

    right = 0
    wrong = 0

    if Musk == 1971:
        right += 1
    else:
        wrong += 1

    if Bezos == 1964:
        right += 1
    else:
        wrong += 1

    if Gates == 1955:
        right += 1
    else:
        wrong += 1

    if Jobs == 1955:
        right += 1
    else:
        wrong += 1

    if Korolev == 1907:
        right += 1
    else:
        wrong += 1

    print('Ваши результаты: ')
    print('количество правильных ответов', right)
    print('количество ошибок', wrong)
    print('процент правильных ответов - ', right * 100 / 5, "%")
    print('процент неправильных ответов - ', wrong * 100 / 5, "%")


game()
question = str(input('Играем еще раз? '))
while question == 'да':
    game()
    question = str(input('Играем еще раз? '))
print('до скорого')


