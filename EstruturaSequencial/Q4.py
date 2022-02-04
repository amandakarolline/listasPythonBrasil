# 4) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite um número: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


nota1 = leia_numero()
nota2 = leia_numero()
nota3 = leia_numero()
nota4 = leia_numero()
soma = nota1 + nota2 + nota3 + nota4
media = soma/4

print(f'A média é {media}')
