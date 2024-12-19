# Lembre-se de seguir o README.md desse repositório como base para entender
# o design pattern Observer.

# Observer (Observador).
class Pessoa:
    def __init__(self, nome, cargo, salario):
        self.nome = "Nome: " + nome
        self.cargo = cargo
        self.salario = salario

    # Método opcional.
    # Criado apenas para facilitar na vizualização do estado atual do objeto.
    def show(self):
        return "----------------\n" + self.nome + "\nCargo: " + self.cargo + "\nSalario: " + str(self.salario) + "\n----------------"

    # É mais comum aplicar a lógica de comportamento do Observer no update.
    def update(self, cargo, valor):
        if self.cargo == cargo:
            self.salario += valor
        elif cargo == None:
            print(self.show())

# Subject (Sujeito).
class Empresa:
    def __init__(self):
        self.funcionarios = []

    # Contrata uma pessoa. Isso insere o objeto pessoa na sua lista de funcionarios.
    def contratar(self, pessoa):
        self.funcionarios.append(pessoa)

    # Demite um funcionario. Isso remove o objeto pessoa da sua lista de funcionarios.
    def demitir(self, pessoa):
        self.funcionarios.remove(pessoa)

    # Será utilizado para dar aumentos ou redução no salario com base em seus cargos.
    def notificar(self, cargo=None, valor=None):
        for pessoa in self.funcionarios:
            pessoa.update(cargo, valor)

# Criação da empresa (Subject).
XPTO = Empresa()

# Criação de pessoas que vieram para a entrevista de emprego (Observers).
carlos = Pessoa("Carlos", "Gerente", 2700)
diego = Pessoa("Diego", "Gerente", 2700)
fernanda = Pessoa("Fernanda", "Vendedor", 1450)
lucas = Pessoa("Lucas", "Vendedor", 1450)
luana = Pessoa("Luana", "Vendedor", 1450)

# Contratando pessoas.
XPTO.contratar(diego)
XPTO.contratar(fernanda)
XPTO.contratar(luana)

# Perceba que desta maneira não geramos notificações desnecessarias para quem não precisa, ou seja,
# somente as pessoas que foram contratadas serão notificadas da alteração de salario de seus respectivos cargos.

# Funcionamento
while True:
    entrada = input("Menu:\n1 - Aumentar 15 do salario dos vendedores.\n2 - Aumentar 50 do salario do gerente.\n3 - Listar de funcionarios.\nDigite:")
    if entrada == "1":
        XPTO.notificar("Vendedor", 15)
    elif entrada == "2":
        XPTO.notificar("Gerente", 50)
    elif entrada == "3":
        XPTO.notificar()
    else:
        print("Digite algum numero entre as opções do menu.")
