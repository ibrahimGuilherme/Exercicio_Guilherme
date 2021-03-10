sexo = input('Digite seu sexo [M/F]: ').upper()
while True:
    if sexo == 'M':
        print('O sexo escolhido foi o Masculino')
        break
    elif sexo == 'F':
        print('O sexo escolhido foi o Feminino')
        break
    else:
        sexo = input('Digite seu sexo [M/F]: ').upper()