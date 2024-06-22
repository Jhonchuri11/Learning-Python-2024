
def suma(user):

    opcion = user

    a = int(input("Ingresar tu numero 1: "))
    b = int(input("Ingresar tu segundo numero 2: "))

    if opcion == 'suma':

        resultado = a + b
    
    elif opcion == 'resta':

        resultado = a - b

    elif opcion == 'division':

        resultado == a / b
        
    else:
        print("No existe esa opcion")

    print(f"{opcion} es : {resultado}")

suma('suma')

