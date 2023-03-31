

# "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]     #sem nada depois do : vai até o fim da string
print(url_parametros)