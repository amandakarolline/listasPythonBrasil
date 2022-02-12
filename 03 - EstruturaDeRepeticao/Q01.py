"""
1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""

while True:
    try:
        numero = int(input('Digite uma nota: '))
    except ValueError:
        print("Você não digitou um número.")
    if numero < 0 or numero > 10:
        print("Digite uma nota de 0 até 10.")
    else:
        print(f'A nota foi {numero}')
        break
