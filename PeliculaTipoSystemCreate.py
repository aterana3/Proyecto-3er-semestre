# Diccionario de datos del usuari
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import UtilidadesSystem as util
import EstadoSystemCreate as estados

fl_ruta_file = Path("C:/System_VideoClub/PeliculaTipo.txt")

# Estructura de diccionario
Dcc_PeliTipoSystem = {
    "Id_PeliTipo": "",
    "Descripcion": "",
    "Id_Estado": "",
    "Costo": "",
    "Tiempo_Alquiler": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# tipo de pelicula del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo tipo de pelicula: ")
    for clave in Dcc_PeliTipoSystem:
        if format(clave) == "Id_PeliTipo":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        else:
            valor = input("{}: ".format(clave))
        Dcc_PeliTipoSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del tipo de pelicula (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("PelTipoSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "PeliTipo" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_PeliTipoSystem.items():
                    if format(clave) == "Id_PeliTipo":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("PelTipoSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de tipos de peliculas fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")