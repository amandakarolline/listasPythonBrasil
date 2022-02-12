"""
8) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

def leia_numero():
    while True:
        try:
            numero = float(input('Digite um preço: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


numero1 = leia_numero()
numero2 = leia_numero()
numero3 = leia_numero()
menor = min(numero1, numero2, numero3)

print(f'O menor preço é {menor:,.2f}')
