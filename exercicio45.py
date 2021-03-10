import random
sorteio = random.randint(0, 10)
valor = int(input('Qual o valor sorteado (entre 0 e 10)? '))
tentativas = 0

while valor != sorteio:
    if valor != sorteio:
        print('Incorreto.')
        valor = int(input('Qual o valor sorteado (entre 0 e 10)? '))
        tentativas += 1
else:
    tentativas += 1
    print(f'Você acertou o número sorteado pelo computador {sorteio}, em {tentativas} tentativas')