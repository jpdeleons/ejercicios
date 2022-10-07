import re

def primerEjemplo():
    lista_nombres = ['Ana',
                     'pedro',
                     'maria',
                     'rosa',
                     'sandra',
                     'celia']

    for elemento in lista_nombres:
        if re.findall('[o-t]$', elemento):
            print(elemento)

def segundoEjemplo():
    lista_nombres = ['Ma1',
                     'Se1',
                     'Ma2',
                     'Ba1',
                     'Ma3',
                     'Va1',
                     'Va2',
                     'Ma4']

    for elemento in lista_nombres:
        if re.findall('Ma[0-3]', elemento):
            print(elemento)

def tercerEjemplo():
    lista_nombres = ['Ma1',
                     'Se1',
                     'Ma2',
                     'Ba1',
                     'Ma3',
                     'Va1',
                     'Va2',
                     'Ma4',
                     'MaA',
                     'Ma5',
                     'MaB',
                     'MaC']

    for elemento in lista_nombres:
        if re.findall('Ma[0-3A-B]', elemento):
            print(elemento)

def cuartoEjemplo():
    lista_nombres = ['Ma.1',
                     'Se1',
                     'Ma2',
                     'Ba1',
                     'Ma:3',
                     'Va1',
                     'Va2',
                     'Ma4',
                     'MaA',
                     'Ma.5',
                     'MaB',
                     'Ma:C']

    for elemento in lista_nombres:
        if re.findall('Ma[.:]', elemento):
            print(elemento)

primerEjemplo()
segundoEjemplo()
tercerEjemplo()
cuartoEjemplo()