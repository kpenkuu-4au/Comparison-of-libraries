from items import matplotlib_items as plt_items
from items import seaborn_items as sns_items
from items import plotly_items as p_items


def choice_items():
    while True:
        print('\t ______________________________________', sep='', end='\n')
        print('\t| Выберите серию примеров визуализаций |')
        print(
            '\t \\   -> Matplotlib <- (введите "1")   /\n'
            '\t  \\   -> Seaborn <-  (введите "2")   /\n'
            '\t   \\   -> Plotly <- (введите "3")   /\n'
            '\t    \\   Для завершения введите "0" /\n'
            '\t     \\____________________________/\n\n'
        )
        try:
            vote = int(input('Ваш выбор -> '))
            if vote == 1:
                print("После ознакомления с графиком закройте окно")
                print("Дождитесь окончания анимации!")
                plt_items.start_plt_items()
            elif vote == 2:
                print("После ознакомления с графиком закройте окно")
                sns_items.start_sns_items()
            elif vote == 3:
                while True:
                    print("Выберите вариант визуализаций:")
                    print("Plotly Express (введите '1')")
                    print("Plotly Graph Objects (введите '2')")
                    print("Назад к меня введите '0")
                    try:
                        vote = int(input('Ваш выбор -> '))
                        if vote == 1:
                            print("Визуализации графиков отобразятся в браузере")
                            p_items.start_px_items()
                            break
                        elif vote == 2:
                            print("Визуализации графиков отобразятся в браузере")
                            p_items.start_go_items()
                            break
                        elif vote == 0:
                            break
                        else:
                            print("Неверное значение, попробуйте еще раз")
                    except ValueError:
                        print('Значение неверное, повторите ввод')

            elif vote == 0:
                print('\n         -->   Спасибо за просмотр  <--')
                break
            else:
                print("Неверное значение, попробуйте еще раз")
        except ValueError:
            print('Значение неверное, повторите ввод')


choice_items()
