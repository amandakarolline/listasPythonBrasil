# 18) Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def leia_numero(valor='numero'):
    while True:
        try:
            numero = float(input(f'Digite {valor}: '))
        except ValueError:
            print("Você não digitou um número.")
        else:
            break

    return numero


arquivo = leia_numero('o tamanho do arquivo (em MB)')
velocidade = leia_numero('a velocidade de download (em Mbps)')

tempo = arquivo/(velocidade*60)

print(f'O download demorará aproximadamente {tempo} minutos')