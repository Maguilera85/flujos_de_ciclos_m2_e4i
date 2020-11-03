menor3 = 0
menor12 = 5000
mayor12 = 7000

edad = int(input("Ingrese su edad: "))

ciclo = 1

while ciclo == 1:
    if edad < 3 and edad > 0:
        print("El costo de la entrada es de: " + str(menor3) + " pesos.")
        ciclo = 0
    elif edad >= 3 and edad <=12:
        print("El costo de la entrada es de: " + str(menor12) + " pesos.")
        ciclo = 0
    elif edad > 12:
        print("El costo de la entrada es de: " + str(mayor12) + " pesos.")
        ciclo = 0
    else:
        print("Ingresaste un valor invalido, vuelve a intentarlo")
        ciclo = 1
        