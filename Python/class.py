from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome):
        self.__nome = nome 

    @abstractmethod
    def info(self):
        pass 
    def getnome(self):
        return self.__nome 

class Trabalhador(Pessoa):
    def __init__(self, nome,cargo):
        super().__init__(nome) 
        self.__cargo = cargo 

    def info(self):
        return f"Nome: {self.getnome()} Cargo Atual: {self.__cargo}"

    def setcargo(self,novo_cargo):
        self.__cargo = novo_cargo 


class Empresa():
    def __init__(self,nome):
        self.__nome = nome 
        self.funcionarios = []

    def addfunc(self,func):
        self.funcionarios.append(func) 

    def removefunc(self,func):
        self.funcionarios.remove(func)

    def listarfuncs(self):
        for a in self.funcionarios:
            return a.info() 
        
    def buscarfunc(self,func):
        for f in self.funcionarios:
            if f.getnome() == func:
                return f 

    def getnome_emp(self):
        return self.__nome



def menu_1():
    global empresas
    while True:
        for e in empresas:
            print(f"ID: {empresas.index(e)} Nome: {e.getnome_emp()}")
        escolha = input("=== EMPRESAS ===\n1- Acessar\n2- Voltar ")
        if escolha == '1':
            empresa_selecionada = int(input("ID: "))
            menu_2(empresas[empresa_selecionada])
        elif escolha == '2':
            print("Voltando...")
            break

def menu_2(empresa:Empresa):
    while True:
        print('=== ALTERAR ===\n1- Ver Funcionários\n2- Adicionar Funcionários\n3- Remover\n4- Buscar')
        escolha = input("> ")
        if escolha == "1":
            print(empresa.listarfuncs())

        elif escolha == "2":
            nome_func = input("Nome do Funcionário: ")
            cargo_func = input("Cargo do Funcionário: ")
            novo_func = Trabalhador(nome_func,cargo_func)
            empresa.addfunc(novo_func)
            print("Novo funcionário adicionado com sucesso!")

        elif escolha == '3':
            print("Em desenvolvimento...")

        elif escolha == '4':
            func_nome = input("Nome: ")
            funcionario = empresa.buscarfunc(func_nome)
            if funcionario:
                print("Funcionário encontrado! Visualizar? [S/N]")
                escolha2 = input("> ")
                if escolha2 == "S":
                    menu_3(funcionario)
                else:
                    print("Ok!")
            else:
                print("Opss..não encontrei!")
        elif escolha == "5":
            print("Voltando...")
            break

def menu_3(func:Trabalhador):
    while True:
        print(f"{func.info()}\n1- Mudar Cargo\n2- Saída")
        escolha = input("> ")
        if escolha == "1":
            novo_cargo = input("Novo Cargo: ")
            func.setcargo(novo_cargo)
            print("Alteração feita com sucesso!")
        elif escolha == "2":
            print("Voltando...")
            break




empresas = []

while True:
    print("=== EMPRESAS ===\n1- Criar Empresa\n2- Acessar empresa\n3- Saída")
    escolha = input("> ")
    if escolha == "1":
        nome_emp = input("Nome da empresa: ")
        empresa = Empresa(nome_emp)
        empresas.append(empresa)
        print("Empresa Criada com Sucesso!")
    elif escolha == "2":
        if empresas:
            menu_1()
        else:
            print("Nenhuma empresa...")
    elif escolha == "3":
        print("Volte sempre...")
        break


        
        
        

    
        