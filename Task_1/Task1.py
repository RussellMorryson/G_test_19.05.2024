#============================================ №1
# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""

# Функция по чтению и выводу на экран уникальных и повторяющихся записей 
# в рамках поставленной аздачи
def fileReader(path:str):
    main_dict = {}
    uni_dict = {}
    rep_dict = {}    
    with open(path, 'r', encoding='utf-8') as file:
        count = 0;
        for line in file:
            if count == 0:
                count +=1
                continue
            line = line.split('|')
            line[4] = line[4].replace('\n', '')
            main_dict[count] = line
            count +=1
        file.close()
        
    # Инициализация дополнительных переменных
    count = 1
    count_uni = 1
    count_rep = 1
    
    # Процедура по сравнению записей в рамках поставленной задачи
    for k, v in main_dict.items():
        reply = False
        count = 1
        
        # Процесс сравнивания и исключения задваивания в записях
        # Если запись имеет одинаковый id, то она будет записана в словарь rep_dict
        while count <= len(main_dict):
            if k != count and v[4] == main_dict[count][4]:
                if v not in rep_dict.values():
                    rep_dict[count_rep] = v
                    count_rep += 1
                if main_dict[count] not in rep_dict.values():
                    rep_dict[count_rep] = main_dict[count]
                    count_rep += 1
                reply = True
                break
            count += 1
            
        # Если запись уникальна, то на будет записана в словарь uni_dict
        if reply == False:
            uni_dict[count_uni] = v
            count_uni += 1
            
    main_dict.clear() # Освобождение памяти (очистка словаря)
    
    # Вывод на экран уникальных записей
    print("Unique:")
    for k, v in uni_dict.items():
        print(f'{k}: {v}')
    
    # Вывод на экран записей с одинаковым id
    print("Repeties:")
    for k, v in rep_dict.items():
        print(f'{k}: {v}')    

# Точка входа
if __name__ == '__main__':
    #path = input()
    fileReader('Task_1/file.csv')