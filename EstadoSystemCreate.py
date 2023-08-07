# Diccionario de datos del usuario
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import UtilidadesSystem as util

fl_ruta_file = Path("C:/System_VideoClub/EstadoSystem.txt")

# Estructura de diccionario
dcc_state_system = {
    "Id_Estado": "",
    "Nombre": "",
    "Detalle": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# estados del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo estado: ")
    for clave in dcc_state_system:
        if format(clave) == "Id_Estado":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        dcc_state_system[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del estado (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("StateSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Estado" + str(Ln_SenccReg) + ":"
                for clave, valor in dcc_state_system.items():
                    if format(clave) == "Id_Estado":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("StateSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de estados fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo estado
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")