class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title  # Todas as palavras terão a primeira letra como maiuscula
        self.__ano = ano
        self.__duracao = duracao  # Em minutos
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao

    @property
    def like(self):
        return self.__like

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title

    def incrementa_like(self):
        self.__like += 1


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title
        self.__ano = ano
        self.__temporadas = temporadas
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def like(self):
        return self.__like

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title

    def incrementa_like(self):
        self.__like += 1

    def incrementa_temporada(self):
        self.__like += 1
