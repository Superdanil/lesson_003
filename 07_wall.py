# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

sd.resolution = (1600, 900)

#определяем размеры кирпича
brick_lenght = 100
brick_height = 50

#определим функцию рисования нижней горизонтальной линии

def draw_horizontal_line():
    point1 = sd.get_point(0, y + brick_height)
    point2 = sd.get_point(sd.resolution[0], y + brick_height)
    sd.line(point1, point2)


# вызовем функцию через цикл в зависимости от высоты окна и высоты кирпича

for y in range (0, sd.resolution[1], brick_height):
    draw_horizontal_line()

#определим функцию рисования двух вертикальных линий слева снизу

def draw_vertical_lines():
    point11 = sd.get_point(x+ brick_lenght/2, y)
    point12 = sd.get_point(x + brick_lenght/2, y + brick_height)
    sd.line(point11, point12)
    point21 = sd.get_point(x + brick_lenght, y + brick_height)
    point22 = sd.get_point(x + brick_lenght, y + 2 * brick_height)
    sd.line(point21, point22)


# вызовем функцию через цикл в зависимости от размеров окна и размеров кирпича

for y in range(0, sd.resolution[1], brick_height*2):
    for x in range (0, sd.resolution[0], brick_lenght):
        draw_vertical_lines()

sd.pause()
