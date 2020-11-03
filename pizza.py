ingredientes = ["mozarella", "peperoni", 
                "doble queso", "tomate", "piña", "carne", "palta"]
mipyzza = []

print("Bienvenido a PYzza \n")
nombre = input("Ingrese su nombre: ")
print()
print("Hola " + nombre + " todas las pizzas incluyen los ingredientes base" 
            "(queso, jamon, salsa de tomate) \n")

entrada = 1
while entrada == 1:
    print("Selecciona un ingrediente de la lista para tu PYzza \n", ingredientes)
    select = input(">> ")
    if select in ingredientes:
        mipyzza.append(select)
        paso_2 = input("¿Desea agregar otro ingrediente S/N \n >>?")
        if paso_2 == "S" or paso_2 == "s":
           entrada = 1
        elif paso_2 == "N" or paso_2 == "n":
            entrada = 0
        else:
            print("Has ingresado una opcion invalida, vuelve a intentarlo ")
            entrada = 1
    else:
        print("Has ingresado una opcion invalida, vuelve a intentarlo")
        entrada = 1

print("Pronto disfrutaras de tu PYzza con los mejores ingredientes: \n", mipyzza)
