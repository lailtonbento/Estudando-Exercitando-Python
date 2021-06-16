valores = list()
impares = list()
pares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 ==0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')