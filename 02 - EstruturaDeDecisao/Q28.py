"""
28) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 kg           Acima de 5 kg
File Duplo      R$ 4,90 por kg          R$ 5,80 por kg
Alcatra         R$ 5,90 por kg          R$ 6,80 por kg
Picanha         R$ 6,90 por kg          R$ 7,80 por kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
carnes = ['File Duplo', 'Alcatra', 'Picanha']


def tipo_carne():
    global opcao
    while True:
        try:
            for i, a in enumerate(carnes):
                print(f'{i+1} - {a}')
            opcao = int(input('Digite um número da carne escolhida: '))
        except ValueError:
            print("Você não digitou um número.")
        if opcao < 1 or opcao > 3:
            print("Opção Inválida.")
        else:
            break

    return opcao


def leia_quilos():
    while True:
        try:
            numero = float(input('Digite a quantidade de carne que deseja, em kg: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


def forma_pagamento():
    global pagamento
    while True:
        try:
            pagamento = input('Você vai pagar com cartão Tabajara: S/N: ')
            pagamento = pagamento.upper()
        except ValueError:
            print("Você não digitou um número.")
        if pagamento != 'S' and pagamento != 'N':
            print('Opção inválida.')
        else:
            break

    return pagamento


maior_5 = {1: 5.8, 2: 6.8, 3: 7.8}
ate_5 = {1: 4.9, 2: 5.9, 3: 6.9}
carne = tipo_carne()
quilos = leia_quilos()
pag = forma_pagamento()
desconto = 0

if quilos > 5:
    preco_carne = maior_5[carne] * quilos
else:
    preco_carne = ate_5[carne] * quilos
if pag == 'S':
    desconto = preco_carne*0.05
total = preco_carne - desconto

print(f'CUPOM FISCAL\n'
      f'{carnes[carne-1]} ----- {quilos}kg ----- RS {preco_carne}\n'
      f'Forma de pagamento Cartão Tabajara? {pag}\n'
      f'Desconto: R$ {desconto: .2f}\n'
      f'Total a Pagar: R$ {total: .2f}')
