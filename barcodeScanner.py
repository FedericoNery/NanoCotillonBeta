import string

def entradaScanner():
    # Leo entrada del sistema
    try:
        print("Esperando lectura de scanner...")
        codigo = input()
        print("Lectura de scanner recibida, OK!")
    except:
        return None

    # Verifico el codigo
    if len( codigo ) == 13:
        try:
            for s in codigo:
                if s not in string.digits:
                    return None
            codigo = int(codigo)
        except:
            return None
    else: return None

    return codigo
