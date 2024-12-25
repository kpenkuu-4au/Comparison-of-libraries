import matplotlib.pyplot as plt                                     #Импорт библиотек
import matplotlib.animation as animation
from files import data_read as r, function as f
import time


def start_plt_items():                               #Функция вывода визуализаций "matplotlib"
    fig1 = plt.figure(figsize=(8, 5), dpi=80)                   #Создаем изображение
    plt.bar(                                                               #График "Столбцы"
        r.device[:10],                                                    #Используем данные из
        r.data_us[:10],                                                 #модуля "data_read"
        color='deepskyblue',                                           #Цвета столбцов
        width=0.58,                                                      #Ширина столбцов
    )
    plt.title('Using data in models', fontsize=16)    #Название графика
    plt.xlabel('Device Model')                                         #Название оси Х
    plt.ylabel('Data Usage (MB/day)')                              #Название оси У
    plt.show()                                                             #Вывод на экран графика

    fig2 = plt.figure(figsize=(10, 4), dpi=80)
    plt.plot(r.users[:10], r.age[:10], color='lime')   #График "Линии"
    plt.scatter(r.users[:10], r.age[:10], color='magenta')   #Создание точек на изломах графика
    plt.title('Age of users', fontsize=16)
    plt.xlabel('User ID')
    plt.ylabel('Age')
    plt.show()

    fig3, ax1 = plt.subplots(figsize=(9, 7), dpi=80)
    ax1.pie(                                                                 #График "Пирог"
        r.data_us[:3],
        colors=r.colors,                                                   #Цвета берутся из модуля data_read
        autopct='%1.1f%%',                                            #Отображение процентного соотношения
        pctdistance=0.67,                                               #Дистанции надписи процентов от центра графика
        explode=(0, 0, 0.25),                                           #Отделение доли "Пирога"
        radius=0.7                                                         #Радиус графика
    )
    ax1.legend(r.device[:3], title='Device Model', loc="lower left")    #Легенда графика
    plt.title('Using data in models', fontsize=16)
    plt.show()

    fig4 = plt.scatter(r.age, r.users, c=r.age, alpha=0.58, cmap='cividis')  #График рассеяния
    plt.xlabel('Age')
    plt.ylabel('User ID')
    plt.title('User ID by Age', fontsize=16)
    plt.show()

    fig5 = plt.figure(figsize=(7, 6), dpi=120)
    ax2 = fig5.add_subplot(projection='3d')                                          #Создание 3д проекции
    ax2.scatter(r.UBC, r.age, r.users, c=r.age, alpha=0.58, cmap='cividis')  #График рассеяния в 3д
    ax2.set_xlabel('User Behavior Class')
    ax2.set_ylabel('Age')
    ax2.set_zlabel('User ID')
    plt.title('User Behavior Class by Age', fontsize=16)
    f.rotation_3d(ax2, 1)                                         #Вызов функции из модуля "function"
    plt.show()

    fig6 = plt.figure(figsize=(7, 6), dpi=120)                    #Создание изображения
    ax3 = fig6.add_subplot(projection="3d")                   #Создание графика 3д-осей
    steps = 1000                                                         #Количество шагов отрисовки
    walks = [f.random_walk(steps) for index in range(4)]  #Создание списка количества линий
    lines = [ax3.plot([], [], [])[0] for _ in walks]     #Создание списка координат линий
    ax3.set(xlim3d=(0, 1))                                #Назначение предела для осей координат
    ax3.set(ylim3d=(0, 1))
    ax3.set(zlim3d=(0, 1))
    ax3.set_facecolor('dimgray')                       #Настройка цвета фона графика осей
    plt.gcf().set_facecolor('dimgray')                 #Настройка цвета фона изображения
    ani = animation.FuncAnimation(                 #Настраиваем объект анимации:
        fig6,                                        #Изображение графика, где отображается анимация
        f.update_lines,                         #Функция "update_lines", импорт из модуля "function"
        steps,                                      #Переменная
        fargs=(walks, lines),                  #Списки параметров для функции update_lines
        repeat=False,                            #Зацикливать ли анимацию
        interval=10                               #Задержка между кадрами в мс
    )
    plt.axis('off')                                  #Отключаем график с осями (для лучшего восприятия)
    f.rotation_3d(ax3, 2)            #Вызов функции из модуля "function"
    plt.show()
