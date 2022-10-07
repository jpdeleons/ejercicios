import re

def primerEjemplo():

    lista_nombres = ['Ana Gómez',
                     'María Martín',
                     'Sandra López',
                     'Tiago Martín']

    for elemento in lista_nombres:
        if re.findall('Martín$', elemento):
            print(elemento)


def segundoEjemplo():

    lista_de_nombres = ['http://pildorasinformaticas.es',
                        'ftp://pildorasinfromaticas.es',
                        'http://pildorasinformaticas.com',
                        'ftp://pildorasinfromaticas.com']

    for elemento in lista_de_nombres:
        if re.findall('^ftp', elemento):
            print(elemento)

def tercerEjemplo():

    lista_de_nombres = ['http://informaticaenespaña.es',
                        'http://pildorasinformartica.es',
                        'http://pildorasinformartica.com']
    for elemento in lista_de_nombres:
        if re.findall('[ñ]', elemento):
            print(elemento)


def cuartoEjemplo():

    lista_nombres = ['hombres',
                     'mujeres',
                     'mascotas',
                     'niños',
                     'niñas']

    for elementos in lista_nombres:
        if re.findall('niñ[oa]s', elementos):
            print(elementos)


primerEjemplo()
segundoEjemplo()
tercerEjemplo()
cuartoEjemplo()
