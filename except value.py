#try except value permite la validacion de entrada de datos
while True:
    try:
        alumno=input("Dame el nombre del alumno:")
        cal1=float(input("Dame la primera calif:"))
        cal2=float(input("Dame la segunda calif:"))
        break
    except ValueError:
                   print("Error: Debes ingresar numeros validos")
        print("Hola mundo")
