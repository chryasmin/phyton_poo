class Carro:
    
    def __init__(self, marca, modelo, ano, precoDiaria): 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiaria = precoDiaria

    def exibirDetalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço por dia: R$ {self.precoDiaria:.2f}")
        
    def calcularPrecoAluguel(self, dias):
        return self.precoDiaria * dias