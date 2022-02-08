"""
24) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a) par ou ímpar;
b) positivo ou negativo;
c) inteiro ou decimal.
"""


def leia_numero():
    while True:
        try:
            numero = float(input('Digite um número: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


num1 = leia_numero()
num2 = leia_numero()

while True:
    operador = input('Digite qual operação você deseja fazer (+,-,*,/): ')

    if operador == '+':
        resultado = num1 + num2
        break
    elif operador == '-':
        resultado = num1 - num2
        break
    elif operador == '*':
        resultado = num1 * num2
        break
    elif operador == '/':
        resultado = num1 / num2
        break
    else:
        print('Operador inválido.')

print(f'O resultado é: {resultado}')

if resultado % 2 == 0:
    print('Par')
else:
    print('Ímpar')

if resultado > 0:
    print('Positivo')
elif resultado == 0:
    print('0, nem positivo e nem negativo')
else:
    print('Negativo')

if resultado % 1 == 0:
    print('Inteiro')
else:
    print('Decimal')