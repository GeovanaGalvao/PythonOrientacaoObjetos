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


def teste():

    star_wars_ep_um = Filme("star wars - a ameaca fantasma", 1999, 136)
    star_wars_ep_um.incrementa_like()
    mandalorian = Serie("the mandalorian", 2019, 2)
    mandalorian.incrementa_like()
    mandalorian.incrementa_like()
    filmes_e_series = [star_wars_ep_um, mandalorian]

    for programa in filmes_e_series:
        print("\nNome: {}\nAno: {}".format(programa.nome, programa.ano))
        print("Temporadas: {}\nLikes: {}".format(programa.temporada, programa.likes)) if isinstance(programa, Serie) \
            else print("Duração: {} minutos\nLikes: {}".format(programa.duracao, programa.likes))


if __name__ == "__main__":
    teste()
