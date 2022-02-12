"""4) Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
while True:

    letra = input('Digite uma letra: ')
    letra = letra.upper()

    if len(letra) > 1:
        print('Digite apenas uma letra')
    elif letra in vogais:
        print(f'{letra} é uma vogal')
        break
    elif letra in consoantes:
        print(f'{letra} é uma consoante')
        break
    else:
        print(f'{letra} não é uma vogal e nem uma consoante')
        break
