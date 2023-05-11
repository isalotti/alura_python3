#HASH (mapa, dicionário)
#
#[chamve : valor]
dicionario = { "Izabela" : 38,
  "cachorro" : 1,
  "nome" : 'Laica',
  "trabalha" : 1
}
print("Dicionario : ", dicionario)

#Utilizando construtor
dicionario2 = dict(Izabela = 38, cachorro = 1)
print('Dicionario2 : ', dicionario2)

#Operacoes

#Listar
print("Izabela: ", dicionario["Izabela"])

#Modificar
dicionario["cachorro"] = 2
print('Cachorro 1 -> 2: ', dicionario["cachorro"])

#Excluir
del dicionario["trabalha"]
print('Exclui trabalha: ', dicionario)

#Verificar se elemento está no hash
print("trabalha existe? ", "trabalha" in dicionario)

for elemento in dicionario:
    print('Elemento (chave): ', elemento)

for elemento in dicionario.keys():
    print('Elemento (chaves):', elemento)

for valor in dicionario.values():
    print("Valores: ", valor)



for elemento in dicionario.keys():
    valor = dicionario[elemento]
    print('(chave, valor): ', elemento, valor)

for elemento in dicionario.items():    #tupla
    print('chave, valor', elemento)

for chave , valor in dicionario.items():  # tupla desempacotada
    print('chave, valor', chave , "=", valor)

# List comprehension
print(["palavra {}".format(chave) for chave in dicionario.keys()])

# Não mostrado na aula e cobrado no exercicio
# get - verificar se deterninada chave está no dicinario e retorna o valor
print("Izabela está no dict?", dicionario.get("Izabela"))