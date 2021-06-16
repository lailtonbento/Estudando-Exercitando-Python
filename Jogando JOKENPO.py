from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('Computador jogou {}.'.format(itens[computador]))
print('Você jogou {}.'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:              #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O jogador venceu!')
    elif jogador == 2:
        print('O computador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:           #COMPUTADOR JGOOU PAPEL
    if jogador == 0:
        print('O computador venceu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O jogador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:           #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('O jogador venceu!')
    elif jogador == 1:
        print('O computador venceu!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
