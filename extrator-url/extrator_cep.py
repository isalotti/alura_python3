import re #Regular Expresson - RegEx

#CEP  5 digitos + hifen (opicional) + 3 digitos

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ , 23440-120"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # retorna obj match

# ? opcional
# {9} numero de repeticoes
# {0,1} limite de repetiçoes (de , até)
#[0-9] de 0 a 9 (intervalo)

if busca:
    cep = busca.group()  #string encontrada no padrao
    print(cep)

