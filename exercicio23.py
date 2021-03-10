import random
n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5
lista = n1, n2, n3, n4, n5, n6
sorteio = random.choice(lista)
ns = int(input('Qual o número sorteado (entre 0 e 5)? '))
if ns == sorteio:
    print(f'Você acertou! O número {ns} é o mesmo que o sorteado {sorteio}')
else:
    print(f'Você errou! O número {ns} não é o sorteado {sorteio}')
