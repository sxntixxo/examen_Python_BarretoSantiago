from registar import registrar
from inasistencia import inasistencia
from bono import bonos
from calculadora import calculadora

while True:
  try:
    while True:
      print(" BIENVENIDO A SU CALCULADORA DE NOMINA")
      print(" SELECCIONE ELUNA OPCIÒN")
      print(" 1. REGISTAR EMPLEADO ")
      print(" 2. REGISTAR INASISTENCIA ")
      print(" 3. REGISTAR BONOS EXTRA_LEGALES")
      print(" 4. CALCULAR NOMINA DEL EMPLEADO")
      opc = int(input())
      if opc == 1:
        registrar()
      elif opc == 2:
        inasistencia()
      elif opc == 3:
        bonos()
      elif opc == 4:
        calculadora()
  except ValueError:
    print(" LA OPCIÒN ELEGIDA NO EXISTE")