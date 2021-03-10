print('Realize a doma dos números desejados, entre 0 e 998.\n'
      'Para finalizar a soma digite 999.\n')
soma = 0
valor = 0
num = 0

while True:
      if num != 999:
            num = int(input('Digite um número: '))
            soma += num
            valor += 1
      else:
            soma -= num
            valor -= 1
            print(f'Foram digitados {valor} valores, sendo a soma deles {soma}.')
            break