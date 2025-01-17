import pandas as pd                                    #Импорт библиотеки


df = pd.read_csv('data/user_behavior_dataset.csv')
"""
Чтение данных из файла. Представленный файл "user_behavior_dataset.csv"
содержит статистику использования смартфонов.
"""

colors = [                                                     #Назначение цветов
    'darkturquoise', 'khaki',
    'orangered', 'yellowgreen',
    'gold', 'olivedrab',
    'mediumspringgreen', 'deepskyblue',
    'crimson', 'yellow'
]

"""
Создание переменных для данных, извлеченных из файла
"""

users = df['User ID']                                  #Порядковый номер пользователя
device = df['Device Model']                         #Модель смартфона
OS = df['Operating System']                       #Операционная система
app_us = df['App Usage Time (min/day)']    #Время использования приложений (минут/день)
screen = df['Screen On Time (hours/day)']    #Время включенного экрана (часов/день)
battery = df['Battery Drain (mAh/day)']       #Расход заряда батареи (мА/день)
num_app = df['Number of Apps Installed']  #Количество установленных приложений
data_us = df['Data Usage (MB/day)']          #Использование данных (МБ/день)
age = df['Age']                                         #Возраст
gender = df['Gender']                                #Пол
UBC = df['User Behavior Class']                  #Класс поведения пользователя
