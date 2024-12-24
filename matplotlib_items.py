import matplotlib.pyplot as plt                                     #Импорт библиотек
import matplotlib.animation as animation
import function as f
import data_read as r


fig1 = plt.figure(figsize=(8, 5), dpi=80)
plt.bar(
    r.device[:10],
    r.data_us[:10],
    color='deepskyblue',
    width=0.58,
)
plt.title('Using data in models', fontsize=16)
plt.xlabel('Device Model')
plt.ylabel('Data Usage (MB/day)')
plt.show()

fig2 = plt.figure(figsize=(10, 4), dpi=80)
plt.plot(r.users[:10], r.age[:10], color='lime')
plt.scatter(r.users[:10], r.age[:10], color='magenta')
plt.title('Age of users', fontsize=16)
plt.xlabel('User ID')
plt.ylabel('Age')
plt.show()

fig3, ax1 = plt.subplots(figsize=(9, 7), dpi=80)
ax1.pie(
    r.data_us[:3],
    colors=r.colors,
    autopct='%1.1f%%',
    pctdistance=0.67,
    explode=(0, 0, 0.25),
    radius=0.7
)
ax1.legend(r.device[:3], title='Device Model', loc="lower left")
plt.title('Using data in models', fontsize=16)
plt.show()

fig4 = plt.scatter(r.age, r.users, c=r.age, alpha=0.58, cmap='cividis')
plt.xlabel('Age')
plt.ylabel('User ID')
plt.title('User ID by Age', fontsize=16)
plt.show()

fig5 = plt.figure(figsize=(7, 6), dpi=120)
ax2 = fig5.add_subplot(projection='3d')
ax2.scatter(r.UBC, r.age, r.users, c=r.age, alpha=0.58, cmap='cividis')
ax2.set_xlabel('User Behavior Class')
ax2.set_ylabel('Age')
ax2.set_zlabel('User ID')
plt.title('User Behavior Class by Age', fontsize=16)
f.rotation_3d(ax2, 1)
plt.show()

fig6 = plt.figure(figsize=(7, 6), dpi=120)                    #Создание изображения
ax3 = fig6.add_subplot(projection="3d")                   #Создание графика 3д-осей
steps = 1000                                                         #Количество шагов отрисовки
walks = [f.random_walk(steps) for index in range(4)]  #Создание списка количества линий
lines = [ax3.plot([], [], [])[0] for _ in walks]     #Создание списка координат линий
ax3.set(xlim3d=(0, 1))                                #Задание предела для осей координат
ax3.set(ylim3d=(0, 1))
ax3.set(zlim3d=(0, 1))
ax3.set_facecolor('dimgray')                       #Настройка цвета фона графика осей
plt.gcf().set_facecolor('dimgray')                 #Настройка цвета фона изображения
ani = animation.FuncAnimation(                 #Настраиваем объект анимации:
    fig6,                                        #Изображение графика, где отображается анимация
    f.update_lines,                         #Функция, импорт из модуля function
    steps,                                      #Переменная
    fargs=(walks, lines),                  #Списки параметров для функции update_lines
    repeat=False,                            #Зацикливать ли анимацию
    interval=10                               #Задержка между кадрами в мс
)
plt.axis('off')                                  #Отключаем график с осями (для лучшего восприятия)
f.rotation_3d(ax3, 2)            #Запуск функции
