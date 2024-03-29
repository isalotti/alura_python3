import re

#https://www.bytebank.com.br/cambio     # padrão completo
#
# Exemplos de URLs válidas:
#     bytebank.com/cambio
#     bytebank.com.br/cambio
#     www.bytebank.com/cambio
#     www.bytebank.com.br/cambio
#     http://www.bytebank.com/cambio
#     http://www.bytebank.com.br/cambio
#     https://www.bytebank.com/cambio
#     https://www.bytebank.com.br/cambio
#
# Exemplos de URL inválidas:
#     https://bytebank/cambio
#     http://bytebank.naoexiste/cambio
#     ht:bytebank.naoexiste/cambio
#
# (aaa)  string exata
# ?  opcional

url = "https://www.bytebank.com.br/cambio"

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

match = padrao_url.match(url)

if not match:
    raise  ValueError("A URL não é válida.")
print("A URL é válida")

