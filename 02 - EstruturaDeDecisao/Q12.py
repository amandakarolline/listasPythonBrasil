"""
12) Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
— Salário Bruto até 900 (inclusive) — isento
— Salário Bruto até 1500 (inclusive) — desconto de 5%
— Salário Bruto até 2500 (inclusive) — desconto de 10%
— Salário Bruto acima de 2500 — desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00


    Exemplo:
    >>> salario_bruto
    1100.0
    >>> IR
    55.0
    >>> inss
    110.0
    >>> fgts
    121.0
    >>> descontos
    165.0
    >>> salario_liquido
    935.0
"""


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
salario = dinheiro*horas

if salario > 2500:
    salario_bruto = salario
    IR = salario_bruto*0.20
elif salario > 1500:
    salario_bruto = salario
    IR = salario_bruto*0.10
elif salario > 900:
    salario_bruto = salario
    IR = salario_bruto*0.05
else:
    salario_bruto = salario
    IR = 0

inss = salario_bruto*0.10
fgts = salario_bruto*0.11
descontos = IR + inss
salario_liquido = salario_bruto-descontos

print(f'Salário Bruto: R$ {salario_bruto}\n'
      f'(-) IR (5%): R$ {IR}\n'
      f'(-) INSS (10%): R$ {inss}\n'
      f'FGTS: R$ {fgts}\n'
      f'Total de Descontos: R$ {descontos}\n'
      f'Salário Líquido: R$ {salario_liquido}')
