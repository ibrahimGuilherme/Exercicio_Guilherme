pessoas = [[1, 'Ibrahim Guilheme Morais de Oliveira1', 'São Paulo do Potengi1', 'RN'],
           [2, 'Ibrahim Guilheme Morais de Oliveira2', 'São Paulo do Potengi2', 'RA'],
           [3, 'Ibrahim Guilheme Morais de Oliveira3', 'São Paulo do Potengi3', 'RB'],
           [4, 'Ibrahim Guilheme Morais de Oliveira4', 'São Paulo do Potengi4', 'RC'],
           [5, 'Ibrahim Guilheme Morais de Oliveira5', 'São Paulo do Potengi5', 'RD']]

arq = open('convidados.txt', 'w')
print(f'lendo o arquivo convidados.txt\n'
f'{"-"*50}')
for pessoa in pessoas:

    codigo = pessoa[0]
    nome = pessoa[1]
    cidade = pessoa[2]
    estado = pessoa[3]

    registro = f'O convidado {codigo}, cujo o nome é {nome} mora em {cidade}/{estado}'
    print(registro)

    arq.write(registro)

arq.close()