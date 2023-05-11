#Testando o uso de diversas coleções

texto1 = """Rust vem ganhado popularidade em algumas áreas da Ciência de Dados devido à sua eficiência, desempenho e segurança. Vamos compreender a linguagem e o que pode vir por aí em Ciência de Dados."""

texto2 = """A verificação de e-mails em lote se tornou uma dica de produtividade comum. A ideia é que você só olhe para sua caixa de entrada duas a três vezes por dia ou pause as notificações por um período de tempo para poder se concentrar no trabalho sem distrações.

Reuniões em lote, chamadas ou eventos virtuais podem ser igualmente eficazes. Uma pesquisa da Ohio State University mostrou que, quando temos uma reunião na próxima hora ou duas, fazemos 22% menos trabalho em comparação com quando não temos reuniões futuras."""


from collections import Counter

aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())
print("Aparicoes :", aparicoes, ", Total: ",total_de_caracteres)  #conta caractere a caractere

for letra, frequencia in aparicoes.items():
    tupla = (letra, frequencia / total_de_caracteres)
   # print(tupla)

proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))
proporcoes.most_common(10) # os 10 mais

#fazendo em forma de funcao
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto1.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10) # os 10 mais
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}% ".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)