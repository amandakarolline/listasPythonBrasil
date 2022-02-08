"""
25) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""


def pergunta(a):
    global resp
    while True:
        try:
            resp = input(f'{a} S/N: ')
            resp = resp.upper()
        except ValueError:
            print('Valor inválido')
        if resp != 'S' and resp != 'N':
            print('Valor inválido')
        else:
            break
    return resp


perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?",
             "Já trabalhou com a vítima?"]
s = 0
for a in perguntas:
    resp = pergunta(a)
    if resp == 'S':
        s += 1

if s == 2:
    print('Suspeita')
elif s == 3 or s == 4:
    print('Cúmplice')
elif s == 5:
    print('Assassino')
else:
    print('Inocente')
