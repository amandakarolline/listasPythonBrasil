"""
19) Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de
centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


def leia_numero():
    while True:
        try:
            numero = int(input('Digite uma nota: '))
        except ValueError:
            print("Você não digitou um número.")
        if numero < 1 or numero > 999:
            print('Digite um número entre 0 e 1000')
        else:
            break

    return numero


numero = leia_numero()

centena = numero//100
numero_dezena = numero - (centena*100)
dezena = numero_dezena//10
unidade = numero_dezena - (dezena*10)


if centena == 1:
    unidade_cent = 'centena'
elif centena > 1:
    unidade_cent = 'centenas'
else:
    unidade_cent = 'centenas'

if dezena == 1:
    unidade_deze = 'dezena'
elif dezena > 1:
    unidade_deze = 'dezenas'
else:
    unidade_deze = 'dezenas'

if unidade == 1:
    unidade_unit = 'unidade'
elif unidade > 1:
    unidade_unit = 'unidades'
else:
    unidade_unit = 'unidades'

if centena != 0:
    print(f'{numero} = {centena} {unidade_cent}, {dezena} {unidade_deze} e {unidade} {unidade_unit}')
elif dezena != 0:
    print(f'{numero} = {dezena} {unidade_deze} e {unidade} {unidade_unit}')
elif unidade != 0:
    print(f'{numero} = {unidade} {unidade_unit}')
else:
    print('0 unidades')
