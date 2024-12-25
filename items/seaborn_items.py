import matplotlib.pyplot as plt                                 #Импорт библиотек
import seaborn as sns
from files import data_read as r


def start_sns_items():                                     #Функция вывода визуализаций "seaborn"
    fig1 = plt.figure(figsize=(11, 5), dpi=120)       #Создание изображения
    sns.barplot(                                                #График "Столбцы
        x=r.num_app[:10],      # Данные импорта
        hue=r.OS[:10],            # из "data_read"
        palette='hls',                                          #Выбор палитры цветов для графика
        errorbar=None                                        #Отключение отображения ошибок
    )
    plt.show()                                                  #Вывод изображения на экран

    fig2 = plt.figure(figsize=(10, 5), dpi=120)
    sns.lineplot(                                                #График "Линии"
        x=r.app_us[:20],
        y=r.num_app[:20],
        palette='bright',
        hue=r.gender[:20]
    )
    plt.show()

    sns.jointplot(                                                #График "Сводная диаграмма"
        x=r.users[:50],
        y=r.age[:50],
        hue=r.gender[:50],
        palette='cubehelix'
    )
    plt.show()

    sns.relplot(                                                    #График "Диаграмма рассеяния"
        x=r.num_app,
        y=r.app_us,
        hue=r.age,                                                  #Параметр фильтрации по цвету
        style=r.device,                                             #Параметр фильтрации по форме
        size=r.UBC,                                                 #Параметр фильтрации по размеру
        col=r.gender,                                               #Параметр разделения графика
        palette='mako'
    )
    plt.show()

    """
    Скопируем код с 3д графиком из модуля "matplotlib_item" 
    и применим к нему цветовую схему из seaborn через
    переменную "cmap" (3д график можно вращать с помощью мыши)
    """
    cmap = sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)

    fig3 = plt.figure(figsize=(6, 5), dpi=200)
    ax2 = fig3.add_subplot(projection='3d')
    ax2.scatter(r.UBC, r.age, r.users, c=r.age, cmap=cmap)
    ax2.set_xlabel('User Behavior Class')
    ax2.set_ylabel('Age')
    ax2.set_zlabel('User ID')
    plt.title('User Behavior Class by Age', fontsize=16)
    plt.show()
