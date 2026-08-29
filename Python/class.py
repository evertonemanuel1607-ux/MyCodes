from abc import ABC

class Pessoa(ABC):
    def __init__(self,nome,cpf):
        self.__nome = nome 
        self.__cpf = self.setcpf(cpf)

    
    def setcpf(self,var):
        if var >= 1:
            self.__cpf = var

    
    def getcpf(self):
        return self.__cpf 

    def getnome(self):
        return self.__nome

class Estudantes(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.resultado = False

    def getresultado(self):
        if self.resultado == True:
            return 'Aprovado'
        else:
            return 'Reprovado'
    def setresultado(self,valor):
        self.resultado = valor

class Turma:
    def __init__(self,nome):
        self.nome = nome
        self.__alunos = []

    def addalunos(self,aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)

    def removealunos(self,id):
        aluno = self.__alunos[id]
        self.__alunos.remove(aluno)

    def veralunos(self):
        for a in self.__alunos:
            return f"ID: {self.__alunos.index(a)} CPF: {a.getcpf()} Nome: {a.getnome()}"
        
    def buscaraluno(self,id):
        aluno = self.__alunos[id]
        return aluno


def turmasfun(turma):
    print("=== Turmas ===\n1- Ver alunos\n2- Adicionar\n3- Remover\n4- Alterar nota")
    escolhafun = input("> ")
    if escolhafun == '1':
        print(turma.veralunos())
    elif escolhafun == '2':
        nome = input('Nome aluno: ')
        cpf = int(input('CPF do aluno: '))
        a = Estudantes(nome,cpf)
        turma.addalunos(a)
        print(f"Aluno {nome} adicionado com sucesso!")
    elif escolhafun == '3':
        ida = int(input('ID: '))
        turma.removealunos(ida) 
        print("Aluno removido! ")
    elif escolhafun == '4':
        ida = int(input('ID: '))
        aluno = turma.buscaraluno(ida) 
        if aluno:
            print(f"Aluno encontrado! {aluno.getnome()}")
            resultado = input("Ele passou? [S/N]: ")
            if resultado == 'S':
                aluno.setresultado(True)
                print("Alteração feita!")
            else:
                aluno.setresultado(False)
                print('Alteração feita!')




turmas = []

while True:
    print("=== ESCOLA ===\n1- Criar Turma\n2- Acessar Turma\n3- Saída...")
    escolha = input("> ")
    if escolha == '3':
        break
    elif escolha == '2':
        if turmas:
            for t in turmas:
                print(f"ID: {turmas.index(t)} Nome: {t.nome}")
            escolha2 = int(input("Qual acessar? (id): "))
            turma_escolhida = turmas[escolha2]
            turmasfun(turma_escolhida)
        else:
            print("Opss...não tem nada")
    elif escolha == '1':
        nome_turma = input("Nome da Turma: ")
        t = Turma(nome_turma)
        turmas.append(t)
        print("Turma Cadastrada com sucesso!")
    


print("Volte sempre...")