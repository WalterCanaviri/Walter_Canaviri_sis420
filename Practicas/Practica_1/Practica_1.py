def Menu ():
    print("Menu: ")
    print("1 Imprimir bibliografia")
    print("2 Salir")
    a=int(input())
    if a==1:
        Bib()
    elif a==2:
        Salir()
    else:
        print("Numero incorrecto, vuelva a internarlo")
        Menu()
def Bib():
    print("Informacion:")
    print("Mi nombre es Walter Canaviri y tengo 22 años")
    print(" ")
    b=int(input("Digite 1 para volver al menu: "))
    if b==1:
        Menu()
    else:
        Bib()
def Salir():
    print("FIN")

Menu()