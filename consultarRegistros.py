import funciones_SQLite
import ingreso_de_datos
import datetime
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def buscarPrecioDeUnArticulo():
    codigoDeBarrasDelArticuloBuscado = ingreso_de_datos.ingresoCodigoDeBarras()
    comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO,ARTICULOS.STOCK, MARCAS.NOMBRE_MARCA FROM (ARTICULOS) INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE CODIGO_DE_BARRA ={};'.format(codigoDeBarrasDelArticuloBuscado)

    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    articuloBuscado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    print(articuloBuscado)

def buscarPorArea():
    numeroDeArea = ingreso_de_datos.ingresoDeArea()
    comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO, MARCAS.NOMBRE_MARCA FROM ARTICULOS INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE ARTICULO_AREA = {};'.format(numeroDeArea)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosDelArea = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaArticulosDelArea)

def buscarPorPalabraClave():
    palabraClave = ingreso_de_datos.ingresoNombre("palabra clave")
    palabraClave = palabraClave.upper()
    comandoSQL = 'SELECT CODIGO_DE_BARRA,NOMBRE_ARTICULO FROM ARTICULOS WHERE NOMBRE_ARTICULO LIKE "%{}%";'.format(palabraClave,palabraClave,palabraClave)
    #
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosPorPalabraClave = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaArticulosPorPalabraClave)


def buscarPorFechaDeActualizacion():
    fechaDeIngreso = ingreso_de_datos.ingresoFecha()
    comandoSQL = 'SELECT * FROM ARTICULOS WHERE FECHA = {};'.format(fechaDeIngreso)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosPorFecha = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaArticulosPorFecha)

def productosSinStock():
    comandoSQL = 'SELECT * FROM ARTICULOS WHERE STOCK = 0;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosSinStock = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaArticulosSinStock)

def totalDelDia():
    fechaDeHoy = datetime.datetime.date()
    comandoSQL = 'SELECT * FROM FACTURAS WHERE FECHA={};'.format(fechaDeHoy)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaTotal = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaTotal)
