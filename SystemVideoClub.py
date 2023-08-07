from pathlib import Path
import UserSystemCreate as crearUsuario
import RolSystemCreate as crearRol
import ClienteSystemCreate as crearCliente
import PeliculaSystemCreate as crearPelicula
import OperaMovilSystemCreate as crearOperadora
import EstadoCivilSystemCreate as crearEstadoCivil
import ClienteTipoSystemCreate as crearTipoCliente
import GeneroPersonSystemCreate as crearGeneroCliente
import EstadoSystemCreate as crearEstado
import PeliculaTipoSystemCreate as crearTipoPelicula
import GeneroPelSystemCreate as crearGeneroPelicula
import CalificacionPelSystemCreate as calificacionPelicula
import ActoresSystemCreate as crearActores
import DirectorSystemCreate as crearDirectores
import ProductoraSystemCreate as crearProductora
import AlquilarPeliculaSystem as alquilarPelicula

# 1 Presentamos el ingreso al sistema
print("Hola Bienvenido al Sistema de Video Club - UNEMI")

# 1.- Definimos la ruta del file
Fl_Ruta_Menu = Path("C:/System_VideoClub/MenuList.txt")


def Prc_Menu_selector():
    while True:
        print("╔═══════════════════════════════════════════════╗")
        print("║            Sistema de VideoClub               ║")
        print("╠═══════════════════════════════════════════════╣")
        with open(Fl_Ruta_Menu, "r") as archivoMenu:
            for Linea in archivoMenu:
                print("║" + Linea.rstrip("\n").ljust(47) + "║")
        print("╚═══════════════════════════════════════════════╝")
        Lv_opcion = int(input("Introduzca opcion del (1/17): "))
        try:
            if Lv_opcion == 1:
                crearUsuario.registrarDatos()
            elif Lv_opcion == 2:
                crearRol.registrarDatos()
            elif Lv_opcion == 3:
                crearCliente.registrarDatos()
            elif Lv_opcion == 4:
                crearPelicula.registrarDatos()
            elif Lv_opcion == 5:
                crearOperadora.registrarDatos()
            elif Lv_opcion == 6:
                crearEstadoCivil.registrarDatos()
            elif Lv_opcion == 7:
                crearTipoCliente.registrarDatos()
            elif Lv_opcion == 8:
                crearGeneroCliente.registrarDatos()
            elif Lv_opcion == 9:
                crearEstado.registrarDatos()
            elif Lv_opcion == 10:
                crearTipoPelicula.registrarDatos()
            elif Lv_opcion == 11:
                crearGeneroPelicula.registrarDatos()
            elif Lv_opcion == 12:
                calificacionPelicula.registrarDatos()
            elif Lv_opcion == 13:
                crearActores.registrarDatos()
            elif Lv_opcion == 14:
                crearDirectores.registrarDatos()
            elif Lv_opcion == 15:
                crearProductora.registrarDatos()
            elif Lv_opcion == 16:
                alquilarPelicula.registrarDatos()
            elif Lv_opcion == 17:
                print("Finalizando sistema!")
                break
            else:
                print("Opcion invalidad!")
        except ValueError:
            print("Has colocado un valor no valido!")


# Preguntamos si existe el archivo
try:
    Lb_Existe_Archivo = Fl_Ruta_Menu.exists()
    if Lb_Existe_Archivo:
        Prc_Menu_selector()
    else:
        print("El sistema no se encuentra instalado de forma correcta, informe a sistemas.")
        print("Horario de atención: Lunes a viernes de 9:00 a 17:00")
        print("Celular: +593 999999999")
except IOError as error:
    print(f"No existe la información de arranque: {str(error)}")
    # Fue un error en la escritura
except Exception as error:
    print(f"Error de versiones (Solicite soporte): {str(error)}")
    # Nadie sabe lo que ocurrio
