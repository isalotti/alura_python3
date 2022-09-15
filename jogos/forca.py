def jogar():
    print("***********************************")
    print("*** Bem vindo no jogo da Forca! ***")
    print("***********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input ("> Qual a letra ? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, vocé errou! Faltam {} tentativas...".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        letras_faltando = str(letras_acertadas.count('_'))
        if int(letras_faltando) > 0:
            print("> Ainda faltam acertar {} letras!".format(letras_faltando))

    if acertou:
        print(">> Você ganhou!! <<")
    else:
        print(">> Você perdeu!! <<")

if(__name__ == "__main__"):
    jogar()

