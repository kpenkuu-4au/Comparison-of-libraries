# Comparison-of-libraries

Анализ и сравнение построения графиков 
для визуализации данных при помощи 
различных библиотек Python.

## Описание проекта

Проект представляет собой дипломную работу
по теме "Сравнение различных библиотек 
для визуализации данных: Matplotlib, Seaborn и Plotly"

## Установка проекта

1. Клонируйте проект с GitHub:

git clone https://github.com/kpenkuu-4au/Comparison-of-libraries.git


2. Перейдите в папку проекта:

cd Comparison-of-libraries


3. Создайте виртуальное окружение (если используется):  

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate  # Для Windows


4. Установите зависимости:  

pip install -r requirements.txt

## Использование проекта

Запустите основной скрипт:

python main.py и следуйте указаниям.

## Основной функционал

Предоставляется выбор просмотра примеров
визуализаций в модулях "matplotlib_items"(функция "start_plt_items"), 
"seaborn_items" (функция "start_sns_items"),
"plotly_items" (функция "start_gopx_items"). 
С помощью модуля "data_read" производится 
чтение файлов из папки "data". В модуле "function" находятся 
все необходимые функции.

## Структура проекта

- main.py - Главный файл запуска
- files - Директория с модулями обработки данных
- items - Директория с модулями визуализации данных
- data - Директория c файлами баз данных
- README.md - Документация проекта
- requirements.txt - Список зависимостей

---

## Автор проекта

Павел Колчанов, джуниор python-разработчик
