#============================================ №2
# в наличии список множеств. внутри множества целые числа
# m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

# Задание: посчитать 
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж
# *написать решения в одну строку

if __name__ == '__main__':
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}] # Условие задачи
    print(len(m))

    count = 0       # Общее количество чисел
    sum = 0         # Общая сумма чисел
    avg = 0         # Среднее значение
    cort = []       # Кортеж

    for i in m:
        for j in i: count+=1; sum+=j;  cort.append(j);

    avg = sum / count

    print (f'Количество чисел = {count}')
    print (f'Сумма чисел = {sum}')
    print (f'Среднее значение = {avg}')
    print (f'Кортеж = {cort}')