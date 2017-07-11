import ingreso_de_datos
import funciones_SQLite
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos
from eliminarRegistros import verificarSiExisteMarca
def agregarArticulo():
    codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()


    validacionParaAgregarRegistro = verificarQueNoExistaElArticulo(codigoDeBarras)
    if(validacionParaAgregarRegistro):
        nombreDelArticulo = ingreso_de_datos.ingresoNombre("Articulo")
        nombreDeLaMarcaDelArticulo = ingreso_de_datos.ingresoNombre("Marca")
        precioDelArticulo = ingreso_de_datos.ingresoDePrecio()
        numeroDeAreaDelArticulo = ingreso_de_datos.ingresoDeArea()
        existeMarca = verificarSiExisteMarca(nombreDeLaMarcaDelArticulo)
        if (existeMarca):
            numeroDeMarcaDelArticulo = ingreso_de_datos.determinarNumeroDeMarcaDelArticulo(nombreDeLaMarcaDelArticulo)
        else:
            comandoSQL = 'INSERT INTO MARCAS (NOMBRE_MARCA) VALUES("{}")'.format(nombreDeLaMarcaDelArticulo)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
            funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
        numeroDeMarcaDelArticulo = ingreso_de_datos.determinarNumeroDeMarcaDelArticulo(nombreDeLaMarcaDelArticulo)
        stockDelArticulo = ingreso_de_datos.ingresoCantidadDeStock()

        comandoSQL = 'INSERT INTO ARTICULOS (CODIGO_DE_BARRA, NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA,ARTICULO_AREA,STOCK,ALTA_BAJA)' \
                 'VALUES({},"{}",{},{},{},{},{});'\
        .format(codigoDeBarras,nombreDelArticulo,precioDelArticulo,numeroDeMarcaDelArticulo,numeroDeAreaDelArticulo,stockDelArticulo,str(1))
        funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("Ya existe ese articulo ")

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
    noExisteCliente = verificarQueNoExistaElCliente(nombreDelCliente)
    if(noExisteCliente):
        numeroDeTelefonoDelCliente = ingreso_de_datos.ingresoNumeroDelCliente()
        comandoSQL = 'INSERT INTO CLIENTES(NOMBRE,NUMERO_TELEFONO) VALUES("{}",{});'.format(nombreDelCliente,numeroDeTelefonoDelCliente)
        funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
        funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
    else:
        print("Ya existe el cliente")

def verificarQueNoExistaElCliente(nombreDelCliente):
    comandoSQL = 'SELECT NOMBRE FROM CLIENTES;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaNombresDeClientes = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    for nombre in tablaNombresDeClientes:
        if(nombre[0] == nombreDelCliente):
            return False
    return True

def verificarQueNoExistaElArticulo(codigoDeBarras):
    comandoSQL = 'SELECT CODIGO_DE_BARRA FROM ARTICULOS;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaConCodigosDeBarra = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    for codigo in tablaConCodigosDeBarra:
        if(codigo[0] == int(codigoDeBarras)):
            return False
    return True
