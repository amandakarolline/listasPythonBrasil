# 7) Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def leia_numero():
    while True:
        try:
            numero = float(input('Digite o lado do quadrado: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


lado = leia_numero()
area = lado**2
dobro_area = 2*area

print(f'A área é {area}')
print(f'O dobro da área é {dobro_area}')