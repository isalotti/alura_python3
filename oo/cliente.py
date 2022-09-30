class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando getter @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter @property nome()")
        self.__nome = nome