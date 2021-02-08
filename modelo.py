class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()  # Todas as palavras terão a primeira letra como maiuscula
        self.__ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def incrementa_like(self):
        self.__likes += 1

    def __str__(self):
        return "Nome: {}\nAno: {}\nLikes: {}".format(self.nome, self.ano, self.likes)


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao  # Em minutos

    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return "Nome: {}\nAno: {}\nDuração: {} min\nLikes: {}".format(self.nome, self.ano, self.duracao, self.likes)


class Serie(Programa):

    def __init__(self, nome, ano, quantidade_temporadas):
        super().__init__(nome, ano)
        self.__temporadas = quantidade_temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    def incrementa_temporada(self):
        self.__temporadas += 1

    def __str__(self):
        return "Nome: {}\nAno: {}\nTemporadas: {}\nLikes: {}".format(self.nome, self.ano, self.temporadas, self.likes)


class Playlist:

    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.programas)

    @property
    def nome(self):
        return self.__nome

    @property
    def programas(self):
        return self.__programas

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def adiciona_programa(self, programa):
        self.__programas.append(programa)

    def remove_programa(self, nome_do_programa):
        programa = self.procura_programa_na_lista(nome_do_programa)
        self.__programas.remove(programa) if isinstance(programa, Programa) else None

    def procura_programa_na_lista(self, nome_do_programa):
        nome_do_programa = nome_do_programa.title()
        for programa in self:
            if programa.nome == nome_do_programa:
                return programa

    def exibe_informacoes_programa(self, nome_do_programa):
        programa = self.procura_programa_na_lista(nome_do_programa)
        print("\n{}".format(programa)) if isinstance(programa, Programa) else None

    def exibe_programas(self):
        for programa in self:
            print("\n{}".format(programa))


def teste():

    playlist = Playlist("Maratona para final de semana", [])
    playlist.adiciona_programa(Filme("star wars - a ameaca fantasma", 1999, 136))
    playlist.adiciona_programa(Serie("the mandalorian", 2019, 2))
    playlist.adiciona_programa(Filme("toy story", 1995, 81))
    playlist.adiciona_programa(Serie("the witcher", 2019, 1))
    playlist.adiciona_programa(Filme("homem aranha", 2002, 121))
    print("\nTamanho da playlist: {}".format(len(playlist)))
    playlist.exibe_informacoes_programa("the mandalorian")
    playlist.exibe_informacoes_programa("pokemon")
    playlist.remove_programa("the mandalorian")
    playlist.remove_programa("south park")
    print("\nNovo tamanho da playlist: {}".format(len(playlist)))
    playlist.exibe_programas()


if __name__ == "__main__":
    teste()
