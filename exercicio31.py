from datetime import datetime
now = datetime.now()
anoNas = int(input('Qual o seu ano de nascimento? '))
if now.year - anoNas == 18:
    print('Esse é o seu ano de alistamento.')
elif now.year - anoNas < 18:
    print(f'Você irá se alistar dentro de {18-(now.year - anoNas)} anos')
else:
    print(f'já passou o seu tempo de alistamento em {now.year - anoNas - 18} anos')