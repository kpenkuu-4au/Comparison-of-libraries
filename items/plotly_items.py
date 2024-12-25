import plotly.graph_objects as go      #Импорт библиотек
import plotly.express as px
from files import data_read as r


def start_go_items():            #Функция запуска визуализаций "graph objects"
    fig1 = go.Figure(
        [go.Bar(                        #График "Столбцы"
            x=r.device[:13],          #Ось Х - название смартфона
            y=r.num_app[:13],     #Ось У - количество установленных приложений
            text=r.gender[:13],      #Принадлежность к полу
            textposition='auto'      #Позиция текста
        )]
    )
    fig1.update_layout(
        title="Number of Apps Installed by Devise Model",       #Название графика
        xaxis_title="Device Model",                                       #Название оси Х
        yaxis_title="Number of Apps Installed"                      #Название оси У
    )
    fig1.show()                                                             #Вывод графика на экран

    fig2 = go.Figure(data=go.Scatter(           #График "Линии"
        x=r.users[:15],                                 #Ось Х - Порядковый номер пользователя
        y=r.screen[:15],                                #Ось У - Время включенного экрана смартфона
        mode='lines+markers',                      #Режим графика - линии+круги
        text=r.device[:15]                             #Текст при наведении - название смартфона
    ))
    fig2.update_layout(
        title="Screen On Time by users",
        xaxis_title="User ID",
        yaxis_title="Screen On Time (hours/day)"
    )
    fig2.show()

    fig3 = go.Figure(data=[go.Pie(     #График "Пирог"
        labels=r.device[:3],                 #Доли графика - названия смартфонов
        values=r.battery[:3],               #значение доли - расход батареи
        textinfo='value+percent',        #информация в тексте - значение расхода + процентное соотношение
        insidetextorientation='radial',  #Ориентация текста - по радиусу
        hole=.2,                                #Диаметр отверстия внутри графика
        pull=[0, 0, 0.3],                      #Отделение доли "пирога"
        text=r.OS[:3]                          #Текст при наведении - операционная система
    )])
    fig3.update_layout(title=dict(text='Battery Drain  by devices'))
    fig3.show()

    fig4 = go.Figure(data=go.Scatter(      #График рассеяния
        x=r.screen[:30],                           #Ось Х - Время включенного экрана смартфона
        y=r.users[:30],                            #Ось У - порядковый номер пользователя
        mode='markers',                         #Режим отображения - "круг"
        marker_color=r.battery[:30],         #Цвет круга отображает расход батареи смартфона
        marker=dict(
                            size=r.age[:30],       #Размер круга отображает возраст пользователя
                            colorscale='Viridis'   #Палитра цветов
                        ),
        text=r.device[:30]                        #Текст при наведении на круг - модель смартфона
    ))
    fig4.update_layout(
        title=dict(text='Screen On Time by users'),
        xaxis_title="Screen On Time by users",
        yaxis_title="User ID"
    )
    fig4.show()

    fig5 = go.Figure(data=[go.Scatter3d(    #График рассеяния в 3D
        x=r.app_us,                                  #Ось Х - время использования приложений
        y=r.num_app,                               #Ось У - количество приложений
        z=r.users,                                     #Ось Z - Порядковый номер пользователя
        mode='markers',
        marker=dict(
            size=r.age,                               #Размер отображает возраст пользователя
            color=r.data_us,                       #Цвет отображает количество использованных данных
            colorscale='RdBu'                      #Цветовая палитра
        )
    )])
    fig5.update_layout(
        scene=dict(                                   #Названия осей
            xaxis=dict(
                title=dict(
                    text='App Usage Time (min/day)'
                )
            ),
            yaxis=dict(
                title=dict(
                    text='Number of Apps Installed'
                )
            ),
            zaxis=dict(
                title=dict(
                    text='User ID'
                )
            ),
        ))
    fig5.show()                                    #Вывод график (вращается при помощи мыши)


def start_px_items():       #Функция запуска визуализаций "express"
    fig6 = px.bar(                                          #График "Столбцы"
        x=r.device[:25],                                    #Ось Х - модель смартфона
        y=r.users[:25],                                     #Ось У - порядковый номер пользователя
        hover_data=[r.gender[:25], r.age[:25]],   #Данные при наведении - пол и возраст
        color=r.data_us[:25],                           #Цвет отображает использование данных
        labels={                                             #Название надписей
            'x': 'Device Model',
            'y': 'User ID',
            'color': 'Data Usage (MB/day)',
            'hover_data_0': 'Gender',
            'hover_data_1': 'Age'
                }                                         #
    )
    fig6.show()

    fig7 = px.line(                                       #График "Линии"
        x=r.users[:17],                                  #Ось Х - Порядковый номер пользователя
        y=r.data_us[:17],                              #Ось У - использование данных
        color=r.gender[:17],                           #Цвет отображает пол
        title='Data Usage by users',                #Название графика
        hover_data=[r.device[:17], r.OS[:17]],   #Данные при наведении - модель смартфона и ОС
        labels={
            'x': 'User ID',
            'y': 'Data Usage (MB/day)',
            'color': 'Gender',
            'hover_data_0': 'Device Model',
            'hover_data_1': 'Operating System'
        }
    )
    fig7.show()

    fig8 = px.pie(                                                     #График "Пирог"
        values=r.num_app[:3],                                    #Количество приложений
        names=r.device[:3],                                         #Название смартфона
        title='Number of Apps Installed by devices',
        hole=.3,                                                                #Величина отверстия внутри графика
        color_discrete_sequence=px.colors.sequential.deep,    #Цветовая гамма
        hover_data=[r.OS[:3]],
        labels={'hover_data_0': 'Operating System'}
    )
    fig8.update_traces(
        textposition='inside',                          #Позиция текста - внутри
        textinfo='value',                                #Текст - количество приложений
        textfont_size=21                              #Размер букв
    )
    fig8.show()

    fig9 = px.scatter(                          #График рассеяния
        x=r.num_app,
        y=r.app_us,
        animation_frame=r.device,        #Кадр анимации - модель смартфона
        animation_group=r.users,         #Группа анимации - пользователи
        size=r.screen,                           #Размер отображает время работы экрана
        color=r.UBC,                             #Цвет отображает класс поведения пользователя
        log_x=True,  #Логарифмическое отображение
        log_y=True,  #по осям координат Х и У
        symbol=r.OS,                            #Форма отображает операционную систему
        facet_col=r.gender,                   #Деление графика на 2 по полу
        size_max=31,                          #Максимальный размер круга
        hover_data=[r.age],                  #Добавление данных при наведении
        labels={
                    'x': 'Number of Apps Installed',
                    'y': 'App Usage Time (min/day)',
                    'color': 'User Behavior Class',
                    'symbol': 'Operating System',
                    'hover_data_0': 'Age',
                    'facet_col': 'Gender',
                    'animation_frame': 'Device Model',
                    'size': 'Screen On Time (hours/day)'
                }
    )
    fig9.show()

    fig10 = px.scatter_3d(                #График рассеяния в 3D варианте
        x=r.num_app,
        y=r.app_us,
        z=r.age,                                 #Добавляется ось Z - возраст
        color=r.age,                            #Цвет отображает возраст
        size=r.UBC,                             #Размер отображает класс поведения пользователя
        size_max=40,
        hover_name=r.device,              #Информация при наведении - модель смартфона
        labels={
                        'x': 'Number of Apps Installed',
                        'y': 'App Usage Time (min/day)',
                        'z':'Age',
                        'color': 'Age',
                        'size': 'User Behavior Class',
                    }
    )
    fig10.show()
