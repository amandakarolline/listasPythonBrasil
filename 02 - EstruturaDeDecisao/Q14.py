"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0         A
  Entre 7.5 e 9.0          B
  Entre 6.0 e 7.5          C
  Entre 4.0 e 6.0          D
  Entre 4.0 e zero         E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

def leia_numero():
    while True:
        try:
            numero = float(input('Digite uma nota: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


nota1 = leia_numero()
nota2 = leia_numero()
media = (nota1+nota2)/2

if media > 9:
    conceito = 'A'
    situacao = 'Aprovado'
elif media > 7.5:
    conceito = 'B'
    situacao = 'Aprovado'
elif media > 6:
    conceito = 'C'
    situacao = 'Aprovado'
elif media > 4:
    conceito = 'D'
    situacao = 'Reprovado'
else:
    conceito = 'E'
    situacao = 'Reprovado'

print(f'Nota 1: {nota1}\n'
      f'Nota 2: {nota2}\n'
      f'Média: {media}\n'
      f'Conceito: {conceito}\n'
      f'Situação: {situacao}')
