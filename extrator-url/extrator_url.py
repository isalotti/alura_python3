import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")


    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self,parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parametros: " + self.get_url_parametros() + "\n" + "URL base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url = "https://bytebank.com/cambio?moedaDestino=real&quantidade=100&moedaOrigem=dolar"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais

moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

valor_convertido = 0
moeda_de = ""
moeda_para = ""

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_convertido = int(quantidade) * VALOR_DOLAR
    moeda_de = "R$"
    moeda_para = "$"
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_convertido = int(quantidade) / VALOR_DOLAR
    moeda_de = "S"
    moeda_para = "R$"
else:
    valor_convertido = -1

if valor_convertido == -1:
    error =  f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível."
    raise ValueError(error)
print(f"O valor de {moeda_de} {quantidade} é igual a {moeda_para} {valor_convertido:.2f}.")



# print("O tamanho da URL é : ", len(extrator_url))
# print(extrator_url)
# # extrator_url = ExtratorURL(None)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)
#
# extrator_url2 = ExtratorURL(url)

# print(extrator_url.__eq__(extrator_url2))
#
# #print(id(extrator_url))
#
# print(extrator_url == extrator_url2)# extrator_url.__eq__(extrator_url_2)

