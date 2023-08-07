# Importar las librerias/Bibliotecas
from pathlib import Path
import UtilidadesSystem as util
import GeneroPersonSystemCreate as genero
import datetime

fl_ruta_file = Path("C:/System_VideoClub/ActorCine.txt")

# Estructura de diccionario
Dcc_ActorSystem = {
    "Id_Actor": "",
    "Nombres_Apellidos": "",
    "Id_Genero": "",
    "Fecha_nacimiento": "",
    "Galardonada": "",
    "Oscar": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# actor del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo actor: ")
    for clave in Dcc_ActorSystem:
        if format(clave) == "Id_Actor":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_Genero":
            dcc_genero = util.recuperarDatos(genero.fl_ruta_file)
            valor = util.obtenerValor(dcc_genero, "Id_Genero")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        Dcc_ActorSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del actor (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("ActorCine")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Actor" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_ActorSystem.items():
                    if format(clave) == "Id_Actor":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("ActorCine", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de actores fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")