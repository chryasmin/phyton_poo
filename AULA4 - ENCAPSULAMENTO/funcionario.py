class Funcionario:
    def __init__(self, cargo, salario=2000):
        self.__cargo = cargo
        self.__salario = salario #esse atributo está opcional, caso não seja informado outo valor será atribuido o valor padrão de R$2000

    def getCargo(self):
        return self.__cargo

    def setCargo(self, novoCargo):
        self.__cargo = novoCargo

#IREMOS UTILIZAR UMA FORMA ÚNICA DO PHYTON PARA ACESSAR ATRIBUTOS PRIVADOS

    #criando o 'get' do salário 'mais amigável'
    @property 
    def salario(self):
        return self.__salario

    #criando o 'set' do salário 'mais amigável'
    @salario.setter
    def salario(self, valor):
        if valor <= 0:
            print("Informe um valor positivo")
        else:
            self.__salario = valor
       