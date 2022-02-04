# 9) Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def leia_numero():
    while True:
        try:
            numero = float(input('Digite a temperatudo em graus Fahrenheit: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


F = leia_numero()
C = 5*((F-32)/9)

print(f'A temperatura é {C}ºC')
