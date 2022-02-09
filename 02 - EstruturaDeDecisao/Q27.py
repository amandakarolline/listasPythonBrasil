"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 kg           Acima de 5 kg
Morango         R$ 2,50 por kg          R$ 2,20 por kg
Maçã            R$ 1,80 por kg          R$ 1,50 por kg
Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em kg) de morangos
e a quantidade (em kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""


def fruta(fruta):
    while True:
        try:
            numero = float(input(f'Digite o peso em kg - {fruta}: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


morango = fruta('morango')
maca = fruta('maçã')
peso_total = morango + maca

if morango > 5:
    preco_morango = morango * 2.2
else:
    preco_morango = morango * 2.5
if maca > 5:
    preco_maca = maca * 1.5
else:
    preco_maca = maca * 1.8

total = preco_morango + preco_maca

if peso_total > 8 or total > 25:
    total = total * 0.9
    print(f'Valor a ser pago: R$ {total}')
else:
    print(f'Valor a ser pago: {total}')
