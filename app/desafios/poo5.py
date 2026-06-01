#CLASSE LIVRO

class Livro:
    def __init__(self, titulo):
        self.titulo      = titulo
        self.disponivel  = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"'{self.titulo}' foi emprestado!")
        else:
            print(f"'{self.titulo}' já está emprestado!")

    def devolver(self):
        self.disponivel = True
        print(f"'{self.titulo}' foi devolvido!")



livro1 = Livro("O Pequeno Príncipe")


livro1.emprestar()
livro1.emprestar()
livro1.devolver()
livro1.emprestar()