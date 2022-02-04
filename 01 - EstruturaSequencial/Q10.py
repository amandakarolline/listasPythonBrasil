# 10) Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite a temperatudo em graus Celsius: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


C = leia_numero()
F = 32+(9*C/5)

print(f'A temperatura é {F}ºF')
