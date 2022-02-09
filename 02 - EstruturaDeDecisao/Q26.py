"""
26) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
o preço do litro do álcool é R$ 1,90.
"""


def leia_numero():
    while True:
        try:
            numero = float(input('Digite a quantidade de litros de combustível: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


def tipo_combustivel():
    while True:
        tipo = input('Digite o tipo de combustível A-álcool, G-gasolina: ')
        tipo = tipo.upper()
        if tipo != 'A' and tipo != 'G':
            print('Digite A ou G!')
        else:
            break

    return tipo


combustivel = tipo_combustivel()
litros = leia_numero()

if litros > 20:
    preco_gasolina = 2.50 * 0.94
    preco_alcool = 1.90 * 0.95
else:
    preco_gasolina = 2.50 * 0.96
    preco_alcool = 1.90 * 0.97

if combustivel == 'A':
    total = litros * preco_alcool
    print(f'Você deve pagar R$ {total}.')
else:
    total = litros * preco_gasolina
    print(f'Você deve pagar R$ {total}.')
