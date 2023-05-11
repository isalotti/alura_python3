
## LISTAS
usuarios_data_science = [15,23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = []
#Copia uma lista par aa outra
assistiram = usuarios_data_science.copy()
#Copiar uma lista para a outra - inserindo
assistiram.extend(usuarios_machine_learning)

assistiram

print("assistiram ", assistiram)
#Problema : copiou todos os valores sem verificar se são repetidos.
# Em uma lista pode haver elementos repetidos.

# SET
#
# Não adimite repetições em seus valores
# Limitado por { }
# Ordem não importa (sem acesso sequencial, sem acesso indexado)

print('assistiram (set)',set(assistiram))
print('outra lista : ', set([1, 2, 3, 4, 1]))

usuarios_data_science_set = {15,23, 43, 56}
usuarios_machine_learning_set = {13, 23, 56, 42}

#União (OU) : |
print("União de conjuntos: ", usuarios_machine_learning_set | usuarios_machine_learning_set)

#Intersecção (AND) : &
print('Intersecção: ', usuarios_data_science_set & usuarios_machine_learning_set)

# Diferença (NOT) : -
print('Diferença: ', usuarios_data_science_set - usuarios_machine_learning_set)


#Verificar se está no conjunto
fez_ds_mas_nao_fez_ml = usuarios_data_science_set - usuarios_machine_learning_set
print('15  fez ds? ', 15 in fez_ds_mas_nao_fez_ml)

#OU exclusivo : ^
print("Usuarios nos 2 conjuntos Sem repetição: ", usuarios_data_science_set ^ usuarios_machine_learning_set)

###
# SETS são mutáveis

usuarios = {1, 5, 76, 34, 52, 13, 17}
print('Usuarios = ', usuarios, ', len: ', len(usuarios))

usuarios.add(13)
print('Usuarios (add 13) = ', usuarios, ', len: ', len(usuarios))

usuarios.add(345)
print('Usuarios (add 345)= ', usuarios, ', len: ', len(usuarios))

#Impedir adições no SET
usuarios = frozenset(usuarios)

print('Frozen usuarios : ', usuarios)


meu_texto = "Eu tenho um cachorro e gosto muito de cachorro"
print(meu_texto)
print(meu_texto.strip())
print(set(meu_texto.split()))  #cachorro está repetido e nao vai para o conjunto

