import random

import forca
import jogos
def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while ( not enforcou and not acertou):
        chute = input("Digite uma letra ")
        chute = chute.strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            print("jogando")
        else:
            print ("Errou")
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("ACERTOU")
        print("FIM DO JOGO")
        jogar_novamente()
    else:
        print("ERROU")
        print("PALAVRA SECRETA: ", palavra_secreta)
        print("LETRAS ACERTADAS: ", letras_acertadas)
        print("FIM DO JOGO")
        jogar_novamente()

def jogar_novamente():
    print("Jogar novamente? ")
    resposta_jogar_novamente = int(input("1- SIM/ 2- NÃO "))
    while (resposta_jogar_novamente != 1 or resposta_jogar_novamente != 2):
        if resposta_jogar_novamente == 1 :
            forca.jogar()
        elif resposta_jogar_novamente == 2 :
            jogos.jogar()

def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt" , "r")
    palavras = []
    for linha in arquivo :
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


if(__name__ == "__main__"):
    jogar()