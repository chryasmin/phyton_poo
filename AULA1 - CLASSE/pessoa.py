class Pessoa: 
    #atributos
    nome = "Fulano"
    idade = 25
    altura = 1.60

    #métodos: são comportamentos da classe
    def falar(self,texto): #self: parâmetro obrigatório
        print(f"tenho algo para te falar: {texto}")

#CRIANDO OBJETOS
pessoa1 = Pessoa()  #OBJETO DO TIPO PESSOA        

print(pessoa1.nome, pessoa1.idade)
pessoa1.falar("Bom dia, hoje é segunda-feira")