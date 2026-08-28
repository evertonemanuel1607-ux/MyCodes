class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade 
    
    def info(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

class Programador(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        self.saldo = 0 
        self.projetos = []

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def deposito(self,valor):
        if valor >= 0:
            self.saldo += valor

    def info(self):
        return f"Programador: {self.nome} Idade: {self.idade} Saldo: {self.saldo}"
    
    def addproj(self,projeto):
        self.projetos.append(projeto)

    def listarproj(self):
        for p in self.projetos:
            print(p.titulo,p.ling)

class Projetos:
    def __init__(self,titulo,linguagem):
        self.titulo = titulo 
        self.ling = linguagem
        
    def infoproj(self):
        return(f'Projeto: {self.titulo} Linguagem: {self.ling}')
  

projeto1 = Projetos('Snake','Python')
projeto2 = Projetos('Sites','Python')

p2 = Programador('Everton',20)
print(p2.info())

p2.deposito(10)
print(p2.info())

p2.sacar(12)
print(p2.info())

p2.addproj(projeto1)
p2.addproj(projeto2)

p2.listarproj()