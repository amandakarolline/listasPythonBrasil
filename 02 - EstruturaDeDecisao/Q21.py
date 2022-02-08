"""
21) Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a) Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b) Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""


def leia_numero():
    while True:
        try:
            numero = int(input('Digite o valor que deseja sacar no mínimo 10 e no máximo 600: '))
        except ValueError:
            print("Você não digitou um número.")
        if numero < 10 or numero > 600:
            print("Valor não disponível")
        else:
            break

    return numero


valor = leia_numero()

cem = valor // 100
valor_cinquenta = valor - (cem*100)
cinquenta = valor_cinquenta // 50
valor_dez = valor_cinquenta - (cinquenta*50)
dez = valor_dez // 10
valor_cinco = valor_dez - (dez*10)
cinco = valor_cinco // 5
um = valor_cinco - (cinco*5)

if cem != 0:
    print(f'R$ 100,00: {cem}')
if cinquenta != 0:
    print(f'R$ 50,00: {cinquenta}')
if dez != 0:
    print(f'R$ 10,00: {dez}')
if cinco != 0:
    print(f'R$ 5,00: {cinco}')
if um != 0:
    print(f'R$ 1,00: {um}')
