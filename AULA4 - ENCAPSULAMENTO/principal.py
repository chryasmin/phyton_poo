from funcionario import Funcionario

funcionario1 = Funcionario("Gerente", 3000)
print("Seu cargo atual é:",funcionario1.getCargo())


#TENTANDO MUDAR O VALOR DO ATRIBUTO
funcionario1.__cargo = "Surpevisor" #ACESSANDO O ATRIBUTO DIRETO (NÃO DEU CERTO PQ TA PRIVADO)
funcionario1.setCargo("Engenheiro") #ACESSANDO O MÉTODO PARA MUDAR O CARGO
print("Seu cargo atual é:",funcionario1.getCargo())

#EXIBINDO O SALÁRIO
print("Seu salário atual é ", funcionario1.salario)

funcionario1.salario = 5500
print("Seu salário atual é ", funcionario1.salario)