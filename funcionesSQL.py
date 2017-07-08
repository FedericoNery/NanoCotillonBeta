import sqlite3

baseDeDatos = None
cursorBaseDeDatos = None

def conectarConBaseDeDatos():
    global baseDeDatos
    baseDeDatos = sqlite3.connect("nuevaBase.db")
    return baseDeDatos

def tomarCursor():
    global cursorBaseDeDatos
    cursorBaseDeDatos = baseDeDatos.cursor()
    return cursorBaseDeDatos

def ejecutarComandoSQL(comandoSQL,cursorBaseDeDatos):
    cursorBaseDeDatos.execute(comandoSQL)

def extraerTabla(cursorBaseDeDatos):
    tabla = cursorBaseDeDatos.fetchall()
    return tabla

def extraerElemento(cursorBaseDeDatos):
    elemento = cursorBaseDeDatos.fetchone()
    return elemento

def guardarBaseDeDatos(baseDeDatos):
    baseDeDatos.commit()

def ejecutarVariosComandos(comandoSQL):
    cursorBaseDeDatos.executescript(comandoSQL)

a = conectarConBaseDeDatos()
b = tomarCursor()
