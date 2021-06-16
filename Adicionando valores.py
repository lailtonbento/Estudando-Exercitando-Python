valores = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Erro em adicionar.')
    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')
