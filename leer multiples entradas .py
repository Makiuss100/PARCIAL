import sys
import math

def calcular_nivel_maximo(casos):
    resultados = []
    for n in casos:
        # Calculamos la raíz cuadrada de (1 + 8n)
        k = (-1 + math.isqrt(1 + 8 * n)) // 2
        resultados.append(k)
    return resultados

def main():
    # Leer el número de casos de prueba desde la primera línea
    t = int(sys.stdin.readline().strip())
    
    # Leer los siguientes valores en líneas separadas
    casos = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        casos.append(n)
    
    # Calcular los niveles máximos
    resultados = calcular_nivel_maximo(casos)
    
    # Imprimir los resultados
    sys.stdout.write("\n".join(map(str, resultados)) + "\n")

if __name__ == "__main__":
    main()
