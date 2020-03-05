"""
Exercício 2 de LAEDs
Aluno: Fúlvio Taroni Monteforte
"""

class Biblioteca:
    # Método construtor-------------------------------------------------------------------------------------------------
    def __init__(self, livros=None):
        self.livros = livros

        if livros is None:
            self.livros = list()

    # Métodos especias--------------------------------------------------------------------------------------------------
    def add_livro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        pass

    # Métodos adicionais
    def livros_por_autor(self):
        lista_autores = list()
        lista_titulos = list()
        chaves = list()

        # Cria uma lista de autores e uma lista de titulo que será útil na construção do dicionário
        for iter in livros:
            lista_autores.append(iter.get_autores())
            lista_titulos.append(iter.get_titulo())

        for i in range(len(lista_autores)):
            for j in range(len(lista_autores[i])):
                chaves.append(lista_autores[i][j].nome_como_citado())
        dicionario = dict()
        for iter in chaves:
            dicionario.setdefault(iter, list())

        # Só Deus sabe como esse loop deu certo
        for i in range(len(livros)):
            for j in range(len(livros[i].get_autores())):
                x = livros[i].get_autores()
                for k in range(len(x)):
                  dicionario[x[k].nome_como_citado()].append(livros[i].get_titulo())

        # Na real ele não deu certo, esse pedaço corrige o que sai errado dele (Elimana repetições)
        chaves = set(chaves)
        chaves = list(chaves)
        for iter in chaves:
            aux = set(dicionario[iter])
            aux = list(aux)
            dicionario[iter] = aux

        return dicionario
# Fim da classe Biblioteca----------------------------------------------------------------------------------------------


class Livro:
    quant_livros = 0 # Apenas para controle do desenvolvedor

    # Método construtor-------------------------------------------------------------------------------------------------
    def __init__(self, data, titulo=None, autores=None,):
        if titulo is None or titulo == '':
            raise ValueError("Erro!! O título não pode estar vazio")
        self.titulo = titulo
        self.data = data
        self.autores = autores
        self.quant_livros += 1
        if autores is None:
            self.autores = list()

    # Métodos especiais-------------------------------------------------------------------------------------------------
    def set_titulo(self, titulo=None):
        if titulo is None or titulo == '':
            raise ValueError("Erro!! O título não pode estar vazio")
        self.titulo = titulo

    def set_data(self, data):
        self.data = data

    def set_autores(self, autores):
        self.autores = autores

    def get_titulo(self):
        return self.titulo

    def get_data(self):
        return self.data

    def get_autores(self):
        return self.autores

    def get_quant_livros(self):
        return self.quant_livros

    def __str__(self):
        return f'Titulo: {self.get_titulo()}\nData: {self.get_data()}\nAutores: {self.get_autores()}'
# Fim da classe Livro---------------------------------------------------------------------------------------------------


class Autor:
    num_autores = 0 # Apenas par controle do desenvolvedor

    # Método construtor-------------------------------------------------------------------------------------------------
    def __init__(self, nome_1, nome_3, nome_2=''):
        self.nome_1 = nome_1
        self.nome_2 = nome_2
        self.nome_3 = nome_3
        Autor.num_autores += 1

    # Métodos especiais-------------------------------------------------------------------------------------------------
    def set_nome_1(self, nome):
        self.nome_1 = nome

    def set_nome_2(self, nome):
        self.nome_2 = nome

    def set_nome_3(self, nome):
        self.nome_3 = nome

    def get_nome_1(self):
        return self.nome_1

    def get_nome_2(self):
        return self.nome_2

    def get_nome_3(self):
        return self.nome_3

    def get_quant_autores(self):
        return self.num_autores

    def __str__(self):
        return f'{self.get_nome_1()} {self.get_nome_2()} {self.get_nome_3()}'

    # Métodos adicionais------------------------------------------------------------------------------------------------
    def nome_como_citado(self):
        x = self.get_nome_3()
        x = x.upper()
        y = self.get_nome_1()
        y = y[0]
        return f"{x} {y}."
# Fim da classe Autor---------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    # Criando autores---------------------------------------------------------------------------------------------------
    autor0 = Autor('', '', '')
    autor0.set_nome_1('Fúlvio')
    autor0.set_nome_2('Taroni')
    autor0.set_nome_3('Monteforte')

    autor1 = Autor('Lara', 'Galvani')

    autor2 = Autor('Thiago', 'Bahia', 'Lima')

    autor3 = Autor('Sophia', 'Black')

    """
    # Testar métodos da classe Autor
    print(autor0.__str__())
    print(autor0.nome_como_citado())
    print(autor0.get_quant_autores())
    """
    # Fim da região que cria os autores---------------------------------------------------------------------------------

    # Criando livros----------------------------------------------------------------------------------------------------
    livro0 = Livro('', 'Harry Potter e a Câmara Secreta', '')
    livro0.set_autores([autor0, autor1])
    # livro0.set_titulo('')
    livro0.set_data('20/10/1998')

    livro1 = Livro('23/12/1997', 'Guia do Mochileiro das Galáxias', [autor2])

    livro2 = Livro('14/05/2039', 'O Conto de Uma República Alegre', [autor0, autor1, autor3])

    livros = list()
    livros.append(livro0)
    livros.append(livro1)
    livros.append(livro2)
    # Fim da região que cria os livros----------------------------------------------------------------------------------
    """
    """
    # Criando a biblioteca----------------------------------------------------------------------------------------------
    biblioteca = Biblioteca(livros)

    # Testando a função de 'livros_por_autor'---------------------------------------------------------------------------
    for autor, livros in biblioteca.livros_por_autor().items():
        print(f'Autor: {autor} - Livros: {livros}')
