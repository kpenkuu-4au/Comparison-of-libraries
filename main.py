from items import (matplotlib_items as plt_items,
                   seaborn_items as sns_items)


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
            elif vote == 0:
                print('Спасибо за просмотр')
                break
        except ValueError:
            print('Значение неверное, повторите ввод')


choice_items()
