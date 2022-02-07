"""
20) Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c) A mensagem "Aprovado com Distinção", se a média for igual a 10.
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
nota3 = leia_numero()
media = (nota1+nota2+nota3)/3

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print(f'Aprovado! Com média: {media}')
else:
    print(f'Reprovado! Com média: {media}')