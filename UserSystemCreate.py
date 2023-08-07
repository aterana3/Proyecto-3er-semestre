# Importar las librerias/Bibliotecas
from pathlib import Path
import UtilidadesSystem as util
import RolSystemCreate as roles
import EstadoSystemCreate as estados
import getpass
from cryptography.fernet import Fernet
import datetime

fl_ruta_file = Path("C:/System_VideoClub/UserSystem.txt")

# Estructura de diccionario
Dcc_UserSystem = {
    "Id_User": "",
    "Nombre": "",
    "Password": "",
    "Id_Rol": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# usuario del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo usuario: ")
    for clave in Dcc_UserSystem:
        # valor = input("{}: ".format(clave))
        # Dcc_UserSystem[clave] = valor
        if format(clave) == "Id_User":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Password":
            valor = getpass.getpass("{}: ".format(clave))
            clave_fernet = Fernet.generate_key()
            fernet = Fernet(clave_fernet)
            cifrado = fernet.encrypt(valor.encode())
            valor = cifrado
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Id_Rol":
            dcc_roles = util.recuperarDatos(roles.fl_ruta_file)
            valor = util.obtenerValor(dcc_roles, "Id_Rol")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        Dcc_UserSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del usuario (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("UserSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Usuario" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_UserSystem.items():
                    if format(clave) == "Id_User":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("UserSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de usuario fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")