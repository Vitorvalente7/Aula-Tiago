# Desafio 3 criar uma classe para substituir um codigo 

class Conta:
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self,valor):
        self.saldo = valor
        print(f'Sala da Conta: {self.saldo}')

C1= Conta('Maria Antonieta')
C1.depositar(int(input(f'{C1.titular}Quanto voce deseja depositar? ')))

     




    