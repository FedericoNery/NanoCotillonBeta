import ingreso_de_datos
import funciones_SQLite
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def eliminarArticulo():
    codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
    comandoSQL = 'UPDATE ARTICULOS SET ALTA_BAJA = 0 WHERE CODIGO_DE_BARRA = {} '.format(str(codigoDeBarras))
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

def eliminarCliente():
    nombreCliente = ingreso_de_datos.ingresoNombre("Cliente")
    existeCliente = verificarSiExisteCliente(nombreCliente)
    if(existeCliente):
        comandoSQL = 'UPDATE CLIENTES SET ALTA_BAJA = 0 WHERE NOMBRE = "{}"'.format(nombreCliente)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("No existe el cliente")

def eliminarMarca():
    nombreMarca = ingreso_de_datos.ingresoNombre("Marca")
    existeMarca = verificarSiExisteMarca(nombreMarca)
    if (existeMarca):
        comandoSQL = 'UPDATE MARCAS SET ALTA_BAJA = 0 WHERE NOMBRE_MARCA = "{}"'.format(nombreMarca)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("No existe el cliente")

def verificarSiExisteCliente(nombreCliente):
    comandoSQL = "SELECT * FROM CLIENTES;"
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaClientes = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    for cliente in tablaClientes:
        if(cliente[1] == nombreCliente):
            return True
    return False

def verificarSiExisteMarca(nombreMarca):
    comandoSQL = "SELECT * FROM MARCAS;"
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaMarcas = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    for marca in tablaMarcas:
        if(marca[1] == nombreMarca):
            return True
    return False