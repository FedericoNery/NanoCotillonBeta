import agregarRegistros
import modificarRegistros
import eliminarRegistros

def ingresoOpcionDelMenuElegida():
    validacionDeIngreso = False
    while(not validacionDeIngreso):
        try:
            numeroDeOpcion = int(input("Ingrese el numero de opcion: "))
            if(numeroDeOpcion > 0 and numeroDeOpcion < 10):
                validacionDeIngreso = True
                return numeroDeOpcion
            else:
                print("ERROR!!")
                validacionDeIngreso = False
        except:
            print("ERROR!!")
            validacionDeIngreso = False

def seleccionarOpcionDelMenuElegida(numeroDeOpcion):
    if(numeroDeOpcion == 1):
        agregarRegistros.agregarArticulo()
    elif(numeroDeOpcion == 2):
        agregarRegistros.agregarCliente()
    elif(numeroDeOpcion == 3):
        agregarRegistros.agregarMarca()
    elif(numeroDeOpcion == 4):
        modificarRegistros.modificarArticulo()
    elif(numeroDeOpcion == 5):
        modificarRegistros.modificarCliente()
    elif(numeroDeOpcion == 6):
        modificarRegistros.modificarMarca()
    elif(numeroDeOpcion == 7):
        eliminarRegistros.eliminarArticulo()
    elif(numeroDeOpcion == 8):
        eliminarRegistros.eliminarCliente()
    elif(numeroDeOpcion == 9):
        eliminarRegistros.eliminarMarca()

