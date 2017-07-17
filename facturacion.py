from funciones_SQLite import cursorBaseDeDatos
from funciones_SQLite import baseDeDatos
from eliminarRegistros import verificarSiExisteCliente
import funciones_SQLite
import datetime
import ingreso_de_datos
import agregarRegistros
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4





def crearFactura():
    idDeUltimaFactura = extraerIDDeLaUltimaFactura()

    nombreDelCliente = ingreso_de_datos.ingresoNombre("Cliente")
    existeCliente = verificarSiExisteCliente(nombreDelCliente)
    if (not existeCliente):
        print("No existe el cliente, debe agregarlo")
        agregarRegistros.agregarCliente()

    validacionSeguirFacturando = True
    while(validacionSeguirFacturando):
        codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
        existeArticulo = verificarQueExistaElArticulo(codigoDeBarras)
        if(not existeArticulo):
            agregarRegistros.agregarArticulo()

        print("Ingrese stock deseado")
        stockDeseadoDelArticulo = ingreso_de_datos.ingresoCantidadDeStock()
        stockDeseadoDelArticulo = int(stockDeseadoDelArticulo)

        sePoseeElStockDeseado = verificarStockDisponible(codigoDeBarras,stockDeseadoDelArticulo)

        if(sePoseeElStockDeseado):

            comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA,ARTICULOS.NOMBRE_ARTICULO,MARCAS.ID_MARCA, ARTICULOS.PRECIO FROM ARTICULOS,MARCAS WHERE ARTICULOS.CODIGO_DE_BARRA = {}'.format(codigoDeBarras)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
            articuloConsultado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
            codigoDeBarrasDelArticulo = articuloConsultado[0]
            precioDelArticulo = articuloConsultado[3]

            comandoSQL = 'INSERT INTO ART_FACT(ID_ART,ID_FACT,CANTIDAD,PRECIO) VALUES({},{},{},{});'\
            .format(codigoDeBarrasDelArticulo,str(idDeUltimaFactura),stockDeseadoDelArticulo,str(precioDelArticulo))
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)

            comandoSQL = 'INSERT INTO FACTURAS (ID_CLIENTE) VALUES ((SELECT ID_CLIENTE FROM CLIENTES WHERE NOMBRE = "{}"));'.format(nombreDelCliente)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
            funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
            validacionSeguirFacturando = deseaSeguirIngresandoArticulosALaFactura()

            comandoSQL = 'UPDATE ARTICULOS SET STOCK = (SELECT STOCK FROM ARTICULOS WHERE CODIGO_DE_BARRA = {})-{} WHERE CODIGO_DE_BARRA = {}'.format(codigoDeBarras,stockDeseadoDelArticulo,codigoDeBarras)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
            funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

        else:
            validacionSeguirFacturando = deseaSeguirIngresandoArticulosALaFactura()

def extraerIDDeLaUltimaFactura():
    comandoSQL = 'SELECT MAX(ID_FACT) FROM ART_FACT;'
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    idDeUltimaFactura = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    if(idDeUltimaFactura[0] == None):
        idDeUltimaFactura = 1
    else:
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
    fechaDeLaFactura = datetime.datetime.strptime(fechaDeLaFactura, "%Y-%m-%d %H:%M:%S")
    fechaDeLaFactura = fechaDeLaFactura.strftime("%d/%m/%y")


    comandoSQL = 'SELECT FACTURAS.ID_CLIENTE, CLIENTES.NOMBRE FROM FACTURAS INNER JOIN CLIENTES ON FACTURAS.ID_CLIENTE = CLIENTES.ID_CLIENTE WHERE FACTURAS.ID_FACTURA = {};'.format(numeroDeFacturaDeseada)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    tablaFechaYNumeroDeCliente = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    numeroDeCliente = tablaFechaYNumeroDeCliente[0]
    comandoSQL = 'SELECT ART_FACT.ID_ART,ARTICULOS.NOMBRE_ARTICULO,ART_FACT.CANTIDAD,ART_FACT.PRECIO FROM ART_FACT INNER JOIN ARTICULOS ON ARTICULOS.CODIGO_DE_BARRA = ART_FACT.ID_ART WHERE ID_FACT ={};'.format(str(numeroDeFacturaDeseada))
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    tablaArticulosFacturas = funciones_SQLite.extraerTabla(cursorBaseDeDatos)

    comandoSQL = 'SELECT NOMBRE, NUMERO_TELEFONO FROM CLIENTES WHERE ID_CLIENTE = {}'.format(numeroDeCliente)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
    tablaCliente = funciones_SQLite.extraerElemento(cursorBaseDeDatos)

    print("FECHA:{:<20} ".format(fechaDeLaFactura) + "Cliente:{:<20} " .format(tablaCliente[0]) )

    print("---------------------------------------------------------------------------------------------------")
    encabezado = ["Codigo de Producto","Nombre/Descripcion","Cantidad ","Precio Por Unidad","Total"]
    print('|{:<20} '.format(encabezado[0]) + '|{:<20} '.format(encabezado[1]) + '|{:<20} '.format(encabezado[2]) + '|{:<20} '.format(encabezado[3])+ '|{:<9}|'.format(encabezado[4]))

    for i in tablaArticulosFacturas:
       print('|{:<20} '.format(i[0]) +'|{:<20} '.format(i[1])+'|{:<20} '.format(i[2])+'|{:<20} '.format(i[3])+'|{}{:<8}|'.format("$",round(float(i[3])*float(i[2]),2)))

    print("---------------------------------------------------------------------------------------------------")
    for i in tablaArticulosFacturas:
        total = float(i[3])*float(i[2]) + total

    print("Subtotal:${0:.2f} ".format(round(total,2)))
    print("IVA:${0:.2f}".format(round(total*0.21,2)))
    print("Total:${0:.2f}".format(round(total+total*0.21,2)))

    nombreDeArchivo = "factura{}.pdf".format(numeroDeFacturaDeseada)
    canvasDelPDF = canvas.Canvas(nombreDeArchivo,pagesize=A4)
    canvasDelPDF.setLineWidth(.3)
    canvasDelPDF.setFont('Helvetica', 10)

    canvasDelPDF.drawString(30, 750, 'NANO COTILLON')
    canvasDelPDF.drawString(30, 735, 'ELSA EDIS CORREA')
    canvasDelPDF.drawString(500, 750, 'Fecha: {}'.format(str(fechaDeLaFactura)))
    canvasDelPDF.line(480, 747, 580, 747)

    canvasDelPDF.drawString(400, 725, "Nombre de cliente:{}".format(tablaCliente[0]))
    canvasDelPDF.line(378, 723, 580, 723)

    canvasDelPDF.drawString(30, 703, 'Nro de factura:{}'.format(numeroDeFacturaDeseada))
    canvasDelPDF.line(120, 700, 580, 700)
    canvasDelPDF.drawString(30, 690,'-------------------------------------------------------------------------------------------------------------------------------------------')
    canvasDelPDF.drawString(30, 670, encabezado[0])
    canvasDelPDF.drawString(150, 670, encabezado[1])
    canvasDelPDF.drawString(280, 670, encabezado[2])
    canvasDelPDF.drawString(350, 670, encabezado[3])
    canvasDelPDF.drawString(470, 670, encabezado[4])
    j = 0
    contador = 0
    ejeY = 670
    ejeX = 30
    for j in tablaArticulosFacturas:
        ejeY = ejeY - 25
        ejeX = 30
        canvasDelPDF.drawString(ejeX, ejeY, "{}".format(j[0]))
        ejeX = 150
        canvasDelPDF.drawString (ejeX,ejeY,"{}".format(j[1]))
        ejeX = 280
        canvasDelPDF.drawString (ejeX,ejeY,"{}".format(j[2]))
        ejeX = 350
        canvasDelPDF.drawString (ejeX,ejeY,"{}".format(j[3]))
        ejeX = 470
        canvasDelPDF.drawString(ejeX,ejeY,"${}".format(round(j[3]*j[2],2)))
    ejeY = ejeY - 25
    ejeX = 30
    canvasDelPDF.drawString(ejeX,ejeY,'-----------------------------------------------------------------------------------------------------------------------------------------')
    ejeY = ejeY - 25
    canvasDelPDF.drawString(ejeX,ejeY,"Subtotal: ${}".format(round(total,2)))
    ejeY = ejeY - 25
    canvasDelPDF.drawString(ejeX, ejeY, "IVA: ${}".format(round(total*0.21,2)))
    ejeY = ejeY - 25
    canvasDelPDF.drawString(ejeX, ejeY, "Total: ${}".format(round(total+total*0.21,2)))

    canvasDelPDF.save()



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
    comandoSQL = 'SELECT STOCK FROM ARTICULOS WHERE CODIGO_DE_BARRA = {};'.format(codigoDeBarra)
    funciones_SQLite.ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos)
    stockDisponible = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
    stockDisponible = stockDisponible[0]
    if(stockDisponible < stockDeseado):
        print("Solo quedan disponibles {} unidades".format(stockDisponible))
        return False
    else:
        return True
