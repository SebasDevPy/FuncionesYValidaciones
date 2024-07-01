def validaciones_numeros(mensaje_error: str, minimo: int|float, maximo: int|float) -> int|float:
    while True:
        numero = input(mensaje_error)
        if numero.lstrip('-').isdigit():
            numero = int(numero)
            if minimo <= numero <= maximo:
                break
            else:
                print("El número ingresado está fuera del rango permitido.")
        else:
            print("Por favor, introduce solo números.")
    return numero

def validar_lista_numeros(lista: list, minimo: int|float, maximo: int|float) -> list:
    numeros_validados = []
    for numero in lista:
        numero_validado = validaciones_numeros(f"El número '{numero}' no es válido. Introduce un número válido: ", minimo, maximo)
        numeros_validados.append(numero_validado)
    return numeros_validados

def validar_busqueda(busqueda: int) -> int:
    return validaciones_numeros("Ingrese un número válido para la búsqueda: ", -float('inf'), float('inf'))

def validar_reemplazo(reemplazo: int) -> int:
    return validaciones_numeros("Ingrese un número válido para el reemplazo: ", -float('inf'), float('inf'))

def validar_base_exponente(mensaje: str, minimo: int|float, maximo: int|float) -> tuple:
    base = validaciones_numeros("Ingrese la base: ", minimo, maximo)
    exponente = validaciones_numeros("Ingrese el exponente: ", minimo, maximo)
    return base, exponente