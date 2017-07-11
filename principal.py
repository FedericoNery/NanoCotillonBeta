import mostrar_menu_principal
import funciones_menu_de_opciones
def principal():
    mostrar_menu_principal.mostrarMensajeDeBienvenida()
    mostrar_menu_principal.mostrarMenuDeOpciones()
    numeroDeOpcion = funciones_menu_de_opciones.ingresoOpcionDelMenuElegida()
    funciones_menu_de_opciones.seleccionarOpcionDelMenuElegida(numeroDeOpcion)

while(True):
    principal()