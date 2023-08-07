# Diccionario de datos del usuario
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import EstadoSystemCreate as estados
import UtilidadesSystem as util

fl_ruta_file = Path("C:/System_VideoClub/RolSystem.txt")

# Estructura de diccionario
dcc_rol_system = {
    "Id_Rol": "",
    "Descripcion": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# rol del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo rol: ")
    for clave in dcc_rol_system:
        if format(clave) == "Id_Rol":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        else:
            valor = input("{}: ".format(clave))
        dcc_rol_system[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del rol (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("RolSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Rol" + str(Ln_SenccReg) + ":"
                for clave, valor in dcc_rol_system.items():
                    if format(clave) == "Id_Rol":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("RolSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de rol fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")