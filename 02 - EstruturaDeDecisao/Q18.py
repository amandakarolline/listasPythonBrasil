"""
18) Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""


def leia_dia():
    while True:
        try:
            numero = int(input('Digite um dia: '))
        except ValueError:
            print('Você não digitou um número.')
        if numero < 0 or numero > 31:
            print('Dia não é válido')
        elif numero > maxdias[mes]:
            print('Esse dia não existe no mês digitado')
        else:
            break

    return numero


def leia_mes():
    while True:
        try:
            mes = input('Digite um mês: ')
        except ValueError:
            print("Você não digitou um número.")
        if mes not in maxdias.keys():
            print('Mês não é válido')
        else:
            break

    return mes


def leia_ano():
    while True:
        try:
            numero = int(input('Digite um ano: '))
        except ValueError:
            print("Você não digitou um número.")
        if numero < 100:
            print('Formato do ano não é válido')
        else:
            break

    return numero


maxdias = {'01': 31, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
mes = leia_mes()
dia = leia_dia()
ano = leia_ano()
print(f'Data válida: {dia}/{mes}/{ano}')