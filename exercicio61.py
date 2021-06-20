n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

d1 = {1:n1, 2:n2, 3:n3}

print(f'Selecione a nota que será cancelada \n'
      f'{d1[1]:.2f}\n'
      f'{d1[2]:.2f}\n'
      f'{d1[3]:.2f}\n')
n = int(input('[1/2/3]: '))
if n == 1:
    del(d1[1])
    media = (d1[2] + d1[3]) / 2
if n == 2:
    del (d1[2])
    media = (d1[1] + d1[3]) / 2
if n == 3:
    del (d1[3])
    media = (d1[1] + d1[2]) / 2

print(f'Média = {media:.2f}')