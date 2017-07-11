import modificarRegistros
import ingreso_de_datos

def modificarNumero(antiguoNumero):
    modificacionDeArea = modificarRegistros.validacionDeModificacion("Numero de telefono")
    if (modificacionDeArea):
        nuevoNumero = ingreso_de_datos.ingresoNumeroDelCliente()
    else:
        nuevoNumero = antiguoNumero
    return nuevoNumero

def modificarNombre(antiguoNombre):
    modificacionDeNombre = modificarRegistros.validacionDeModificacion("Nombre")
    if (modificacionDeNombre):
        nombreNuevo = ingreso_de_datos.ingresoNombre("Cliente")
    else:
        nombreNuevo = antiguoNombre
    return nombreNuevo