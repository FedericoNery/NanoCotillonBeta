import funciones_SQLite
from funciones_SQLite import baseDeDatos
from funciones_SQLite import cursorBaseDeDatos

def comandoSQLParaCrearBaseDeDatosNueva():
    comandoSQL = """
    CREATE TABLE IF NOT EXISTS AREAS(ID_AREA INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_AREA TEXT);
    CREATE TABLE IF NOT EXISTS MARCAS(ID_MARCA INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_MARCA TEXT,ALTA_BAJA INTEGER);
    CREATE TABLE IF NOT EXISTS ARTICULOS( CODIGO_DE_BARRA INTEGER PRIMARY KEY, NOMBRE_ARTICULO TEXT,PRECIO REAL,
    ARTICULO_MARCA INTEGER,ARTICULO_AREA INTEGER,FECHA DATETIME DEFAULT CURRENT_TIMESTAMP,STOCK INTEGER, ALTA_BAJA INTEGER,
    FOREIGN KEY (ARTICULO_MARCA) REFERENCES MARCAS(ID_MARCA),
    FOREIGN KEY (ARTICULO_AREA) REFERENCES AREAS(ID_AREA));
    CREATE TRIGGER IF NOT EXISTS ACT_FECHA AFTER UPDATE OF PRECIO ON ARTICULOS FOR EACH ROW BEGIN UPDATE ARTICULOS SET FECHA = CURRENT_TIMESTAMP;END;

    CREATE TABLE IF NOT EXISTS CLIENTES(ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE TEXT,NUMERO_TELEFONO INTEGER
    ,ALTA_BAJA INTEGER);

    CREATE TABLE IF NOT EXISTS ART_FACT(ID_ART INTEGER,ID_FACT INTEGER, CANTIDAD INTEGER, PRECIO INTEGER,
    FOREIGN KEY (ID_ART) REFERENCES ARTICULOS(ID),
    FOREIGN KEY (ID_FACT) REFERENCES FACTURAS(ID));

    CREATE TABLE IF NOT EXISTS FACTURAS (ID_FACTURA	INTEGER PRIMARY KEY AUTOINCREMENT, FECHA DATETIME DEFAULT CURRENT_TIMESTAMP,
	ID_CLIENTE INTEGER, FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE));

    INSERT INTO AREAS (NOMBRE_AREA) VALUES("COTILLON");
    INSERT INTO AREAS (NOMBRE_AREA) VALUES("REPOSTERIA");
    INSERT INTO AREAS (NOMBRE_AREA) VALUES("DESCARTABLES");
    INSERT INTO AREAS (NOMBRE_AREA) VALUES("SOUVENIRS");
   """
    return comandoSQL

def crearBaseDeDatosNueva():
    funciones_SQLite.conectarConBaseDeDatos()
    funciones_SQLite.tomarCursor()
    comandoSQL = comandoSQLParaCrearBaseDeDatosNueva()
    funciones_SQLite.ejecutarVariosComandos(comandoSQL)
    funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

