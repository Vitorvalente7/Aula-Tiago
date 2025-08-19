numeros = []


while True:
        n = int(input("Digite um valor: "))
        if n not in numeros:
            numeros.append(n)
            print('Valor adicionado com sucesso...')
        else:
                print(f'Valor {n} ja Existe na lista...')
        
        resposta = input('Quer continuar/ [S/N]')
        if resposta in 'Nn':
            break

print('='*30)
numeros.sort()
print(f'Voce digitou os valores: {numeros}')
numeros.sort(reverse=true)
print(f'Os valores digitados em ordem descresente são {numeros}')

