from Validaciones import *

def get_int(mensaje: str, minimo: int|float, maximo: int|float) -> int|float|None:
    return validaciones_numeros(mensaje, minimo, maximo)

def get_float(mensaje: str, minimo: float, maximo: float) -> float | None:
    return validaciones_numeros(mensaje, minimo, maximo)

def calcular_factorial(mensaje: str, minimo: int, maximo: int) -> int:
    numero = validaciones_numeros(mensaje, minimo, maximo)
    if numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

def sumar_naturales(numero: int) -> int:
    if numero < 0:
        return 0
    else:
        suma = (numero * (numero + 1)) // 2
        return suma

def calcular_potencia(mensaje: str, minimo: int, maximo: int) -> int:
    base, exponente = validar_base_exponente(mensaje, minimo, maximo)
    return base ** exponente

def sumar_digitos_seguidos(minimo: int|float, maximo: int|float, solicitar_input: bool = True) -> int:
    if solicitar_input:
        numero = validaciones_numeros("Ingrese un número: ", minimo, maximo)
    if numero < 10:
        return numero
    else:
        return numero % 10 + sumar_digitos_seguidos(minimo, maximo, numero // 10, False)

def calcular_fibonacci() -> int:
    numero = validaciones_numeros("Ingrese un número: ", 0, float('inf'))
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

def sumar_positivos(lista: list) -> int|None|bool:
    retorno = None
    if type(lista) is list: 
        retorno = True
        if len(lista) > 0 :   
            retorno = 0    
            for i in range(len(lista)):
                numero_validado = validaciones_numeros( "Ingrese un número válido: ", -float('inf'), float('inf'), lista[i])
                if numero_validado > 0:
                    retorno += numero_validado
    return retorno

def buscar_maximo(numeros: list) -> int:
    maximo_numero = None
    for numero in numeros:
        if maximo_numero is None or numero > maximo_numero:
            maximo_numero = numero
    return maximo_numero

def buscar_negativo(numeros: list) -> bool:
    for numero in numeros:
        numero_validado = validaciones_numeros("Ingrese un número válido: ", -float('inf'), float('inf'), numero)
        if numero_validado < 0:
            return True
    return False

def buscar_reemplazar(lista: list, busqueda : int, reemplazo: int, reemplazo_todo: bool) -> list:
    numero_encontrado = False
    busqueda_validada = busqueda
    reemplazo_validado = reemplazo
    if type(lista) == list and type(busqueda_validada) == int and type(reemplazo_validado) == int:
        for i in range(len(lista)): 
            if lista[i] == busqueda_validada:
                lista[i] = reemplazo_validado
                numero_encontrado = True
                if not reemplazo_todo:  
                    break
        if not numero_encontrado:  
            print(f"El número {busqueda_validada} no se encontró en la lista.")
    return lista

def listar_numeros(numeros: list) -> list:
    return [f"Los numeros ingresados son: {numero}" for numero in numeros]

def listar_pares(numeros: list) -> list:
    return [f"Los numeros pares son: {numero}" for numero in numeros if numero % 2 == 0]

def listar_posiciones_impares(numeros: list) -> list:
    return [f"La posición es {i+1}: {numero}" for i, numero in enumerate(numeros) if (i+1) % 2 != 0]
    
def mostrar_postivos_negativos(numeros: list, mensaje_error: str, minimo: int|float, maximo: int|float) -> tuple:
    positivo = 0
    negativo = 0
    for numero in numeros:
        if numero > 0:
            positivo += 1
        elif numero < 0:
            negativo += 1
    return positivo, negativo

def sumar_pares(numeros: list, mensaje_error: str, minimo: int|float, maximo: int|float) -> int:
    suma = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma += numero
    return suma

def mayor_numero_impar(numeros: list, mensaje_error: str, minimo: int|float, maximo: int|float) -> int|None:
    mayor_impar = None
    for numero in numeros:
        if numero % 2 != 0:
            if mayor_impar is None or numero > mayor_impar:
                mayor_impar = numero
    return mayor_impar