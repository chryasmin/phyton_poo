from carro import Carro

carro1 = Carro("Hyundai", "HB20", 2023, 96.95)
carro2 = Carro("Honda", "Civic", 2024,  78.90)


def exibirDetalhes(carro, dias):
    carro.exibirDetalhes()
    custo = carro.calcularPrecoAluguel(dias)
    print(f"Custo total para {dias} dias: R$ {custo:.2f}\n")


exibirDetalhes(carro1, 5)
exibirDetalhes(carro2, 3)