
def jogar():
    print("JOGO DE FORCA")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while ( not enforcou and not acertou):
        print("jogando")
        chute = input("Digite uma letra ")
        if ( palavra_secreta.find(chute) ):
            print("")
        else:
            print("")

    print("FIM DO JOGO")

if(__name__ == "__main__"):
    jogar()