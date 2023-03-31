class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no fórum')

# MIXIN - classes sem responsabilidades, podem ser herdadas mas não devem ser instanciadas.
# uso : configs, logs, formatação...
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura,Caelum,Hipster):
    pass

# Testando as classes

jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
# uso do MRO   : Pleno > Alura > Funcionario > Caelum
# herança lida na ordem da esquerda para a direita na def da classe : Vai chamar método da Alura.
# se excluir o método de Alura, ele vai para a Caelum e não para Funcionario. Isso seria subir a hierarquia.
# primeiro busca ha mesma hierarquia -> Caelum
luan.mostrar_tarefas()

# Invoca o __str__ da classe Hipster ( MIXIN)
print(luan)