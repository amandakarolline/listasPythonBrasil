# 5) Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# — A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# — A mensagem "Reprovado", se a média for menor que sete;
# — A mensagem "Aprovado com Distinção", se a média for igual a dez.

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

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
