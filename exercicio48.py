opcao = ''
maiorDeIdade = 0
homens = 0
sexo = ''
mulheres21 = 0
while opcao != 'N':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: ')).upper()
    opcao = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper()

    if idade >= 18:
        maiorDeIdade += 1
    if sexo == 'H':
        homens += 1
    if sexo == 'M':
        if idade > 21:
            mulheres21 += 1

print(f'Pessoas maiores de idade: {maiorDeIdade}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com mais de 21 anos: {mulheres21}')