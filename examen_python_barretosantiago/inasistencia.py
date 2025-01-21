import json
from datetime import datetime
from registar import cargar_datos,guardar_datos

def inasistencia():
    datos = cargar_datos()
    identificacion = input("ESCRIBE EL NUMEROD DE IDENTIFICACIÒN DEL EMPLEADO ")
    if identificacion in datos:
        fecha = str(datetime.now())
        datos[identificacion]['inasistencias'].append(fecha)
        guardar_datos(datos)
        print("INASISTENCIA REGISTRADA")
    else:
        print("EL EMPLEADO NO SE ENCONTRO")
    guardar_datos(datos)    

 