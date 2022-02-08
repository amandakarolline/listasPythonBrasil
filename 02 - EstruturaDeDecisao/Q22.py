"""
22) Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""

def leia_numero():
    while True:
        try:
            numero = int(input('Digite um número: '))
        except ValueError:
            print("Você não digitou um número inteiro.")
        else:
            break

    return numero

numero = leia_numero()

if numero % 2 == 0:
    print('Número é par')
else:
    print('Número é ímpar')
