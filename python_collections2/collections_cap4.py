#Dicionarios (hash)

meu_texto = "Eu sou Izabela e tenho um cachorro e gosto muito de cachorro"

meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)  # se não tiver, aparece 0
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

#Dicionario default

from collections import defaultdict

aparicoes = defaultdict(int)  # dicionario de inteiros como valores. Vai colocar 0 quando não houver

for palavra in meu_texto.split():
    #ate_agora = aparicoes[palavra] # se não tiver, aparece 0 . Com o default dict não precisa desta linha par somar embaixo
    aparicoes[palavra] += 1

print("Defaultdict", aparicoes)

class Conta:
    def __init__(self):
        print('Imprimindo a conta!')

contas = defaultdict(Conta)  #sempre que não houver, ele cria uma Conta, via construtor default
contas[15]   # falha na busca e chama o construtor
contas[17]

print('Contas:', contas)

## Função Counter

from collections import Counter

aparicoes = Counter(meu_texto.split())  # já faz a separação, não vai precisar do for!

print("Aparicoes: ",aparicoes)