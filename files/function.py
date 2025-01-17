import matplotlib.pyplot as plt                               #Импорт библиотек
import numpy as np


def rotation_3d(ax, mode):
    """
    Функция rotation_3d принимает 2 аргумента –
    график "ax" и режим вращения "mode",
    производя  вращение 3д графика в 2 режимах
    """
    if mode == 1:
        """
        1 режим - вращение относительно оси Z;
        """
        for angle in range(0, 180 + 1):
            angle_norm = (angle + 180) % 360 - 180
            rotation1 = 0
            if angle <= 180:
                rotation1 = angle_norm
            ax.view_init(azim=rotation1)
            plt.draw()
            plt.pause(.001)
    if mode == 2:
        """
        2 режим - вращение относительно осей X и Y.
        """
        for angle in range(0, 360 * 3 + 1):
            angle_norm = (angle + 180) % 360 - 180
            rotation1 = rotation2 = 0
            if angle <= 360:
                rotation1 = angle_norm
            elif angle <= 360 * 2:
                rotation2 = angle_norm
            else:
                rotation1 = rotation2 = angle_norm
            ax.view_init(elev=rotation1, roll=rotation2)
            plt.draw()
            plt.pause(.001)


def random_walk(steps):
    """
    Функция "random_walk" рассчитывает логику произвольного
    построения линии на графике. Принимает аргумент "steps"
    (количество шагов отрисовки). Переменная "start_pos" задает координату
    старта отрисовки. Переменная "max_step" отвечает за величину отклонения
    координат для отрисовки линии (в случайном порядке). Функция возвращает
    список "walk"
    """
    start_pos = (0.5, 0.5, 0.5)
    max_step = 0.03
    step = np.random.uniform(-max_step, max_step, size=(steps, 3))
    walk = start_pos + np.cumsum(step, axis=0)
    return walk


def update_lines(num, walks, lines):
    """
    Функция "update_lines" производит обновление отрисовки линий на графике.
    Принимает аргументы "num", "walks", "lines". Возвращает измененный
    список "lines"
    """
    for line, walk in zip(lines, walks):
        line.set_data_3d(walk[:num, :].T)
    return lines
