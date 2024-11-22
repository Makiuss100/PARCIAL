import math


def contar_digitos(n):
    return len(str(n))


def criba_eratostenes(limite):
    """Genera todos los primos hasta el límite usando la criba de Eratóstenes."""
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos
    primos = []

    for i in range(2, limite + 1):
        if es_primo[i]:
            primos.append(i)
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    return primos


def factores_primos_criba(n):
    """Devuelve los factores primos únicos de n usando primos generados por la criba."""
    limite = int(math.sqrt(n)) + 1
    primos = criba_eratostenes(limite)  # Generamos primos hasta la raíz de n
    factores = set()  # Usamos un conjunto para factores únicos

    # Usamos los primos para dividir n
    for p in primos:
        while n % p == 0:
            factores.add(p)  # Añadimos solo el primo, sin repeticiones
            n //= p

    # Si queda un número mayor que 1, es un primo
    if n > 1:
        factores.add(n)  # Añadimos el número restante como un factor primo

    return factores  # Retornamos la lista ordenada de factores primos únicos


# Ejemplo de uso

casos = int(input())
for _ in range(casos):
    n = int(input())
    digitos = contar_digitos(n)
    factores = factores_primos_criba(n)
    cantidad_factores = len(factores)
    if digitos == cantidad_factores:
        print("SI")
    else:
        print("NO")
