import string

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
                validacionDeIngreso = True
            except:
                print("ERROR!!")
                validacionDeIngreso = False
        else:
            print("ERROR!!")
            validacionDeIngreso = False

    return nombre

"""
def ingresoNombreDelCliente(nombreDelCampo):
    try:
        print("Esperando ingreso del nombre del cliente...")
        nombreDelCliente = input()
        print("Ingreso de nombre del cliente, OK!")
    except:
        return None

def ingresoNombreDeArticulo():
    try:
        print("Esperando ingreso del nombre del articulo...")
        nombreDelArticulo = input()
        print("Ingreso del nombre del articulo, OK!")
    except:
        return None

def ingresoNombreDeLaMarca():
    try:
        print("Esperando ingreso del nombre de la marca...")
        nombreDeLaMarca = input()
        print("Ingreso del nombre de la marca, OK!")
    except:
        return None

"""


