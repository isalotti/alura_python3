class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'

class FolhaDePagamento:

    @staticmethod
    def log():
        return f'Isso é um log qualquer.'

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())