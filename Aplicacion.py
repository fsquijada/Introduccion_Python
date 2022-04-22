# -----------------VARIABLES------------------
bandera = True

# -----------------FUNCIONES------------------
def validacion (CLAVE, TIEMPO):
    if CLAVE == 1:
        if TIEMPO >= 1 and TIEMPO < 2:
            return 6
        elif TIEMPO >= 2 and TIEMPO < 7:
            return 14
        elif TIEMPO > 7:
            return 20
        else:
            return 0
    elif CLAVE == 2:
        if TIEMPO >= 1 and TIEMPO < 2:
            return 7
        elif TIEMPO >= 2 and TIEMPO < 7:
            return 15
        elif TIEMPO > 7:
            return 22
        else:
            return 0
    elif CLAVE == 3:
        if TIEMPO >= 1 and TIEMPO < 2:
            return 10
        elif TIEMPO >= 2 and TIEMPO < 7:
            return 20
        elif TIEMPO > 7:
            return 30
        else:
            return 0

#----------------------OPERATIVO-----------------
while bandera == True:
    nombre = input ("Escriba el nombre del empleado: ")
    clave = int (input ("Escriba la clave del departamento: "))

    while clave < 1 or clave > 3:
        print ("La clave del departamento no existe")
        clave = int (input ("Escriba la clave del departamento (Entre 1 y 3): "))
    
    tiempo = float (input ("Introduzca la cantidad de años laborados: "))

    dias = validacion (clave, tiempo)

    print (f"El empleado {nombre} tiene derecho a {dias} días de vacaciones")
    print ("\n ¿Desea seguir revisando empleados?")
    continuar = input("Presione cualquier tecla para continuar o presione 's' para salir")

    if continuar == "s" or continuar == "S":
        bandera = False

        
























"""
nombre = input ("Escriba el nombre del empleado: ")
clave = int (input ("Escriba la clave del departamento: "))
tiempo = float (input ("Introduzca la cantidad de años laborados: "))



if clave == 1:
    if tiempo >= 1 and tiempo < 2:
        print (f"El empleado {nombre}, tiene derecho a 6 días de vacaciones")
    elif tiempo >= 2 and tiempo < 7:
        print (f"El empleado {nombre}, tiene derecho a 14 días de vacaciones")
    elif tiempo > 7:
        print (f"El empleado {nombre}, tiene derecho a 20 días de vacaciones")
    else:
        print ("El empleado no tiene derecho a vacaciones.")
elif clave == 2:
    if tiempo >= 1 and tiempo < 2:
        print (f"El empleado {nombre}, tiene derecho a 7 días de vacaciones")
    elif tiempo >= 2 and tiempo < 7:
        print (f"El empleado {nombre}, tiene derecho a 15 días de vacaciones")
    elif tiempo > 7:
        print (f"El empleado {nombre}, tiene derecho a 22 días de vacaciones")
    else:
        print ("El empleado no tiene derecho a vacaciones.")
elif clave == 3:
    if tiempo >= 1 and tiempo < 2:
        print (f"El empleado {nombre}, tiene derecho a 10 días de vacaciones")
    elif tiempo >= 2 and tiempo < 7:
        print (f"El empleado {nombre}, tiene derecho a 20 días de vacaciones")
    elif tiempo > 7:
        print (f"El empleado {nombre}, tiene derecho a 30 días de vacaciones")
    else:
        print ("El empleado no tiene derecho a vacaciones.")
else:
    print("No existe la clave del departamento")

"""

