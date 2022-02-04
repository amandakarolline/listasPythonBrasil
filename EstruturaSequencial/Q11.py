# 11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

def leia_inteiro():
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
        except ValueError:
            print("Você não digitou um número inteiro.")
        else:
            break

    return numero


def leia_real():
    while True:
        try:
            numero = float(input('Digite um número real: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero

numero1 = leia_inteiro()
numero2 = leia_inteiro()
numero3 = leia_real()

a = (2*numero1)*(numero2/2)
b = (3*numero1)+numero3
c = numero3**3

print(f'a) {a}')
print(f'b) {b}')
print(f'c) {c}')