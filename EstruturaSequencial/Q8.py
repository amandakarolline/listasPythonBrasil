# 8) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o salarioBruto do seu salário no referido mês.

def leia_numero(valor='numero'):
    while True:
        try:
            numero = float(input(f'Digite o {valor}: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


dinheiro = leia_numero('salario por hora')
horas = leia_numero('número de horas por mês')
total = dinheiro*horas

print(f'Você recebe {total} por mês.')
