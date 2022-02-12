"""2) Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]."""

while True:
    try:
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print("Você não digitou um número inteiro.")
    else:
        break

print(f'O número informado foi {numero}')
