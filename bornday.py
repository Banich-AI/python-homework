"""
- Спросить у пользователя год рождения А.С. Пушкина
- Если пользователь ввел верный год спросить у него день рождения
- Если день рождения введен верно вывести 'Верно'
- Если день рождения введен неверно вывести 'Неверный день рождения'
- Если неверно введен год, то сразу вывести 'Неверный год'

"""

# Год рождения Пушкина
born_year = 1799
# print(type(born_year))
# День рождения Пушкина
born_day = '6 июня'

question_1 = int(input("Введите год рождения Пушкина А.С.: "))  # Запрос года рождения Пушкина
if question_1 == born_year:
    question_2 = input("Введите день рождения Пушкина А.С.: ")  # Запрос дня рождения Пушкина
    if question_2 == born_day:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
