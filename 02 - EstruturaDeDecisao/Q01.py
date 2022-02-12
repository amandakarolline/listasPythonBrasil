"""1) Faça um Programa que peça dois números e imprima o maior deles."""

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
maior = max(numero1,numero2)

print(f'O maior número é {maior}')