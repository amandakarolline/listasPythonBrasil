# 3) Faça um Programa que peça dois números e imprima a soma.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite um número: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


numero1 = leia_numero()
numero2 = leia_numero()
soma = numero1+numero2

print(f'A soma é {soma}')
