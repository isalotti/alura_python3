from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo      #private
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, other):      #importantem implementar quando listas de objetos
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __str__(self):
        return "[>>Codigo: {} , Saldo: {}<<]".format(self._codigo,self._saldo)

    #def __lt__(self, outro):
    #    return self._saldo == outro._saldo         ## neste caso, sobrecrevendo um método padrao less than (<), mantem dentro do objeto

                                                ## não quebra o encapsulamento
    #Novom método realizando a comparação dos atributos, assin não será precisso usar o attrgetter
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    # implementar o <=, pois não é composto pelo __eq__ e __lt__!
    #functools conjuga o que já esta implementado, via @total_ordering na classe


class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

conta3 = ContaMultiploSalario(37)
print(conta3)

print(conta1 == conta2)   # implementacao default comparar 2 objetos, o eq implementado, muda o comportamento

print(conta1 in [conta2])

print(conta3 in [conta2])

#comparando instâncias, usando método equals sobrescrito
print(isinstance(ContaSalario(34),ContaSalario))

print(isinstance(ContaMultiploSalario(34),ContaSalario))   #filho é considerado igual


######
conta_iza = ContaSalario(17)
conta_iza.deposita(500)

conta_leo = ContaSalario(3)
conta_leo.deposita(1000)

conta_eilene = ContaSalario(133)
conta_eilene.deposita(510)

contas = [conta_iza, conta_leo,conta_eilene]

for conta in contas:
    print(conta)

#Para ordenar objetos, deve ser definido key, para comparar A < B.
#A key pode ser definida como objeto
def extrai_saldo(conta):
    return conta._saldo        #oops! acessando variavel privada para comparar!

for conta in sorted(contas, key=extrai_saldo):
    print(conta)


#Outro método é acessar o atributo via attrgetter
#abordagem funcional

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):   #oops ! ainda acessando algo privado...
    print(conta)

################



for conta in sorted(contas):    # o __lt__ vai servir para o reverse tb.
    print(conta)


### critétios de desenpate
print(" ")

conta_da_iza = ContaSalario(1700)
conta_da_iza.deposita(500)

conta_do_leo = ContaSalario(3)
conta_do_leo.deposita(1000)

conta_da_eilene = ContaSalario(133)
conta_da_eilene.deposita(500)

contas = [ conta_da_iza, conta_do_leo, conta_da_eilene]

for conta in sorted(contas, key=attrgetter("_saldo","_codigo")):   # definir 2 critérios de comparação, em ordem para desempata
    print(conta)

print(" ")
for conta in sorted(contas):     #usando o __lt__
    print(conta)