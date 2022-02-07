"""
16) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
o programa não deve fazer pedir os demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math


def leia_numero(a):
    while True:
        try:
            numero = float(input(f'Digite digite o valor de {a}: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


a = leia_numero('a')
b = leia_numero('b')
c = leia_numero('c')
delta = (b**2)-4*a*c
if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a

if a == 0:
    print('Não é uma equação do 2º grau!')
elif delta < 0:
    print('Não possui raizes reais')
elif delta == 0:
    print(f'Só possui uma raiz: x = {x1}')
else:
    print(f'As raízes são: x1 = {x1} e x2 = {x2}')
