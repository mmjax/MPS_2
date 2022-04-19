import numpy
from tabulate import tabulate
from DecisionHelper import DecisionHelper


name = ['Pycharm', 'VScode', 'Replit']
har = [
    'Эфективность', 'Переносимость',
    'Защищонность', 'Доступность', 'Функционал'
]
data = numpy.array(
    [[32, 53.4, 68.9, 67, 94.3],
     [29, 84.6, 73.4, 93, 75.7],
     [51, 79.8, 78.7, 78, 83.9]]
    )
weigh = [0.1, 0.1, 0.1, 0.3, 0.4]

dh = DecisionHelper(data, weigh, name)
print("Исходная таблица\n", tabulate(data, headers=har, showindex=name))
dh.saw()
dh.electre()
dh.topsis()

'''
[[4, 43.4, 44.9, 22, 56.3],
     [3, 50.6, 35.4, 23, 63.7],
     [5, 62.8, 40.7, 21, 74.9]]

     [0.2, 0.1, 0.3, 0.3, 0.1]
'''