from pathlib import Path

# Cargar la ruta del Control de secuencia
fl_ruta_sec = Path("C:/System_VideoClub/ControlSecuencia.txt")


# Obtener los diccionarios de los archivos
def recuperarDatos(Fl_Ruta_File):
    Dcc_datos_Read = {}
    with open(Fl_Ruta_File, mode="r") as archivo:
        for linea in archivo:
            registro = linea.rstrip("\n").split(":")
            datos = registro[1].split(",")
            Dcc_datos_registro = {}
            for dato in datos:
                clave, valor = dato.split("=")
                Dcc_datos_registro[clave] = valor
            Dcc_datos_Read[registro[0]] = Dcc_datos_registro
    return Dcc_datos_Read


# Preguntar los valores
def obtenerValor(dcc, key, key_nombre="Descripcion"):
    print(f"Opciones disponibles de {key}")
    for estado, datos in dcc.items():
        nombre = datos[key_nombre]
        id_gen = datos[key]
        print(f"Nombre: {nombre}, Id: {id_gen}")
    while True:
        try:
            valor = input("{}: ".format(key))
            if valor in [datos_pelGenero[key] for datos_pelGenero in dcc.values()]:
                break
            else:
                print("Introduzca un estado valido!")
        except ValueError:
            print("ID de estado no válido. Intente nuevamente.")
    return valor


# Obtener el valor del control de secuencia
def Prc_ContrSecuencia(Iv_Registro):
    On_Secuencia = 0
    # Accedemos al file txt y recuperamos el registro
    with open(fl_ruta_sec, "r") as archivoSecuencia:
        for registro in archivoSecuencia:
            # Control = valor a recuperar
            # Secuencia = La secuencia/cantidad de registros
            Control, Secuencia = registro.strip().split(":")
            if Control == Iv_Registro:
                On_Secuencia = int(Secuencia) + 1
                break
    return On_Secuencia


# Actualizar los valores del control de secuencia
def Prc_UpdateSecuencia(Iv_Registro, In_Secuencia):
    Ov_Mensaje = ""
    Linea = ""
    # Accedemos al file de secuencia en forma de lectura
    with open(fl_ruta_sec, "r") as archivoSecuencia:
        for registro in archivoSecuencia:
            # Control = valor a recuperar
            # Secuencia = La secuencia/cantidad de registros
            Control, Secuencia = registro.strip().split(":")
            if Control == Iv_Registro:
                Secuencia = In_Secuencia
            Linea += Control + ":" + str(Secuencia) + "\n"
    # Accedemos al archivo en forma de escritura y agregamos el nuevo valor
    with open(fl_ruta_sec, "w") as archivoSecuencia:
        archivoSecuencia.write(Linea)
        Ov_Mensaje = "SI"
    return Ov_Mensaje
