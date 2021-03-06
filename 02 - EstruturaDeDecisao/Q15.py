"""
15) Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""


def leia_numero():
    while True:
        try:
            numero = float(input('Digite o valor do lado: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


l1 = leia_numero()
l2 = leia_numero()
l3 = leia_numero()

if (l1+l2 > l3) and (l1+l3 > l2) and (l2+l3 > l1):
    print('É um triângulo!')
    if l1 == l2 == l3:
        print('Triângulo Equilátero!')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isósceles!')
else:
    print('Não é um triângulo!')
