"""
    ============================================ №6*
Имеется банковское API возвращающее JSON
{
 "Columns": ["key1", "key2", "key3"],
 "Description": "Банковское API каких-то важных документов",
 "RowCount": 2,
 "Rows": [
  ["value1", "value2", "value3"],
  ["value4", "value5", "value6"]
 ]
}
Основной интерес представляют значения полей "Columns" и "Rows",
которые соответственно являются списком названий столбцов и значениями столбцов

Задание:
 1. Получить JSON из внешнего API
  ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
 2. Валидировать входящий JSON используя модель pydantic
  (из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
 2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
 3. В полученном DataFrame произвести переименование полей по след. маппингу
  "key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
 3. Полученный DataFrame обогатить доп. столбцом:
  "load_dt" -> значение "сейчас"(датавремя)
"""

import requests
from datetime import datetime
import pandas as pd
from pydantic import BaseModel

# Валидация входящего JSON используя модель pydantic
class Values(BaseModel):
    key1: int
    key2: datetime
    key3: str

def validationJsonData():
    url = 'https://api.gazprombank.ru/very/important/docs?documents_date=' + str(datetime.now())
    response = requests.get(url)
    my_json = response.json() # Не удалось получить JSON из внешнего API
#################################################################################################       
    data = [dict(zip(my_json['Columns'], x)) for x in my_json["Rows"]]
    for value in data:
        print('Валидация данных "{}"'.format(value))
        try:
            valid_result = Values(**value)
            print(valid_result)
        except ValueError as e:
            print(e.errors())

    # Представление данных
    df = pd.DataFrame(data)
    print('Представление данных в виде csv: \n {}'.format(df))

    # Переименование полей
    columns = {"key1": "document_id", "key2": "document_dt", "key3": "document_name"}
    df = df.rename(columns=columns)
    print('Переименованный DataFrame\n {}'.format(df))

    # Добавление дополнительного столбца:
    df['значение "сейчас"'] = datetime.now()
    print('Обогащенный DataFrame\n {}'.format(df))

if __name__ == '__main__':
    validationJsonData()