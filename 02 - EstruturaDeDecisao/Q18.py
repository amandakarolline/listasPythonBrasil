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
        elif mes == '02' and (anoBissexto(ano) == True):
            if numero > 29:
                print('Esse dia não existe no mês digitado')
            else:
                break
        elif mes == '02' and (anoBissexto(ano) == False):
            if numero > 28:
                print('Esse dia não existe no mês digitado')
            else:
                break
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


def anoBissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

maxdias = {'01': 31, '02':29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
ano = leia_ano()
mes = leia_mes()
dia = leia_dia()
print(f'Data válida: {dia}/{mes}/{ano}')
