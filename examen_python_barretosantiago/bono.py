import json
from datetime import datetime
from registar import cargar_datos, guardar_datos,data


def bonos():
    datos = cargar_datos()
    identificacion = input("SCRIBE EL NUMEROD DE IDENTIFICACIÒN DEL EMPLEADO ")
    if identificacion in datos:
        fecha = str((datetime)(""))
        valor = float(input(" VALOR DEL BONO: "))
        concepto = input("Concepto del bono: ")
        datos[identificacion]['bonos'].append({'fecha': fecha, 'valor': valor, 'concepto': concepto})
        guardar_datos(datos)
        print("Bono registrado.")
    else:
        print("EL EMPLEADO NO SE ENCONTRO")
    guardar_datos(datos)    