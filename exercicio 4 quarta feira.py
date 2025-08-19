num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um numero: ')))
    resp = input('Quer continuiar? [S/N]: ')
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é: {num}')
print(f'A lista completa é: {pares}')
print(f'A lista completa é: {impares}')