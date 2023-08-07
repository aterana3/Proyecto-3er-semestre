# Diccionario de datos del usuario
# Importar las librerias/Bibliotecas
from pathlib import Path
from UtilidadesSystem import Prc_ContrSecuencia, Prc_UpdateSecuencia
import datetime

fl_ruta_file = Path("C:/System_VideoClub/UsuarioTipoSystem.txt")

# Estructura de diccionario
Dcc_TipoSystem = {
    "Id_ClienTipo": "",
    "Descripcion": "",
    "Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# tipo de usuario del sistema.
print("Ingrese los datos del nuevo tipo de usuario: ")
for clave in Dcc_TipoSystem:
    if format(clave) == "Fecha_Ingreso":
        valor = datetime.datetime.now()
    else:
        valor = input("{}: ".format(clave))
    Dcc_TipoSystem[clave] = valor

while True:
    Lv_Guardar = str(input("Desea guardar los datos del estado (S/N): ")).upper()
    if Lv_Guardar == "S":
        print("Procesando...")
        # Proceso de almacenamiento
        # Recuperamos la secuencia de los registros guardados
        Ln_SenccReg = Prc_ContrSecuencia("ClientTipoSystem")
        # Salvo el registro dentro del file del archivo
        with open(fl_ruta_file, "a") as archivoUser:
            Linea = "ClientTipo" + str(Ln_SenccReg) + ":"
            for clave, valor in Dcc_TipoSystem.items():
                Linea += f"{clave}={valor},"
            Linea = Linea.rstrip(",") + "\n"
            archivoUser.write(Linea)
        # Actualizar la secuencia de los registros
        Lv_Guardar = Prc_UpdateSecuencia("ClientTipoSystem", Ln_SenccReg)
        if Lv_Guardar == "SI":
            print("La secuencia de los registros tipo de usuario fue actualizada")
        else:
            print("La secuencia no fue actualizada, notifique a sistema.")
        break
    elif Lv_Guardar == "N":
        # Cancelamos el proceso de crear un nuevo usuario
        print("Proceso cancelado.")
        break
    else:
        print("Opción no valida.")
