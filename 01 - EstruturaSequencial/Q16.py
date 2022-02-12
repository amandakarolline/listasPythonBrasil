"""
16) Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math


def leia_numero():
    while True:
        try:
            numero = float(input('Digite a área em m² que deseja pintar: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


area = leia_numero()
litros = math.ceil(area/3)
latas = math.ceil(litros/18)
preco = latas*80

print(f'Será preciso comprar {latas} latas de tinta que custarão R$ {preco},00')
