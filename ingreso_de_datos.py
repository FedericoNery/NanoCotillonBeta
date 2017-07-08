import string

def ingresoCodigoDeBarras():
    # Leo entrada del sistema
    try:
        print("Esperando lectura de scanner...")
        codigoDeBarras = input()
        print("Lectura de scanner recibida, OK!")
    except:
        return None

    # Verifico el codigo
    if len( codigoDeBarras ) == 13:
        try:
            for digito in codigoDeBarras:
                if digito not in string.digits:
                    return None
            codigoDeBarras = int(codigoDeBarras)
        except:
            return None
    else: return None

    return codigoDeBarras

def