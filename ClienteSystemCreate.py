# Diccionario de datos del usuario
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import UtilidadesSystem as util
import GeneroPersonSystemCreate as genero
import EstadoCivilSystemCreate as civil
import OperaMovilSystemCreate as opera
import ClienteTipoSystemCreate as tipo
import EstadoSystemCreate as estados


fl_ruta_file = Path("C:/System_VideoClub/ClienteSystem.txt")

# Estructura de diccionario
Dcc_ClientSystem = {
    "Id_Cliente": "",
    "Cedula": "",
    "Nombres": "",
    "Apellidos": "",
    "Id_Genero": "",
    "Fecha_nacimiento": "",
    "Id_Estado_Civil": "",
    "Dirección": "",
    "Referencia": "",
    "Id_Operadora": "",
    "Celular": "",
    "Teléfono": "",
    "Correo": "",
    "Id_ClienTipo": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nuevo
# cliente del sistema.
def registrarDatos():
    print("Ingrese los datos de la nuevo cliente: ")
    for clave in Dcc_ClientSystem:
        if format(clave) == "Id_Cliente":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_Genero":
            dcc_genero = util.recuperarDatos(genero.fl_ruta_file)
            valor = util.obtenerValor(dcc_genero, "Id_Genero")
        elif format(clave) == "Id_Estado_Civil":
            dcc_civil = util.recuperarDatos(civil.fl_ruta_file)
            valor = util.obtenerValor(dcc_civil, "Id_Estado_Civil")
        elif format(clave) == "Id_Operadora":
            dcc_operadora = util.recuperarDatos(opera.fl_ruta_file)
            valor = util.obtenerValor(dcc_operadora, "Id_Operadora")
        elif format(clave) == "Id_ClienTipo":
            dcc_tipo = util.recuperarDatos(tipo.fl_ruta_file)
            valor = util.obtenerValor(dcc_tipo, "Id_ClienTipo")
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        Dcc_ClientSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos del cliente (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("ClientSystem")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Cliente" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_ClientSystem.items():
                    if format(clave) == "Id_Cliente":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("ClientSystem", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de clientes fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")