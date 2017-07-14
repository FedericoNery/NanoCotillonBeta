import ingreso_de_datos
import modificarRegistros

def modificarNombre(antiguoNombre):
    modificacionDeNombre = modificarRegistros.validacionDeModificacion("Nombre")
    if (modificacionDeNombre):
        nombreNuevo = ingreso_de_datos.ingresoNombre("Articulo")
    else:
        nombreNuevo = antiguoNombre
    return nombreNuevo

def modificarPrecio (antiguoPrecio):
    modificacionDePrecio =modificarRegistros. validacionDeModificacion("Precio")
    if(modificacionDePrecio):
        precioNuevo = ingreso_de_datos.ingresoDePrecio()
    else:
        precioNuevo = antiguoPrecio
    return precioNuevo

def modificarMarca(antiguoMarca):
    modificacionDeMarca = modificarRegistros.validacionDeModificacion("Marca")
    if (modificacionDeMarca):
        nombreDeMarcaNuevo = ingreso_de_datos.ingresoNombre("Marca")
    else:
        nombreDeMarcaNuevo = antiguoMarca
    return nombreDeMarcaNuevo

def modificarStock(antiguoStock):
    modificacionDeStock = modificarRegistros.validacionDeModificacion("Stock")
    if (modificacionDeStock):
        cantidadDeStockNuevo = ingreso_de_datos.ingresoCantidadDeStock()
    else:
        cantidadDeStockNuevo = antiguoStock
    return cantidadDeStockNuevo

def modificarArea(antiguaArea):
    modificacionDeArea = modificarRegistros.validacionDeModificacion("Area")
    if (modificacionDeArea):
        nuevaArea = ingreso_de_datos.ingresoDeArea()
    else:
        nuevaArea = antiguaArea
    return nuevaArea

