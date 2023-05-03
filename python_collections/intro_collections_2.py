class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0


    def deposita(self, valor):
        self.saldo += valor


    def __str__(self):
        return "[>>Codigo {} , Saldo {}<<]".format(self.codigo, self.saldo)


conta_iza = ContaCorrente(15)
print(conta_iza)

conta_iza.deposita(500)
print(conta_iza)

conta_leo = ContaCorrente(2000)
conta_leo.deposita(345)

contas = [conta_iza,conta_leo]
print(contas)

#chama o __str__
for conta in contas:
    print(conta)

print(contas[0])

# método
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas(contas)
print(contas[0],contas[1])

contas.insert(0,76)
print(contas[0],contas[1],contas[2])

#dá erro, pois o item [2] não é oo
#deposita_para_todas(contas)


#tupla
# - imutavel
# - sem métodos agregados

iza = ('Izabela',38,1984)
leo = ('Leo',36,1986)



#Trabalhando o que era OO com abordagem funcional (tupla:)

conta_iza = (15,1000)
print(conta_iza[0])

#conta_iza[1] += 100   #erro - tuplas são imutaveis
#print(conta_iza[1])

#Abordagem funcional (separando comportamento dos dados)
def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo,novo_saldo)

print(deposita(conta_iza))   #cria outra tupla, pois ela é imutavel

print(conta_iza)    # retorna os valores anteriores - a tupla original não foi modificada


#Colocando as tuplas em uma lista
usuarios = [iza,leo]
print(usuarios)



#fazendo uma tupla de objetos
conta_da_iza = ContaCorrente(15)
conta_da_iza.deposita(500)

conta_do_leo = ContaCorrente(16)
conta_do_leo.deposita(345)

contas_tupla = (conta_da_iza,conta_do_leo)   # A tupla não pode ser modificadas, mas os objetos dentro dela sim

for conta in contas_tupla:
    print(conta)

contas_tupla[0].deposita(300)
for conta in contas_tupla:
    print(conta)

