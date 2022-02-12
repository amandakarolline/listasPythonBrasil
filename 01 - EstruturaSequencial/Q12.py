"""
12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
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


altura = leia_numero()
peso = (72.7*altura)-58

print(f'O seu peso ideal é {peso}')
