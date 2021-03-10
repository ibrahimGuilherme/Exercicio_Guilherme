n1 = float(input('Nota mensal: '))
n2 = float(input('Nota bimestral: '))

media = (n1+n2)/2

if media < 5:
    print(f'Reprovado - Média {media:.1f}')
elif media >= 5 and media <= 6.9:
    print(f'Em recuperação - Média {media:.1f}')
else:
    print(f'Aprovado - Média {media:.1f}')