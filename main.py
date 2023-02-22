#Задание 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите два варианта решения: через list и через dict.

#Через List

seasons_list = ('Зима','Весна','Лето','Осень')
month = int(input("Введите месяц по номеру: "))
if month ==1 or month == 12 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month ==8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

#Через Dict

seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц по номеру: "))
if month ==1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month ==8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
else:
    print("Такого месяца не существует")

#Задание 2. Реализовать структуру «Рейтинг», представляющую собой не
#возрастающий набор натуральных чисел
#(каждый элемент ряда меньше или равен предыдущему).
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них.

number = int(input("Enter number: "))
my_list = [7, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

#Задание 3. Реализовать структуру данных «Товары». Она должна представлять
#собой список кортежей.Каждый кортеж хранит информацию об отдельном товаре.
#В кортеже должно быть два элемента — номер товара и словарь с параметрами
#(характеристиками товара: название, цена, количество, единица измерения).
#Структуру нужно сформировать программно, т.е. запрашивать все данные
#у пользователя.Далее необходимо собрать аналитику о товарах. Реализовать
#словарь,в котором каждый ключ — характеристика товара, например название,
#а значение — список значений-характеристик, например список названий товаров.

