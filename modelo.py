class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()  # Todas as palavras terão a primeira letra como maiuscula
        self.__ano = ano
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def like(self):
        return self.__like

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def incrementa_like(self):
        self.__like += 1


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao  # Em minutos

    @property
    def duracao(self):
        return self.__duracao


class Serie(Programa):

    def __init__(self, nome, ano, quantidade_temporadas):
        super().__init__(nome, ano)
        self.__temporadas = quantidade_temporadas

    @property
    def temporada(self):
        return self.__temporadas

    def incrementa_temporada(self):
        self.__temporadas += 1
