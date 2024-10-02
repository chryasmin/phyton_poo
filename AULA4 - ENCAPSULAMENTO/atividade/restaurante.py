class Servico:
    def __init__(self):
        self.__pedido = 0

    def novoPedido(self):
        self.__pedido += 1 

    def cancelarPedido(self):
        if self.__pedido > 0:
            self.__pedido -= 1
        else:
            print("Nenhum pedido para cancelar.")


    def mostrarPedido(self):
        return self.__pedido

    