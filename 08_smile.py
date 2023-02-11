# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

from random import randint


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x, y, color):
    radius = 50
    # x = randint(0 + radius, 600 - radius)
    # y = randint(0 + radius, 600 - radius)
    point = sd.get_point(x, y)
    sd.circle(point, radius=radius, width=2, color=color)
    left_eye = sd.get_point(x - 20, y + 10)
    right_eye = sd.get_point(x + 20, y + 10)
    eye_radius = 5
    mouth = sd.get_point(x, y - 20)
    mouth_radius = 10
    sd.circle(left_eye, radius=eye_radius, width=1, color=color)
    sd.circle(right_eye, radius=eye_radius, width=1, color=color)
    sd.circle(mouth, radius=mouth_radius, width=1, color=color)


smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())
smile(x=randint(0, 600), y=randint(0, 600), color=sd.random_color())

sd.pause()
