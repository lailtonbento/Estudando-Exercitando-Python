num = 0
while True:
    num = int(input('Digite um número para ver a sua tabuada: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print('{} x {:1} = {}'.format(num, c, num*c))
    print('-' * 30)
print('Tabuada encerrada! Volte sempre!')