ano = int(input('Digite um ano: '))
if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
    print('\033[31mEsse ano é bissexto')
else:
    print('\033[35mEsse ano não é bissexto')