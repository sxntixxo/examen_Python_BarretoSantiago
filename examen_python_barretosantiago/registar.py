import json
data = 'empleado.json'
def cargar_datos():
    try:
        with open(data, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_datos(datos):
    with open(data, 'w') as file:
        json.dump(datos, file, indent=4)

def registrar():
    datos = cargar_datos()
    identificacion = input("IDENTIFICACIÒN: ")
    nombre = input("NOMBRE:: ")
    cargo = input("CARGO: ")
    salario = float(input("SALARIO: "))
    
    datos[identificacion] = {
        'nombre': nombre,
        'cargo': cargo,
        'salario': salario,
        'inasistencias': [],
        'bonos': []
    }
    guardar_datos(datos)
    print("EL EMPLEADO SE REGISTRO")