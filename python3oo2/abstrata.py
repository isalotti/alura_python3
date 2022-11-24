from abc import ABC  #abstract base classes

from collections.abc import MutableSequence
from numbers import Complex

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()

class Playlist(MutableSequence):
    pass



##
from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

lista = MinhaListagem('Nova_lista')
print(lista)




# Se você ficou com curiosidade sobre como criar uma classe abstrata, vamos pensar no seguinte caso:
# imagine que não queremos permitir que ninguém instancie um objeto da classe Programa, e queremos garantir que
# todo mundo implemente o __str__ nas suas subclasses. Parece uma boa ideia.



from abc import ABCMeta, abstractmethod
class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass