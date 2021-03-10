import random
n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')

lista = n1, n2, n3
sorteio = random.choice(lista)

print(f'Escolhido: {sorteio}')