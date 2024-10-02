class Conta:
    #método construtor
    def __init__(self, numero, titular, saldo, limite = 200):#passando valor padrão para o limite, tornado opcional, objeto ao ser criado pode ter limite
        #quando colocamos 2 underlines antes do nome do atriburo indicamos qie ele está com a visibilidade privada, o contrário significa que ele está público 
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

#criando os demais métodos
    def detalhes(self):
        print(f"Olá, {self.__titular} seu saldo atual é {self.__saldo}")

    #IRÁ RETORNAR O CONTEÚDO DO LIMITE
    def getLimite(self):
        return self.__limite
    
    #mÉtOdo para alteração de valor do limite
    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor positivo para o limite")
        else:
            self.__limite = valor

    #CRIANDO MÉTODO PARA DEPOSITAR VALOR
    def depositar(self, valor):
        if valor < 0:
            print("Informe um valor maior que zero")
        else: 
            self.__saldo = self.__saldo + valor

    #criando método para sacar valor
    def sacar(self, valor):
        if self.__saldo <= 0 or valor > self.__saldo:
            print("Saldo insuficiente")
        else: 
            self.__saldo = self.__saldo - valor