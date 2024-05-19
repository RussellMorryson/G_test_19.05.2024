#============================================ №4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import os
import platform
import time
from datetime import date 
import calendar

# Фукнция для решения основной задачи задания (удаление старых файлов)
def deletingOldFiles():
    print('Программа для удаления файлов старше указанного периода') 
    while(True):
        try:
            N = int(input('Введите количество дней: '))
            break
        except:
            print('Повторите попытку!')
        
    #folder_path = input('Укажите путь: ') 
    #folder_path = folder_path.replace('\\', '/')
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'June': 6, \
        'July': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11,'Dec': 12}
  
    # Блок кода по расчету количества дней с рождества христова на текущий момент
    current_date = str(date.today()).split('-')
    today = 0
    year = 1
    while year < int(current_date[0]):
        today += sum(map(lambda x: calendar.monthrange(year, x)[1], range(1, 13)))
        year +=1
    today += sum(map(lambda x: calendar.monthrange(int(current_date[0]), x)[1], range(1, int(current_date[1]))))
    today += int(current_date[2])
    
    for file_path in os.listdir():
        if os.path.isfile(file_path):            
            # Данный блок кода относится к выборке информации о дате создания файла дял ОС Windows
            if platform.system() == 'Windows':
                file_create_date = time.ctime(os.path.getctime(file_path)).split()                
                file_days = 0                
                year = 1
                # Расчет количества дней в годах до текущего года
                while year < int(file_create_date[4]):
                    file_days += sum(map(lambda x: calendar.monthrange(year, x)[1], range(1, 13)))
                    year +=1 
                
                # Конвертация строки названия месяца в число
                for k, v in months.items():
                    if k == file_create_date[1]:
                        file_create_date[1] = v
                        break
                # Суммирование количества дней в предшествующих месяцах
                file_days += sum(map(lambda x: calendar.monthrange(int(file_create_date[4]), x)[1], range(1, int(file_create_date[1]))))
                # Суммирование даты создания
                file_days += int(file_create_date[2])

                # Финишное сравнение количества дней от создания файла 
                if today - file_days > N:
                    os.remove(file_path)
                    print(f'Файл {file_path} удален. Дата его создания старше {N} дней.')    
    print('Процесс завершен!')

if __name__ == '__main__':    
    deletingOldFiles()