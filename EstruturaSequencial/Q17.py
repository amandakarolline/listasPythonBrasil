# 17) Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# — comprar apenas latas de 18 litros;
# — comprar apenas galões de 3,6 litros;
# — misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Sempre arredonde os valores para cima, isto é, considere latas cheias.

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
litros = math.ceil(area/6)
latas = math.ceil(litros/18)
galoes = math.ceil(litros/3.6)
preco_latas = latas*80
preco_galoes = galoes*25
latas2 = math.floor(litros/18)
residuo = (litros/18) - latas2
galoes2 = math.ceil((residuo*18)/3.6)
preco_latas2 = latas2*80
preco_galoes2 = galoes2*25
total = preco_galoes2+preco_latas2
litros_totais = (latas2*18)+(galoes2*3.6)

print(f'Será preciso comprar {latas} latas de tinta que custarão R$ {preco_latas},00 um total de {latas*18} litros')
print(f'Será preciso comprar {galoes} galões de tinta que custarão R$ {preco_galoes},00 um total de {galoes*3.6} litros')
print(f'Você pode utilizar {latas2} latas e {galoes2} galões e gastar R$ {total},00 um total de {litros_totais} litros')