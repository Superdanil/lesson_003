# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

sd.resolution = (1200, 600)
def line(step):
    x1 = 50
    x2 = 350
    i = 0
    for x1 in range (0, step * 7, step):
        point1 = sd.get_point(x1 + step, 50)
        point2 = sd.get_point(x2 + step * i, 450)
        sd.line(point1, point2, width = 4, color = rainbow_colors[i])
        i += 1
line(step = 5)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

def rainbow (point, step):
    radius = 60
    i = 0
    for _ in range(7):
        radius += step
        sd.circle(point, radius=radius, width=40, color = rainbow_colors[i])
        i += 1
point = sd.get_point(sd.resolution[0]/2, 0)

rainbow(point, 40)


sd.pause()
