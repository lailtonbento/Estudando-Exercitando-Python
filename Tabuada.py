num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:1} = {}'.format(num, c, num*c))
print('Tabuada encerrada! Volte sempre!')