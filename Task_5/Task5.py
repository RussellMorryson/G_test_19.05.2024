"""
============================================ №5*
В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.

Задание:
Написать программу которая выводит список слов, каждый элемент списка которого - 
это новое слово, которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения

Например, текстовый файл содержит слова: 
ласты
стык
стыковка
баласт
кабала
карась

Пользователь вводмт первое слово: ласты
Программа выводит: ластык ластыковка

Пользователь вводмт первое слово: кабала
Программа выводит: кабаласты кабаласт

Пользователь вводмт первое слово: стыковка
Программа выводит: стыковкабала стыковкарась
"""
# Функция для чтения файла и вывода составных слов
def compoundWords():
    print('Программа для поиска составных слов')
    #file_path = input('Введите путь к файлу: ')
    file_path = 'Task_5/text.txt'
    words = []
    
    # Чтение файла и запись слов в массив words
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words.append(line.replace('\n', ''))
        file.close()

    # Инициализация переменных
    word = input('Введите слово для поиска: ')
    first_word = ''
    second_word = ''
    new_word = first_word
    count = 0
    used_words = []
    
    # Основной цикл сравнения слов
    while len(new_word) >= 2:
        for w in words:
            if new_word in w and w != word:
                first_word.replace(new_word, '')
                second_word = str(w)
                
                # Если влово ранее уже использовалось, то его вывод не доступен
                if second_word not in used_words:
                    used_words.append(second_word)
                    second_word = second_word.replace(new_word, '')
                    print(first_word + second_word)
                    count +=1
                first_word = word
            if count == 2:
                break
        if count == 2:
            break
        new_word = new_word[1:len(new_word)] # Формирование среза слова пользователя
    print('Выполнение вывода двух составных слов, завершено!')

if __name__ == '__main__':
    compoundWords()