import random


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
        self.__tamanho = len(programas)

    @property
    def nome(self):
        return self.__nome

    @property
    def programas(self):
        return self.__programas

    @property
    def tamanho(self):
        return self.__tamanho

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def adiciona_programa(self, programa):
        self.__programas.append(programa)

    def remove_programa(self, programa):
        self.__programas.remove(programa)


def teste():
    star_wars_ep_um = Filme("star wars - a ameaca fantasma", 1999, 136)
    mandalorian = Serie("the mandalorian", 2019, 2)
    toy_story = Filme("toy story", 1995, 81)
    witcher = Serie("the witcher", 2019, 1)
    playlist = Playlist("nome", [star_wars_ep_um, mandalorian, toy_story, witcher])
    playlist.remove_programa(star_wars_ep_um)
    playlist.adiciona_programa(Filme("homem aranha", 2002, 121))

    for programa in playlist.programas:

        contador = 0
        quantidade_aleatoria_de_likes = random.randint(0, 100)

        while contador < quantidade_aleatoria_de_likes:
            programa.incrementa_like()
            contador += 1

        print("\n{}".format(programa))


if __name__ == "__main__":
    teste()
