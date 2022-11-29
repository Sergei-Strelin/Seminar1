# 5.Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input('Введите координату Х для первой точки: '))
y1 = int(input('Введите координату Y для первой точки: '))
x2 = int(input('Введите координату Х для второй точки: '))
y2 = int(input('Введите координату Y для второй точки: '))

d = (((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5)
print('Расстояние между двумя точками: ', (int (d*100))/100)