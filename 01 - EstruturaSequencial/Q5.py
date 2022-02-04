# 5) Faça um Programa que converta metros para centímetros.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite um número em metros: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


metros = leia_numero()
centimetros = metros*100

print(f'{metros}m = {centimetros}cm')
