import ingreso_de_datos
import funciones_SQLite
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def agregarArticulo():
    codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
    nombreDelArticulo = ingreso_de_datos.ingresoNombre("Articulo")
    nombreDeLaMarcaDelArticulo = ingreso_de_datos.ingresoNombre("Marca")
    precioDelArticulo = ingreso_de_datos.ingresoDePrecio()
    numeroDeAreaDelArticulo = ingreso_de_datos.ingresoDeArea()
    numeroDeMarcaDelArticulo = ingreso_de_datos.determinarNumeroDeMarcaDelArticulo(nombreDeLaMarcaDelArticulo)
    stockDelArticulo = ingreso_de_datos.ingresoCantidadDeStock()

    comandoSQL = 'INSERT INTO ARTICULOS (CODIGO_DE_BARRA, NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA,ARTICULO_AREA,STOCK,ALTA_BAJA)' \
                 'VALUES({},"{}",{},{},{},{},{});'\
    .format(codigoDeBarras,nombreDelArticulo,precioDelArticulo,numeroDeMarcaDelArticulo,numeroDeAreaDelArticulo,stockDelArticulo,str(1))

    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

def agregarMarca():
    nombreDeLaMarca = ingreso_de_datos.ingresoNombre("Marca")
    numeroDeIDDeLaMarca = ingreso_de_datos.determinarNumeroDeMarcaDelArticulo(nombreDeLaMarca)
    if(numeroDeIDDeLaMarca == None):
        comandoSQL = 'INSERT INTO MARCAS (NOMBRE_MARCA) VALUES("{}")'.format(nombreDeLaMarca)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("Ya existe la marca ")

def agregarCliente():
    nombreDelCliente = ingreso_de_datos.ingresoNombre("Cliente")
    numeroDeTelefonoDelCliente = ingreso_de_datos.ingresoNumeroDelCliente()
    comandoSQL = 'INSERT INTO CLIENTES(NOMBRE,NUMERO_TELEFONO) VALUES("{}",{});'.format(nombreDelCliente,numeroDeTelefonoDelCliente)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    funciones_SQLite.guardarBaseDeDatos(baseDeDatos)