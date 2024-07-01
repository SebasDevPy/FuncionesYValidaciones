def validaciones_numeros(mensaje_error: str, minimo: int|float, maximo: int|float) -> int|float:
    while True:
        numero = input(mensaje_error)
        if numero.lstrip('-').replace('.', '', 1).isdigit():
            numero = float(numero)
            if minimo <= numero <= maximo:
                break
            else:
                print("El número ingresado está fuera del rango permitido.")
        else:
            print("Por favor, introduce solo números.")
    return numero

def calcular_fibonacci(numero: int) -> int:
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

numero_usuario = validaciones_numeros("Ingrese un número: ", 0, float('inf'))
resultado = calcular_fibonacci(int(numero_usuario))
print("El número de Fibonacci para", int(numero_usuario), "es:", resultado)