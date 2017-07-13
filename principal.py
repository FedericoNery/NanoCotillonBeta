import mostrar_menu_principal
import funciones_menu_de_opciones
import os

def principal():
    os.system("cls")
    mostrar_menu_principal.mostrarMensajeDeBienvenida()
    mostrar_menu_principal.mostrarMenuDeOpciones()
    numeroDeOpcion = funciones_menu_de_opciones.ingresoOpcionDelMenuElegida()
    funciones_menu_de_opciones.seleccionarOpcionDelMenuElegida(numeroDeOpcion)
    input("presione cualquier tecla para continuar")
    os.system("cls")

while(True):
    principal()