class Pessoa:
    #criando método construtor
    def __init__(self, nome, hobby, endereco):
        #estamos criando os atributos da classe, utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atributos
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

        #Criando os étodos normais
        def exibirDados(self):
            print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")

#CRIANDO OBJETOS

pessoa1 = Pessoa("João", "História", "Bequimão")
pessoa1.exibirDados()

pessoa2 = Pessoa("Karla", "Artes Marciais", "Av 12 Renasceça")
print(pessoa2.nome)