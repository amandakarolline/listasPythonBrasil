"""
13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
"""

def leia_numero():
    while True:
        try:
            numero = float(input('Digite sua altura: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


h = leia_numero()

while True:
    sexo = input('Digite o F para feminino e M para masculino: ')
    sexo = sexo.upper()

    if sexo == 'M':
        peso = (72.7*h)-58
        break
    elif sexo == 'F':
        peso = (62.1*h) - 44.7
        break
    else:
        pass

print(f'O seu peso ideal é {peso}')
