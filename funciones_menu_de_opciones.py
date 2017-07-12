import agregarRegistros
import modificarRegistros
import eliminarRegistros
import facturacion
import crear_base_de_datos

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
        eliminarRegistros.eliminarArticulo()
    elif(numeroDeOpcion == 5):
        eliminarRegistros.eliminarCliente()
    elif(numeroDeOpcion == 6):
        eliminarRegistros.eliminarMarca()
    elif(numeroDeOpcion == 7):
        modificarRegistros.modificarArticulo()
    elif(numeroDeOpcion == 8):
        modificarRegistros.modificarCliente()
    elif(numeroDeOpcion == 9):
        modificarRegistros.modificarMarca()
    elif(numeroDeOpcion == 10):
        facturacion.crearFactura()
    elif(numeroDeOpcion == 11):
        facturacion.imprimirFactura()
    elif(numeroDeOpcion == 12):
        crear_base_de_datos.crearBaseDeDatosNueva()




