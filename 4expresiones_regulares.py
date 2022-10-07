import re

def primerEjemplo():
    nombre1 = "Sandra López"
    nombre2 = "Antonio Gómez"
    nombre3 = "sandra López"

    if re.match("Sandra", nombre3, re.IGNORECASE):
        print("Hemos encontrado el nombre")
    else:
        print("No lo hemos encontrado")

def segundoEjemplo():
    nombre1 = "Jara López"
    nombre2 = "Antonio Gómez"
    nombre3 = "Lara López"

    if re.match(".ara", nombre3, re.IGNORECASE):
        print("Hemos encontrado el nombre")
    else:
        print("No lo hemos encontrado")


def tercerEjemplo():
    cadena1 = "Jara López"
    cadena2 = "235235235"
    cadena3 = "a235235235"

    if re.match("\d", cadena2):
        print("Hemos encontrado el numero")
    else:
        print("No lo hemos encontrado")

def cuartoEjemplo():
    nombre1 = "Jara López"
    nombre2 = "Antonio Gómez"
    nombre3 = "Lara López"

    if re.search("López", nombre2):
        print("Hemos encontrado el nombre")
    else:
        print("No lo hemos encontrado")

def quintoEjemplo():
    codigo1 = "askljdhfj kahsdflkha71jhaskjasdhf"
    codigo2 = "jkdagksdfgiuse71hjsadhjsdf"
    codigo3 = "amdh jhajahs djas"

    if re.search("71", codigo1):
        print("Hemos encontrado el nombre")
    else:
        print("No lo hemos encontrado")

primerEjemplo()
segundoEjemplo()
tercerEjemplo()
cuartoEjemplo()
quintoEjemplo()