# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

goods = int(input('Введите количество товара: '))
n=1
storage = [] #склад
store = [] #магазин
analitics = {}
while n <= goods:
    storage = dict({ 'name': input('Введите наименование: '), 'price': input('Введите цену: '),
    'volume': input('Введите количество:'),'unit': input('Введите единицу измерения: ')})

    store.append((n, storage))
    n+=1
    analitics = {'name': storage.get('name'), 'price': storage.get('price'), 'volume': storage.get('volume'),
                 'unit': storage.get('unit')}
print('Goods in store: ', store)
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:{“название”: [“компьютер”, “принтер”, “сканер”],“цена”: [20000, 6000, 2000],“количество”: [5, 2, 7],“ед”: [“шт.”]
print(analitics)

#с аналитикой не получилось
