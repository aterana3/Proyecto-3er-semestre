# Diccionario de datos del usuario
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import UtilidadesSystem as util
import EstadoSystemCreate as estados

fl_ruta_file = Path("C:/System_VideoClub/OperadoraSystem.txt")

# Estructura de diccionario
Dcc_OperaMovilSystem = {
    "Id_Operadora": "",
    "Descripcion": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nueva
# operadora movil del sistema.
def registrarDatos():
    print("Ingrese los datos de la nueva operadora movil: ")
    for clave in Dcc_OperaMovilSystem:
        if format(clave) == "Id_Operadora":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        Dcc_OperaMovilSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos de la operadora movil (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("OperaMovil")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "OperaMovil" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_OperaMovilSystem.items():
                    if format(clave) == "Id_Operadora":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("OperaMovil", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de operadora movil fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")