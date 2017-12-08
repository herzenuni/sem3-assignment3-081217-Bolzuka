# Практическое задание 3 DATA.json
# Практическое задание, где студент должен написать скрипт,
# позволяющий считать данных из файла JSON, распарсить (разпознать их)
# и напечатать несколько значений полей в соответствующем формате
#
# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?
# Импортируйте необходимые библиотеки
# import
# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных
#
# Вывести в форматированном виде поля:
# company, email, phone, address

import json
import pprint

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        json_file = open("data.json", "r")
        cont = json_file.read()
        data = json.loads(cont)

except FileExistsError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'


for index, i in enumerate(data):
    print('\nData number in the list №', index)

    a = {}
    a.update(
		{'address':i.get('address')})
    pprint.pprint(a)

    b = {}
    b.update(
        {'company': i.get('company'),
         'email': i.get('email'),
         'phone': i.get('phone')})
    pprint.pprint(b)
