# Desafio 2

from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogo = {
    jogador1 : randint(1,6),
    jogador2 : randint(1,6),
    jogador3 : randint(1,6),
    jogador4 : randint(1,6),
}
print('Valoes Sorteados: ')
for k, v in jogo.itens():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-='*30)

ranking = sorted(jogo.items(),key itemgetter(1), reverse=True)
print('================= Ranking dos jogadores =================')
for i, v in enumerate(ranking):
    print(f'(i+1)°Lugar: {v[0]}com {v[1]} no dado')
sleep(1)
print('-='*30)



