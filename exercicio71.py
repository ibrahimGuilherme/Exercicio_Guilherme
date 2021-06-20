def alterar_linha(path,index_linha,nova_linha):
    with open(path, 'r') as f:
        texto = f.readlines()
    with open(path, 'w') as f:
        for i in texto:
            if texto.index(i) == index_linha:
                f.write(nova_linha+'\n')
            else:
                f.write(i)

def encontrar_strin(path,string):
    with open(path, 'r') as f:
        texto = f.readlines()
    for i in texto:
        if string in i:
            print(texto.index(i))
            return
    print('String não encontrada')


print('='*50, '\n',
      'Agenda de telefones e e-mails\n',
      '='*50, '\n',
      '1. Listar seus contatos'
      '2. Ver dados de um contato'
      '3. Incluir um contato'
      '4. Apagar um contato'
      '5. Sair')

opcao = int(input('Qual sua opção[1/2/3/4/5]? '))
while True:
    if opcao == 1:
        arq = open('agenda.txt', 'r')
        for x in arq.readline():
            print('Código: ')
            print(x)
            print('Nome: ')
            print(x)
        arq.close()
    if opcao == 2