import string
import funciones_SQLite
from funciones_SQLite import cursorBaseDeDatos
from funciones_SQLite import baseDeDatos

def ingresoCodigoDeBarras():
    # Leo entrada del sistema
    validacionDeIngreso = False
    while(not validacionDeIngreso):
        try:
            codigoDeBarras = input("Esperando lectura de scanner...")
            print("Lectura de scanner recibida, OK!")
        except:
            print("ERROR!!")
            validacionDeIngreso = False

        # Verifico el codigo
        if (len(codigoDeBarras) == 13):
            try:
                for digito in codigoDeBarras:
                    if digito not in string.digits:
                        validacionDeIngreso = False
                codigoDeBarras = int(codigoDeBarras)
                validacionDeIngreso = True
            except:
                print("ERROR!!")
                validacionDeIngreso = False
        else:
            print("ERROR!!")
            validacionDeIngreso = False

    return codigoDeBarras

def ingresoDePrecio():
    # Leo entrada del sistema
    validacionDeIngreso = False
    poseePunto = False
    while (not validacionDeIngreso):
        try:
            precio = float(input("Esperando ingreso del precio..."))
            print("Ingreso de precio, OK!")
            validacionDeIngreso = True
        except:
            print("ERROR!!")
            validacionDeIngreso = False
    return precio


def ingresoNumeroDelCliente():
    # Leo entrada del sistema
    validacionDeIngreso = False
    while (not validacionDeIngreso):
        try:
            numeroDelCliente = input("Esperando ingreso del numero del cliente...")
        except:
            print("ERROR!!")
            validacionDeIngreso = False

        # Verifico el numero
        if(len(numeroDelCliente)== 8 or len(numeroDelCliente)== 10 ):
            try:
                for digito in str(numeroDelCliente):
                    if digito not in string.digits:
                        validacionDeIngreso = False
                validacionDeIngreso = True
                numeroDelCliente = int(numeroDelCliente)
            except:
                print("ERROR!!")
                validacionDeIngreso = False
        else:
            print("ERROR!!")
            validacionDeIngreso = False

    return numeroDelCliente

def ingresoNombre(nombreDelCampo):
    # Leo entrada del sistema
    #  Verifico el nombre del campo afectado
    validacionDeIngreso = False
    while (not validacionDeIngreso):
        if(type(nombreDelCampo) is str):

            try:
                nombre = input('Esperando ingreso del nombre de {}...'.format(nombreDelCampo))
                print('Ingreso de nombre de {}, OK!'.format(nombreDelCampo))
                if(type(nombre)is str):
                    validacionDeIngreso = True
            except:
                print("ERROR!!")
                validacionDeIngreso = False

        else:
            print("ERROR!!")
            validacionDeIngreso = False

    return nombre

def ingresoDeArea():
    validacionDeIngreso = False
    comandoSQL = 'SELECT * FROM AREAS;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaDeAreas = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    comandoSQL = 'SELECT MAX(ID_AREA) FROM AREAS ;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    maximoIDdeArea = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    maximoIDdeArea = maximoIDdeArea[0]
    print(tablaDeAreas)
    print('El numero maximo de registros de areas es {}'.format(str(maximoIDdeArea)) )
    while(not validacionDeIngreso):
        try:
            areaIngresada = int(input("Esperando ingreso de area..."))
            if(areaIngresada <= maximoIDdeArea and areaIngresada > 0):
                validacionDeIngreso = True
            else:
                print("ERROR!!")
                validacionDeIngreso = False
        except:
            print("ERROR!!")
            validacionDeIngreso = False

    return areaIngresada




