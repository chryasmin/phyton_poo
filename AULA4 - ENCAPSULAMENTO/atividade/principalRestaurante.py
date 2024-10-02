from restaurante import Servico

pedido1 = Servico()

pedido1.novoPedido()
print("Pedidos realizados:", pedido1.mostrarPedido())

pedido1.cancelarPedido()
print("Pedidos realizados após cancelamento:", pedido1.mostrarPedido())

pedido1.cancelarPedido()
