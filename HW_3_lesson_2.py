# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer': (6, 7, 8),'autumn': (9, 10, 11)}

month = int(input('Введите число месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

seasons_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'winter', 'spring', 'summer', 'autumn']

month = int(input('Введите число месяца: '))
if month in seasons_list[0:3]:
    print(seasons_list[12])
elif month in seasons_list[3:6]:
    print(seasons_list[13])
elif month in seasons_list[5:9]:
    print(seasons_list[14])
elif month in seasons_list[9:12]:
    print(seasons_list[15])
