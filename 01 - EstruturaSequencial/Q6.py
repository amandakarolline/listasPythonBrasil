# 6) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite o raio: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


raio = leia_numero()
pi = 3.1415
area = pi*raio**2

print(f'A área do raio é {area}')
