# Desafio 1 vendedor


class Vendas():
    def __init__(self,nome):
        self.vendas = nome
        self.vendas = 0

    def vendeu(self,vendas):
        self.vendas = vendas
    
    def bateumeta(self,meta):
        if self.vendas >= meta:
           print(f'{self.nome}Bateu a meta')

        else:
           print(f'{self.nome} Não bateu a meta')

vendedor1 = Vendas("Geronimo")
vendedor1.vendedor(1000)
vendedor1.bateuameta(500)

vendedor2 = Vendas("Vitin")
vendedor2.vendedor(1000)
vendedor2.bateuameta(500)