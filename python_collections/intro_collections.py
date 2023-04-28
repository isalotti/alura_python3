
#List
idades = [39, 30, 27, 18]

print('List idades: ', idades,' ' , type(idades))
print('idades[2] = ',idades[2])   #Lista inicia em 0

idades.append(15)
print('Adicionando item - fim da lista : ', idades)

idades.remove(15)
print('Retirando itens: ', idades)

print('28 em idades? ', 28 in idades)

if 28 in idades:
    idades.remove(28)

idades.insert(0,20)
print('Adiciona elemento em pos 0 :', idades)

idades.append([27,19])
for elemento in idades:
    print('elemento: ',elemento)

idades.extend([67,68])
print('Lista extendida: ', idades)

idades_no_ano_que_vem = []
idades = [21,40,19,28,20]
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem)

# versão reduzida do for

#list_comprehension
idades_no_ano_que_vem = [(idade + 1) for idade in idades]    # tem que estar entre colchetes
print(idades_no_ano_que_vem)

idades_maior_21 = [idade for idade in idades if idade > 21]
print('Imprimir idades > 21: ', idades_maior_21)

#Usando funcao
def proximo_ano(idade):
    return idade+1

prox_idade_maior_21 = [proximo_ano(idade) for idade in idades if idade > 21]
print('Imprimir idades + 1 > 21: ',prox_idade_maior_21)


idades.clear()
print('Limpa toda lista :', idades)

#Mutabilidade da lista

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        list = list()
    print('Lista (len): ',len(lista))
    print('Lista: ', lista)
    lista.append(22)

idades = [16,21,29,56,43]
faz_processamento_de_visualizacao(idades)

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()