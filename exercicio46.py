n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
print('------------------------\n'
      '        M E N U         \n'
      '------------------------\n'
      '1. Somar\n'
      '2. Multiplicar\n'
      '3. Maior valor\n'
      '4. Entrar novos números\n'
      '5. Sair\n')
menu = int(input('Opção desejada: '))
while menu != 5:
      print('------------------------\n'
            '        M E N U         \n'
            '------------------------\n'
            '1. Somar\n'
            '1. Multiplicar\n'
            '3. Maior valor\n'
            '4. Entrar novos números\n'
            '5. Sair\n')
      if menu == 1:
            print(f'{n1} + {n2} = {n1 + n2}\n')

            menu = int(input('Opção desejada: '))
      elif menu == 2:
            print(f'{n1} x {n2} = {n1*n2}')
            print('------------------------\n'
                  '        M E N U         \n'
                  '------------------------\n'
                  '1. Somar\n'
                  '2. Multiplicar\n'
                  '3. Maior valor\n'
                  '4. Entrar novos números\n'
                  '5. Sair\n')
            menu = int(input('Opção desejada: '))
      elif menu == 3:
            if n1 > n2:
                  print(f'Maior valor: {n1}')

                  menu = int(input('Opção desejada: '))
            else:
                  print(f'Maior valor: {n2}')

                  menu = int(input('Opção desejada: '))
      elif menu == 4:
            n1 = int(input('Número 1: '))
            n2 = int(input('Número 2: '))

            menu = int(input('Opção desejada: '))