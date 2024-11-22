def bubble_sort_desc(arr):
    """Ordena una lista en orden descendente usando Bubble Sort"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # Intercambiar si el elemento actual es menor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def calcular_ataques_minimos(n, D, items):
    # Ordenar los ítems en orden descendente usando Bubble Sort
    items = bubble_sort_desc(items)
    
    # Iniciar un contador de ataques
    ataques = 0
    salud_restante = D

    # Usar los ítems más fuertes primero
    for item in items:
        if salud_restante <= 0:
            break
        salud_restante -= item
        ataques += 1

    return ataques


# Entrada
n, D = map(int, input("Ingrese n y D separados por espacio: ").split())
items = list(map(int, input(f"Ingrese {n} valores de daño de los ítems separados por espacio: ").split()))

# Cálculo del número mínimo de ataques
resultado = calcular_ataques_minimos(n, D, items)

# Salida
print(resultado)
