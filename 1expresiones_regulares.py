import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

def primerEjemplo():
    print(re.search("aprender", cadena))


def segundoEjemplo():
    textoBuscar = "aprender"
    if re.search(textoBuscar, cadena) is not None:
        print("He encontrado 1 texto")
    else:
        print("No he encontrado el texto")

def tercerEjemplo():
    textoBuscar = "aprender"
    textoEncontrado = re.search(textoBuscar, cadena)

    print(textoEncontrado.start())
    print(textoEncontrado.end())
    print(textoEncontrado.span())

def cuartoEjemplo():
    textoBuscar = "Python"
    print(re.findall(textoBuscar, cadena))
    print(len(re.findall(textoBuscar, cadena)))

primerEjemplo()
segundoEjemplo()
tercerEjemplo()
cuartoEjemplo()