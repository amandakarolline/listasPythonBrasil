# 7) Faça um Programa que leia três números e mostre o maior e o menor deles.

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
numero3 = leia_numero()
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
