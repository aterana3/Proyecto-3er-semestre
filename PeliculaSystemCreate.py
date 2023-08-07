# Diccionario de datos del usuari
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import UtilidadesSystem as util
import EstadoSystemCreate as estados
import PeliculaTipoSystemCreate as peliTipo
import GeneroPelSystemCreate as genPel
import CalificacionPelSystemCreate as calif
import ActoresSystemCreate as actores
import DirectorSystemCreate as directores
import ProductoraSystemCreate as productora

fl_ruta_file = Path("C:/System_VideoClub/Peliculas.txt")

# Estructura de diccionario
Dcc_PeliSystem = {
    "Id_Pelicula": "",
    "Nombre": "",
    "Id_PeliTipo": "",
    "Id_PelGenero": "",
    "Id_PelClasifica": "",
    "Id_Actor": "",
    "Id_Director": "",
    "Id_Productora": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nueva
# pelicula del sistema.
def registrarDatos():
    print("Ingrese los datos del nueva pelicula: ")
    for clave in Dcc_PeliSystem:
        if format(clave) == "Id_Pelicula":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_PeliTipo":
            dcc_peliTipo = util.recuperarDatos(peliTipo.fl_ruta_file)
            valor = util.obtenerValor(dcc_peliTipo, "Id_PeliTipo")
        elif format(clave) == "Id_PelGenero":
            dcc_pelGenero = util.recuperarDatos(genPel.fl_ruta_file)
            valor = util.obtenerValor(dcc_pelGenero, "Id_PelGenero")
        elif format(clave) == "Id_PelClasifica":
            dcc_calif = util.recuperarDatos(calif.fl_ruta_file)
            valor = util.obtenerValor(dcc_calif, "Id_PelClasifica")
        elif format(clave) == "Id_Actor":
            dcc_actor = util.recuperarDatos(actores.fl_ruta_file)
            valor = util.obtenerValor(dcc_actor, "Id_Actor", "Nombres_Apellidos")
        elif format(clave) == "Id_Director":
            dcc_director = util.recuperarDatos(directores.fl_ruta_file)
            valor = util.obtenerValor(dcc_director, "Id_Director")
        elif format(clave) == "Id_Productora":
            dcc_productora = util.recuperarDatos(productora.fl_ruta_file)
            valor = util.obtenerValor(dcc_productora, "Id_Productora")
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        Dcc_PeliSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos de la pelicula (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("PeliculaSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Pelicula" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_PeliSystem.items():
                    if format(clave) == "Id_Pelicula":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("PeliculaSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de peliculas fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")