# 2) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite um número: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero

numero = leia_numero()
if numero > 0:
    print('Número é positivo')
elif numero < 0:
    print('Número é negativo')
else:
    print("O número é 0")
