import forca
import adivinhacao

# forca.py

def jogar():
    print("*********************************")
    print("***Bem vindo!***")
    print("*********************************")

    print("ESCOLHER ")
    escolha = int(input("1- FORCA / 2- ADIVINHACAO "))
    if escolha == 1:
        forca.jogar()
    else:
        adivinhacao.jogar()


if(__name__ == "__main__"):
    jogar()