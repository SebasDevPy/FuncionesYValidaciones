from Funciones import *

def menu():
    numeros = []
    mensaje = "Ingrese correctamente el número"
    minimo = -1000
    maximo = 1000
    while True:
        print("\nMenu:")
        print("1. Ingresar 10 números enteros entre -1000 y 1000")
        print("2. Mostrar la cantidad de números positivos y negativos")
        print("3. Mostrar la sumatoria de los números pares")
        print("4. Informar el mayor de los números impares")
        print("5. Listar todos los números ingresados")
        print("6. Listar todos los números pares")
        print("7. Listar los números de las posiciones impares")
        print("8. Buscar el número máximo de la lista dada")
        print("9. Sumar naturales")
        print("10. Reemplazar un número de la lista")
        print("11. Calcular factorial")
        print("12. Calcular potencia")
        print("13. Salir")

        opcion = get_int("Elige una opción: ", 1, 13)

        if opcion == 1:
            numeros = [get_int(f"Ingrese el número {i+1}: ", minimo, maximo) for i in range(10)]

        elif opcion == 2:
            positivos, negativos = mostrar_postivos_negativos(numeros, mensaje, minimo, maximo)
            print(f"Números positivos: {positivos}, Números negativos: {negativos}")

        elif opcion == 3:
            suma = sumar_pares(numeros, mensaje, minimo, maximo)
            print(f"La suma de los pares es: {suma}")

        elif opcion == 4:
            mayor_impar = mayor_numero_impar(numeros, mensaje, minimo, maximo)
            print(f"El mayor número impar es: {mayor_impar}")

        elif opcion == 5:
            print("Números ingresados: ", listar_numeros(numeros))

        elif opcion == 6:
            print("Números pares: ", listar_pares(numeros))

        elif opcion == 7:
            print("Números en posiciones impares: ", listar_posiciones_impares(numeros))

        elif opcion == 8:
            print("El mayor número es: ", buscar_maximo(numeros))

        elif opcion == 9:
            numero = get_int("Ingresa un número positivo: ", 0, float("inf"))
            print("El resultado es: ", sumar_naturales(numero))

        elif opcion == 10:
            busqueda = get_int("Ingrese el número que desea buscar: ", minimo, maximo)
            reemplazo = get_int("Ingrese el número por el cual desea reemplazar: ", minimo, maximo)
            reemplazo_todo = input("¿Quiere reemplazar más números? (si/no): ").lower() == "si"
            numeros = buscar_reemplazar(numeros, busqueda, reemplazo, reemplazo_todo)
            print("Lista actualizada:", numeros)

        elif opcion == 11:
            numero = get_int("Ingrese el número: ", minimo, maximo)
            resultado = calcular_factorial(mensaje, 0, maximo)
            print(f"El factorial de {numero} es {resultado}")

        elif opcion == 12:
            resultado = calcular_potencia("Ingrese el número base: ", minimo, maximo)
            print(f"El resultado es {resultado}")

        elif opcion == 13:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 13.")

menu()