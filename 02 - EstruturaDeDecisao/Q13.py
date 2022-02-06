"""
13) Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1 – Domingo, 2 – Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

"""
def leia_numero():
    while True:
        try:
            numero = int(input(f'Digite um número referente ao dia da semana 1-Domingo etc.: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


semana = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
dia = leia_numero()

if dia in semana:
    print(semana[dia])
else:
    print('Valor inválido')
