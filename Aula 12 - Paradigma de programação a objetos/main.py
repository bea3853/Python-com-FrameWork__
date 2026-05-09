# Crie uma classe Pessoa com os atributos nome e idade. Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos." Crie duas pessoas diferentes e chame o método.

# criei a classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade  = idade
# criei o método
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, eu tenho {self.idade}')
# instaciei a classe
pessoa1 =  Pessoa('Kaio',20)
pessoa2 =  Pessoa('Maria',22)
# usei o método na instancia 
pessoa1.apresentar()
pessoa2.apresentar()













# class Caneta:
#     def __init__(self):
#         self.cor = 'azul'
#         self.ponta = 0.7
#         self.tamanho =  13.0
#         self.substrato = 'plastico'

#     def escrever(self):
#         pass    

# caneta = Caneta()
# print(caneta.ponta)    


# class Pessoa:
#     def __init__(self, idade):
#         self.idade = idade    

#     def verificar_idade(self):
#         if self.idade <= 14:
#             print('Criança')
#         elif self.idade >=15 and self.idade <= 17:
#             print('adolescente')
#         elif self.idade >= 18 and self.idade <= 34:
#             print('jovem')
#         elif self.idade >= 35 and self.idade <=60:
#             print('Adulto')
#         else:
#             print('idoso')        

# pessoa =  Pessoa(17)
# pessoa.verificar_idade()