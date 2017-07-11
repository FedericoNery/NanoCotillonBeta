import funciones_SQLite
import ingreso_de_datos
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def buscarPrecioDeUnArticulo():
    codigoDeBarrasDelArticuloBuscado = ingreso_de_datos.ingresoCodigoDeBarras()
    comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO, MARCAS.NOMBRE_MARCA' \
                 'FROM ARTICULOS INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA ' \
                 'WHERE CODIGO_DE_BARRA ={}'.format(codigoDeBarrasDelArticuloBuscado)

    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    articuloBuscado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    print(articuloBuscado)

def buscarPorArea():
    numeroDeArea = ingreso_de_datos.ingresoDeArea()
    comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO, MARCAS.NOMBRE_MARCA ' \
                 'FROM ARTICULOS INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE ARTICULO_AREA = {};'.format(numeroDeArea)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosDelArea = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaArticulosDelArea)

def buscarPorPalabraClave():
    palabraClave = ingreso_de_datos.ingresoNombre("palabra clave")
    comandoSQL = 'SELECT * FROM ARTICULOS WHERE NOMBRE_ARTICULO LIKE "%{}" OR NOMBRE_ARTICULO LIKE "{}%" OR NOMBRE_ARTICULO LIKE "%{}%"'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosPorPalabraClave = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaArticulosPorPalabraClave)


def buscarPorFechaDeActualizacion():
    fechaDeIngreso = ingreso_de_datos.ingresoFecha()
