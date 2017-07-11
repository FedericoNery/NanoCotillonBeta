import ingreso_de_datos
import funciones_SQLite
import funciones_para_modificar_articulo
import funciones_para_modificar_cliente
from eliminarRegistros import verificarSiExisteCliente
from eliminarRegistros import verificarSiExisteMarca
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def modificarArticulo():
    tablaDatosDelArticulo = extraerDatosDelArticuloAModificar()

    antiguoNombre = tablaDatosDelArticulo[0][0]
    antiguoPrecio = tablaDatosDelArticulo[0][1]
    antiguoIDMarca = tablaDatosDelArticulo[0][2]
    antiguoIDArea = tablaDatosDelArticulo[0][3]
    antiguoStock = tablaDatosDelArticulo[0][4]
    codigoDeBarras = tablaDatosDelArticulo[0][5]

    mensaje = "¿Que campos desea modificar?"

    nombreNuevo = funciones_para_modificar_articulo.modificarNombre(antiguoNombre)
    nombreDeMarcaNuevo = funciones_para_modificar_articulo.modificarMarca(antiguoIDMarca)#Ver futuros problemas
    precioNuevo = funciones_para_modificar_articulo.modificarPrecio(antiguoPrecio)
    stockNuevo = funciones_para_modificar_articulo.modificarStock(antiguoStock)#Ver futuros problemas
    areaNueva = funciones_para_modificar_articulo.modificarArea(antiguoIDArea)#Ver futuros problemas

    numeroDeIDDeLaMarca = ingreso_de_datos.determinarNumeroDeMarcaDelArticulo(nombreDeMarcaNuevo)
    if (numeroDeIDDeLaMarca == None):
        comandoSQL = 'INSERT INTO MARCAS (NOMBRE_MARCA,ALTA_BAJA) VALUES("{}",1)'.format(nombreDeMarcaNuevo)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

    if(nombreDeMarcaNuevo != antiguoIDMarca):
        comandoSQL = 'UPDATE ARTICULOS SET NOMBRE_ARTICULO = "{}", PRECIO = {} ,' \
                 'ARTICULO_MARCA = (SELECT ID_MARCA FROM MARCAS WHERE NOMBRE_MARCA = "{}"),' \
                 'ARTICULO_AREA = {} ,STOCK = {}' \
                 ' WHERE CODIGO_DE_BARRA = {} ;'\
        .format(nombreNuevo,str(precioNuevo),nombreDeMarcaNuevo,str(areaNueva),str(stockNuevo),str(codigoDeBarras))

    else:

        comandoSQL = 'UPDATE ARTICULOS SET NOMBRE_ARTICULO = "{}", PRECIO = {} ,' \
                 'ARTICULO_MARCA = {},' \
                 'ARTICULO_AREA = {} ,STOCK = {}' \
                 'WHERE CODIGO_DE_BARRA = {} ;'\
        .format(nombreNuevo,str(precioNuevo),nombreDeMarcaNuevo,str(areaNueva),str(stockNuevo),str(codigoDeBarras))


    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

def modificarCliente():
    nombreAModificar = ingreso_de_datos.ingresoNombre("Cliente a modificar")
    existeCliente = verificarSiExisteCliente(nombreAModificar)
    if(existeCliente):
        tablaDatosDelCliente = extraerDatosDelClienteAModificar(nombreAModificar)
        antiguoNombre = tablaDatosDelCliente[0]
        antiguoNumero = tablaDatosDelCliente[1]
        nuevoNombre = funciones_para_modificar_cliente.modificarNombre(antiguoNombre)
        nuevoNumero = funciones_para_modificar_cliente.modificarNumero(antiguoNumero)
        comandoSQL = 'UPDATE CLIENTES SET NOMBRE = "{}",NUMERO_TELEFONO = {} ;'.format(nuevoNombre,nuevoNumero)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("No existe ese cliente")

def modificarMarca():
    nombreAModificar = ingreso_de_datos.ingresoNombre("Marca a modificar")
    existeMarca = verificarSiExisteMarca(nombreAModificar)
    if (existeMarca):
        IDMarcaAntiguo = ingreso_de_datos.determinarNumeroDeMarcaDelArticulo(nombreAModificar)
        nombreNuevo = ingreso_de_datos.ingresoNombre("Nueva Marca")
        comandoSQL = 'UPDATE MARCAS SET NOMBRE_MARCA = "{}" WHERE ID_MARCA = {} '.format(nombreNuevo,IDMarcaAntiguo)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("No existe ese cliente")

def extraerDatosDelArticuloAModificar():
    codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
    comandoSQL = "SELECT NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA,ARTICULO_AREA,STOCK,CODIGO_DE_BARRA" \
                 " FROM ARTICULOS WHERE CODIGO_DE_BARRA = {}".format(str(codigoDeBarras))
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    tablaDatosDelArticulo = funciones_SQLite.extraerTabla(cursorBaseDeDatos)

    print("Los datos del articulo a modificar son: ")
    print(tablaDatosDelArticulo)
    return tablaDatosDelArticulo

def extraerDatosDelClienteAModificar(nombreAModificar):
    comandoSQL = 'SELECT NOMBRE,NUMERO_TELEFONO FROM CLIENTES WHERE NOMBRE = "{}";'.format(nombreAModificar)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaDatosDelCliente = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    return tablaDatosDelCliente

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

