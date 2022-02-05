# 9) Faça um Programa que leia três números e mostre-os em ordem decrescente.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite um preço: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


numero1 = leia_numero()
numero2 = leia_numero()
numero3 = leia_numero()
ordenados = sorted([numero1, numero2, numero3])

print(ordenados[::-1])
