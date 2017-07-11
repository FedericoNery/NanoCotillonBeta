import ingreso_de_datos
import funciones_SQLite
import funciones_para_modificar_articulo
from eliminarRegistros import verificarSiExisteCliente
from eliminarRegistros import verificarSiExisteMarca
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def modificarArticulo():
    tablaDatosDelArticulo = extraerDatosDelArticuloAModificar()

    antiguoNombre = tablaDatosDelArticulo[0]
    antiguoPrecio = tablaDatosDelArticulo[1]
    antiguoIDMarca = tablaDatosDelArticulo[2]
    antiguoIDArea = tablaDatosDelArticulo[3]
    antiguoStock = tablaDatosDelArticulo[4]
    codigoDeBarras = tablaDatosDelArticulo[5]

    mensaje = "¿Que campos desea modificar?"

    nombreNuevo = funciones_para_modificar_articulo.modificarNombre(antiguoNombre)
    nombreDeMarcaNuevo = funciones_para_modificar_articulo.modificarMarca(antiguoIDMarca)#Ver futuros problemas
    precioNuevo = funciones_para_modificar_articulo.modificarPrecio(antiguoPrecio)
    stockNuevo = funciones_para_modificar_articulo.modificarStock(antiguoStock)#Ver futuros problemas
    areaNueva = funciones_para_modificar_articulo.modificarArea(antiguoIDArea)#Ver futuros problemas

    comandoSQL = 'UPDATE ARTICULOS SET (NOMBRE_ARTICULO = "{}", PRECIO = {} ,' \
                 'ARTICULO_MARCA = (SELECT FROM MARCAS WHERE NOMBRE_MARCA = "{}"),' \
                 'ARTICULO_AREA = {} ,STOCK = {})' \
                 'WHERE CODIGO_DE_BARRA = {} ;'\
        .format(nombreNuevo,str(precioNuevo),nombreDeMarcaNuevo,str(areaNueva),str(stockNuevo),str(codigoDeBarras))

    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

def modificarCliente():
    nombreAModificar = ingreso_de_datos.ingresoNombre("Cliente")
    existeCliente = verificarSiExisteCliente(nombreAModificar)
    if(existeCliente):
        comandoSQL = 'UPDATE CLIENTES SET(NOMBRE_CLIENTE = "{}")'.format(nombreAModificar)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("No existe ese cliente")

def modificarMarca():
    nombreAModificar = ingreso_de_datos.ingresoNombre("Marca")
    existeMarca = verificarSiExisteMarca(nombreAModificar)
    if (existeMarca):
        comandoSQL = 'UPDATE MARCAS SET(NOMBRE_MARCA = "{}")'.format(nombreAModificar)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("No existe ese cliente")

def extraerDatosDelArticuloAModificar():
    codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
    comandoSQL = "SELECT NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA,ARTICULO_AREA,STOCK" \
                 " FROM ARTICULOS WHERE CODIGO_DE_BARRA = {}".format(str(codigoDeBarras))
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    tablaDatosDelArticulo = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    tablaDatosDelArticulo.append(codigoDeBarras)
    print("Los datos del articulo a modificar son: ")
    print(tablaDatosDelArticulo)
    return tablaDatosDelArticulo

def validacionDeModificacion(nombreDelCampoAModificar):
    validacionDeIngreso = False
    while(not validacionDeIngreso):
        try:
            if(type(nombreDelCampoAModificar)is str):
                modificar = input('¿Modifica {}? Ingrese "si" o "no"'.format(nombreDelCampoAModificar))
                modificar = modificar.upper()

                if(modificar == 'SI'):
                    return True
                elif(modificar == 'NO'):
                    return False

        except:
            print("ERROR!!")
            validacionDeIngreso = False

