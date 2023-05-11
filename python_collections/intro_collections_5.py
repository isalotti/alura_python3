idades = [15,87,65,56,32,49,37]

for i in range(len(idades)):    #exclusivo o ultimo elemento  ,ou seja, do 0 ao 8
    print(i, idades[i])

#já existe método pronto para isso!

enumerate(idades)  # lazy : somente quando necessário gera os valores

print(list(range(len(idades))))  # forcar a geracao dos numeros do range

print(list(enumerate(idades)))

for valor in enumerate(idades):
    print(valor)                  #imprime a tupla gerada : (indice,valor)


for indice, valor in enumerate(idades):  #desempacota a tupla original em 2 partes
    print(indice, "x", valor)                  #imprime a tupla gerada : (indice,valor)

#Desempacotando tuplas
usuarios = [("Guilherme", 37,1981),
            ("Daniela", 31, 1987),
            ("Paulo", 39,1979)
]

for nome, idade, nascimento in usuarios:  #desempacotando cada um dos atributos
    print(nome)                     # utiliza somente o que quer

#ignorando o que vier depois, tem que definir algo para cada uma das variaveis na tupla. Mesmo numero
# de elementos completando com _
for nome, _, _ in usuarios:  # desempacotando cada um dos atributos
    print(nome)  # utiliza somente o que quer


#ordenando a lista (sem alterar a lista)

#ascendente
print(sorted(idades))

#descendente
print(list(reversed(idades)))      #reversed é lazy

print(sorted(idades,reverse=True))

print(list(reversed(sorted(idades))))

#ordenando a lista - alterando o objeto


s = idades.sort()
print(s)

nomes = ["Izabela", "Leonardo", "Eilene"]
print(sorted(nomes))      #ordenação feita letra a letra

