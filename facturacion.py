from funciones_SQLite import cursorBaseDeDatos
from funciones_SQLite import baseDeDatos
from eliminarRegistros import verificarSiExisteCliente
import funciones_SQLite
import datetime
import ingreso_de_datos
import agregarRegistros

def crearFactura():
    idDeUltimaFactura = extraerIDDeLaUltimaFactura()

    validacionSeguirFacturando = True
    while(validacionSeguirFacturando):
        codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
        existeArticulo = verificarQueExistaElArticulo(codigoDeBarras)
        if(not existeArticulo):
            agregarRegistros.agregarArticulo()

        print("Ingrese stock deseado")
        cantidadDelArticulo = ingreso_de_datos.ingresoCantidadDeStock()
        cantidadDelArticulo = int(cantidadDelArticulo)

        sePoseeElStockDeseado = verificarStockDisponible(codigoDeBarras,cantidadDelArticulo)
        if(sePoseeElStockDeseado):
            nombreDelCliente = ingreso_de_datos.ingresoNombre("Cliente")
            existeCliente = verificarSiExisteCliente(nombreDelCliente)

            if(not existeCliente):
                agregarRegistros.agregarCliente()

            comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA,ARTICULOS.NOMBRE_ARTICULO,' \
                     ' MARCAS.ID_MARCA, ARTICULOS.PRECIO FROM ARTICULOS,MARCAS WHERE ARTICULOS.CODIGO_DE_BARRA = {}'.format(codigoDeBarras)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
            articuloConsultado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
            codigoDeBarrasDelArticulo = articuloConsultado[0]
            precioDelArticulo = articuloConsultado[3]

            comandoSQL = 'INSERT INTO ART_FACT(ID_ART,ID_FACT,CANTIDAD,PRECIO) VALUES({},{},{},{});'\
            .format(codigoDeBarrasDelArticulo,str(idDeUltimaFactura),cantidadDelArticulo,str(precioDelArticulo))
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)

            comandoSQL = 'INSERT INTO FACTURAS (ID_CLIENTE) VALUES ((SELECT ID FROM CLIENTES WHERE NOMBRE = "{}"));'.format(nombreDelCliente)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
            funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
            validacionSeguirFacturando = deseaSeguirIngresandoArticulosALaFactura()
        else:
            validacionSeguirFacturando = deseaSeguirIngresandoArticulosALaFactura()

def extraerIDDeLaUltimaFactura():
    comandoSQL = 'SELECT MAX(ID_FACT) FROM ART_FACT;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    idDeUltimaFactura = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    idDeUltimaFactura = idDeUltimaFactura[0] + 1
    return idDeUltimaFactura

def deseaSeguirIngresandoArticulosALaFactura():
    validacionDeIngreso = False
    while(not validacionDeIngreso):
        try:
            caracterVerificacion = input("Ingrese si desea seguir o no. [s/n]")
            if (caracterVerificacion == 'n'):
                return False
            elif(caracterVerificacion == 's'):
                return True
            else:
                print("ERROR!!")
                validacionDeIngreso = False
        except:
            print("ERROR!!")
            validacionDeIngreso = False

def imprimirFactura():
    total = 0
    numeroDeFacturaDeseada = obtenerNumeroDeFacturaDeseada()

    comandoSQL = 'SELECT FECHA FROM FACTURAS WHERE ID_FACTURA={}'.format(str(numeroDeFacturaDeseada))
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    fechaDeLaFactura = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    fechaDeLaFactura = fechaDeLaFactura[0]
    fechaDeLaFactura = datetime.strptime("2017-06-07 23:06:28", "%Y-%m-%d %H:%M:%S")
    fechaDeLaFactura = fechaDeLaFactura.strftime("%d/%m/%y")


    comandoSQL = 'SELECT FACTURAS.ID_CLIENTE, CLIENTES.NOMBRE FROM FACTURAS INNER JOIN CLIENTES ON FACTURAS.ID_CLIENTE = CLIENTES.ID_CLIENTE ' \
                 'WHERE FACTURAS.ID_FACTURAS = {};'.format(numeroDeFacturaDeseada)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaFechaYNumeroDeCliente = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    numeroDeCliente = tablaFechaYNumeroDeCliente[0]
    comandoSQL = 'SELECT ART_FACT.ID_ART,ARTICULOS.NOMBRE_ARTICULO,ART_FACT.CANTIDAD,ART_FACT.PRECIO FROM ART_FACT ' \
                 'INNER JOIN ARTICULOS ON ARTICULOS.CODIGO_DE_BARRA = ART_FACT.ID_ART WHERE ID_FACT ={};'.format(str(numeroDeFacturaDeseada))
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    tablaArticulosFacturas = funciones_SQLite.extraerTabla(cursorBaseDeDatos)

    comandoSQL = 'SELECT NOMBRE, NUMERO_TELEFONO FROM CLIENTES WHERE ID_CLIENTE = {}'.format(numeroDeCliente)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    tablaCliente = funciones_SQLite.extraerElemento(cursorBaseDeDatos)

    print("FECHA:{:<20} ".format(fechaDeLaFactura) + "Cliente:{:<20} " .format(tablaCliente[0]) )
    print("Nro De CUIT:{:<14} " .format (str(tablaCliente[1]))+"Razon Social:{:<17} ".format(tablaCliente[2]))

    print("---------------------------------------------------------------------------------------------------")
    encabezado = ["Codigo de Producto","Nombre/Descripcion","Cantidad ","Precio Por Unidad","Total"]
    print('|{:<20} '.format(encabezado[0]) + '|{:<20} '.format(encabezado[1]) + '|{:<20} '.format(encabezado[2]) + '|{:<20} '.format(encabezado[3])+ '|{:<9}|'.format(encabezado[4]))

    for i in tablaArticulosFacturas:
       print('|{:<20} '.format(i[0]) +'|{:<20} '.format(i[1])+'|{:<20} '.format(i[2])+'|{:<20} '.format(i[3])+'|{}{:<8}|'.format("$",str(int(i[3])*int(i[2]))))

    print("---------------------------------------------------------------------------------------------------")
    for i in tablaArticulosFacturas:
        total = int(i[3])*int(i[2]) + total

    print("Subtotal:{}{} ".format("$",total))
    print("IVA:{}{}".format("$",total*0.21))
    print("Total:{}{}".format("$",total+total*0.21))

def obtenerNumeroDeFacturaDeseada():
    tablaNuevaDeNumerosDeFacturas = []
    comandoSQL = 'SELECT ID_FACTURA,FECHA FROM FACTURAS;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    numerosDeFacturas = funciones_SQLite.extraerTabla(cursorBaseDeDatos)
    for i in numerosDeFacturas:
        tablaNuevaDeNumerosDeFacturas.append(i[0])
        print(i[0])

    validacionNumeroDeFactura = False
    while (not validacionNumeroDeFactura):
        numeroDeFacturaDeseada = input("Ingrese el numero de factura que desea imprimir ")
        if (int(numeroDeFacturaDeseada) <= max(tablaNuevaDeNumerosDeFacturas)):
            validacionNumeroDeFactura = True
        else:
            print("Error")
    return numeroDeFacturaDeseada

def verificarQueExistaElArticulo(codigoDeBarra):
    comandoSQL = 'SELECT * FROM ARTICULOS WHERE CODIGO_DE_BARRA = {}'.format(codigoDeBarra)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    articuloBuscado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    if(articuloBuscado == None):
        return False
    else:
        return True

def verificarStockDisponible(codigoDeBarra,stockDeseado):
    comandoSQL = 'SELECT STOCK FROM ARTICULOS WHERE CODIGO_DE_BARRA = {};'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    stockDisponible = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    stockDisponible = stockDisponible[0]
    if(stockDisponible < stockDeseado):
        print("Solo quedan disponibles {} unidades".format(stockDisponible))
        return False
    else:
        return True
