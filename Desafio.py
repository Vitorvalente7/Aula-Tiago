import time
from random import randint

lista = []
jogos = []
cont = 0
print('-='*8,'Jogo da mega sena','-='*8)

quant = int(input('Quantos jogos voce deseja fazer ? \nR: '))
total = 1
while total <= quant:
    cont = 0 
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1 
        
print('-='*6,f'Sorteando {quant} jogos','-='*6)
for i, n in enumerate(jogos):
    time.sleep(1)
    print(f'{i+1}° jogo {n}')
time.sleep(1)
print('-='*6,f'Sorteando {quant} jogos','-='*6)
          