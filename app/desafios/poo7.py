# CLASSE AGENDA 

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar(self, nome):
        self.contatos.append(nome)
        print(f"'{nome}' adicionado!")

    def remover(self, nome):
        if nome in self.contatos:
            self.contatos.remove(nome)
            print(f"'{nome}' removido!")
        else:
            print(f"'{nome}' não está na agenda!")

    def listar(self):
        if self.contatos:
            print("Contatos:")
            for nome in self.contatos:
                print("-", nome)
        else:
            print("Agenda vazia!")


agenda = Agenda()

agenda.adicionar("João")
agenda.adicionar("Maria")
agenda.adicionar("Pedro")
agenda.listar()
agenda.remover("Maria")
agenda.listar()