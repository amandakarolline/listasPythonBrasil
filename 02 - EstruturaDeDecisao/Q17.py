"""
17) Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.

Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto:
por exemplo, 1988, 1992 e 1996 são anos bissextos.
No entanto, ainda há um pequeno erro que deve ser contabilizado.
Para eliminar esse erro, o calendário gregoriano estipula que um ano que é uniformemente divisível por 100
(por exemplo, 1900) é um ano bissexto apenas se também é igualmente divisível por 400.
Por essa razão, os seguintes anos não são bissextos:
1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600:
Isso porque eles são uniformemente divisíveis por 100, mas não por 400.
Os seguintes anos são bissextos: 1600, 2000, 2400
Isso porque eles são uniformemente divisíveis por 100 e 400.
"""


def leia_numero():
    while True:
        try:
            numero = int(input('Digite uma nota: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


ano = leia_numero()
if ano % 400 == 0:
    print('É um ano bissexto')
elif ano % 100 == 0:
    print('Não é um ano bissexto')
elif ano % 4 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')
