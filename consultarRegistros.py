import funciones_SQLite
import ingreso_de_datos
import datetime
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos
from datetime import date
from datetime import datetime, date

def buscarPrecioDeUnArticulo():
    codigoDeBarrasDelArticuloBuscado = ingreso_de_datos.ingresoCodigoDeBarras()
    comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO,ARTICULOS.STOCK, MARCAS.NOMBRE_MARCA FROM (ARTICULOS) INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE CODIGO_DE_BARRA ={};'.format(codigoDeBarrasDelArticuloBuscado)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    articuloBuscado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    if(articuloBuscado == None):
        print("No se encuentra registrado el articulo!!!")
    else:
        encabezado = ["Codigo de Producto", "Nombre/Descripcion","Precio Por Unidad","Cantidad ", "Marca"]
        print('|{:<20} '.format(encabezado[0]) + '|{:<30} '.format(encabezado[1]) + '|{:<20} '.format(
        encabezado[2]) + '|{:<9} '.format(encabezado[3]) + '|{:<20}|'.format(encabezado[4]))
        print('|{:<20} '.format(articuloBuscado[0])+'|{:<30} '.format(articuloBuscado[1])+'|{:<20} '.format(articuloBuscado[2])+'|{:<9} '.format(articuloBuscado[3])+'|{:<20}|'.format(articuloBuscado[4]))

def buscarPorArea():
    numeroDeArea = ingreso_de_datos.ingresoDeArea()
    comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO, MARCAS.NOMBRE_MARCA FROM ARTICULOS INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE ARTICULO_AREA = {};'.format(numeroDeArea)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosDelArea = funciones_SQLite.extraerTabla(cursorBaseDeDatos)

    encabezado = ["Codigo de barra", "Nombre/Descripcion", "Precio", "Marca"]
    print("{:<20}".format(encabezado[0]) + "{:<30}".format(encabezado[1]) + "{:<10}".format(
        encabezado[2]) + "{:<10}".format(encabezado[3]))
    for articulo in tablaArticulosDelArea:
        print("{:<20}".format(articulo[0]) + "{:<30}".format(articulo[1]) + "{:<10}".format(
            articulo[2]) + "{:<10}".format(articulo[3]))


def buscarPorPalabraClave():
    palabraClave = ingreso_de_datos.ingresoNombre("palabra clave")
    palabraClave = palabraClave.upper()
    comandoSQL = 'SELECT CODIGO_DE_BARRA,NOMBRE_ARTICULO,PRECIO FROM ARTICULOS WHERE NOMBRE_ARTICULO LIKE "%{}%";'.format(palabraClave,palabraClave,palabraClave)
    #
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosPorPalabraClave = funciones_SQLite.extraerTabla(cursorBaseDeDatos)

    encabezado = ["Codigo de barra", "Nombre/Descripcion", "Precio"]
    print("{:<20}".format(encabezado[0]) + "{:<30}".format(encabezado[1]) + "{:<10}".format(
        encabezado[2]) )
    for articulo in tablaArticulosPorPalabraClave:
        print("{:<20}".format(articulo[0]) + "{:<30}".format(articulo[1]) + "{:<10}".format(
            articulo[2]) )



def buscarPorFechaDeActualizacion():
    fechaDeIngreso = ingreso_de_datos.ingresoYValidacionDeFecha()
    formatter_string = "%Y-%m-%d"
    datetime_object = datetime.strptime(fechaDeIngreso, formatter_string)
    date_object = datetime_object.date()
    comandoSQL = 'SELECT CODIGO_DE_BARRA,NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA FROM ARTICULOS WHERE FECHA LIKE "%{}%";'.format(date_object)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosPorFecha = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    encabezado = ["Codigo de barra","Nombre/Descripcion","Precio","Marca"]
    print("{:<20}".format(encabezado[0])+"{:<30}".format(encabezado[1])+"{:<10}".format(encabezado[2])+"{:<10}".format(encabezado[3]))
    for articulo in tablaArticulosPorFecha:
        print("{:<20}".format(articulo[0])+"{:<30}".format(articulo[1])+"{:<10}".format(articulo[2])+"{:<10}".format(articulo[3]))

def productosSinStock():
    comandoSQL = 'SELECT CODIGO_DE_BARRA,NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA FROM ARTICULOS WHERE STOCK = 0;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaArticulosSinStock = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    encabezado = ["Codigo de barra", "Nombre/Descripcion", "Precio", "Marca"]
    print("{:<20}".format(encabezado[0]) + "{:<30}".format(encabezado[1]) + "{:<10}".format(
        encabezado[2]) + "{:<10}".format(encabezado[3]))
    for articulo in tablaArticulosSinStock:
        print("{:<20}".format(articulo[0]) + "{:<30}".format(articulo[1]) + "{:<10}".format(
            articulo[2]) + "{:<10}".format(articulo[3]))

def totalDelDia():
    fechaDeHoy = date.today()
    comandoSQL = 'SELECT ID_FACTURA FROM FACTURAS WHERE FECHA LIKE "%{}%";'.format(fechaDeHoy)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaTotal = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    print(tablaTotal)



