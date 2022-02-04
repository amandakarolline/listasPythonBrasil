# 15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o salarioBruto do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.

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
salarioBruto = dinheiro * horas
IR = salarioBruto*0.11
INSS = salarioBruto*0.08
sindicato = salarioBruto*0.05
descontos = IR+INSS+sindicato
salarioLiquido = salarioBruto - descontos

print(f'a) Seu Salário Bruto é {salarioBruto} por mês.\n')
print(f'b) Você paga {INSS} de INSS por mês.\n')
print(f'c) Você paga {sindicato} de sindicato por mês.\n')
print(f'd) Você recebe {salarioLiquido} de salário líquido por mês.\n')
print(f'e) Tabela\n'
      f'+ Salário Bruto : R$ {salarioBruto}\n'
      f'- IR (11%) : R$ {IR}\n'
      f'- INSS (8%) : R$ {INSS}\n'
      f'- Sindicato (5%) : R$ {sindicato}\n'
      f'= Salário Liquido : R$ {salarioLiquido}\n')
