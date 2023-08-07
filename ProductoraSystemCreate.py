# Diccionario de datos del usuari
# Importar las librerias/Bibliotecas
import datetime
from pathlib import Path
import UtilidadesSystem as util
import EstadoSystemCreate as estados

fl_ruta_file = Path("C:/System_VideoClub/Productoras.txt")

# Estructura de diccionario
Dcc_ProductoSystem = {
    "Id_Productora": "",
    "Descripcion": "",
    "Id_Estado": "",
    "Fecha_Ingreso": ""
}


# ***********************************
# Arranca el sistema
# Pedimos al usuario del sistema ingresar los datos del nueva
# productoras del sistema.
def registrarDatos():
    print("Ingrese los datos del nuevo tipo de pelicula: ")
    for clave in Dcc_ProductoSystem:
        if format(clave) == "Id_Productora":
            print(f"{clave}:___")
            valor = ""
        elif format(clave) == "Id_Estado":
            dcc_estados = util.recuperarDatos(estados.fl_ruta_file)
            valor = util.obtenerValor(dcc_estados, "Id_Estado", "Nombre")
        elif format(clave) == "Fecha_Ingreso":
            valor = datetime.datetime.now()
        else:
            valor = input("{}: ".format(clave))
        Dcc_ProductoSystem[clave] = valor

    while True:
        Lv_Guardar = str(input("Desea guardar los datos de la productora (S/N): ")).upper()
        if Lv_Guardar == "S":
            print("Procesando...")
            # Proceso de almacenamiento
            # Recuperamos la secuencia de los registros guardados
            Ln_SenccReg = util.Prc_ContrSecuencia("ProductoraCine")
            # Salvo el registro dentro del file del archivo
            with open(fl_ruta_file, "a") as archivoUser:
                Linea = "Productora" + str(Ln_SenccReg) + ":"
                for clave, valor in Dcc_ProductoSystem.items():
                    if format(clave) == "Id_Productora":
                        valor = str(Ln_SenccReg)
                    Linea += f"{clave}={valor},"
                Linea = Linea.rstrip(",") + "\n"
                archivoUser.write(Linea)
            # Actualizar la secuencia de los registros
            Lv_Guardar = util.Prc_UpdateSecuencia("ProductoraCine", Ln_SenccReg)
            if Lv_Guardar == "SI":
                print("La secuencia de los registros de productoras fue actualizada")
            else:
                print("La secuencia no fue actualizada, notifique a sistema.")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            break
        else:
            print("Opción no valida.")
