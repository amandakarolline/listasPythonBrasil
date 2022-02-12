"""
14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

def leia_numero():
    while True:
        try:
            numero = float(input('Digite o peso do peixe: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


peso = leia_numero()

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O peixe tem {excesso:,.2f}kg além do limite e você deve pagar uma multa de R$ {multa:,.2f}')
else:
    print('O peixe está dentro do peso estabelecido e você não tem que pagar multa')
