# Diccionario de datos del usuari
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import EstadoSystemCreate as estados
import UtilidadesSystem as util

fl_ruta_file = Path("C:/System_VideoClub/GeneroSystem.txt")

# Estructura de diccionario
dcc_genero_system = {
    "Id_Genero": "",
    "Descripcion": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# genero de persona del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo genero: ")
    for clave in dcc_genero_system:
        if format(clave) == "Id_Genero":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        dcc_genero_system[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del genero (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("GeneroPersonSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Genero" + str(Ln_SenccReg) + ":"
                for clave, valor in dcc_genero_system.items():
                    if format(clave) == "Id_Genero":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("GeneroPersonSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de generos de personas fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")