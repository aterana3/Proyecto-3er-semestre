# Diccionario de datos del usuario
# Importar las librerias/Bibliotecas
from pathlib import Path
import UtilidadesSystem as util
import EstadoSystemCreate as estados
import datetime

fl_ruta_file = Path("C:/System_VideoClub/UsuarioTipoSystem.txt")

# Estructura de diccionario
Dcc_TipoSystem = {
    "Id_ClienTipo": "",
    "Descripcion": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# tipo de cliente del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo tipo de cliente: ")
    for clave in Dcc_TipoSystem:
        if format(clave) == "Id_ClienTipo":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Fecha_Ingreso":
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
            Ln_SenccReg = util.Prc_ContrSecuencia("ClientTipoSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "ClientTipo" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_TipoSystem.items():
                    if format(clave) == "Id_ClienTipo":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("ClientTipoSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de tipo de clientes fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")