import json
from registar import cargar_datos, guardar_datos

datos = cargar_datos()
def calculadora ():
  for identificacion, info in datos.items():
        salario_base = info['salario']
        inasistencias = len(info['inasistencias'])
        bonos = sum(bono['valor'] for bono in info['bonos'])
        
        descuentos = {
            'salud': salario_base * 0.04,
            'pension': salario_base * 0.04,
            'faltas': (salario_base / 30) * inasistencias
        }
        total_descuentos = sum(descuentos.values())
        
        auxilio_transporte = 0
        if salario_base < 2000000:
            auxilio_transporte = salario_base * 0.10
        
        total_pagar = salario_base - total_descuentos + bonos + auxilio_transporte
        
        with open(f'{identificacion}.txt', 'w') as file:
            file.write(f"Identificación: {identificacion}\n")
            file.write(f"Nombre: {info['nombre']}\n")
            file.write(f"Cargo: {info['cargo']}\n")
            file.write(f"Salario Base: {salario_base}\n")
            file.write(f"Descuento Salud: {descuentos['salud']}\n")
            file.write(f"Descuento Pensión: {descuentos['pension']}\n")
            file.write(f"Descuento Faltas: {descuentos['faltas']}\n")
            file.write(f"Bonos: {bonos}\n")
            file.write(f"Auxilio de Transporte: {auxilio_transporte}\n")
            file.write(f"Total a Pagar: {total_pagar}\n")
            
        print(f"Nómina calculada y archivo generado para {info['nombre']}.")
  guardar_datos(datos)

