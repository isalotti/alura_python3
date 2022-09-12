import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("Escolha seu JOGO!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if jogo == 1:
        print("Jogando forca...")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação..")
        adivinhacao.jogar()
    print("-----------Fim do jogo!-----------")

if(__name__ == "__main__"):
    escolhe_jogo()
