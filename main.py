import math
import time

def header():
    print("##########################################################################")
    print("# Programa que calcula los 0s de una ecuacion usando diferentes metodos  #")
    print("##########################################################################\n")
    print("\n")
    print("Metodos Numericos: AD2024")
    print("\n")
    print("Integrantes:")
    print("Fernando Villarreal Castillo 2049219")   
    print("Julio Alejandro Galindo Estrada 1945686")    
    print("Oscar Eduardo Reyes Pereyra  2109292")  
    print("\n") 

tol = 10e-10
Iteraciones_max = 1000
p0 = 0  # Punto inicial para los métodos que lo requieren
p1 = 100  # Segundo punto inicial para el método de la secante
a = 0   # Límite inferior del intervalo
b = 100   # Límite superior del intervalo

def punto_fijo(p0, tol, M):
    i = 1
    while i <= M:
        p = math.sqrt((2 * math.exp(-p0)) / 3)  # g(x)
        if abs(p - p0) < tol:
            print("Punto Fijo: El resultado es =", p)
            return p
        p0 = p
        print(f"\tIteración [{i}] valor = {p}")
        i += 1
    print("Lo siento, no se alcanzó la tolerancia deseada.")
    return p

def biseccion(a, b, tol, M):
    i = 1
    FA = (1.5 * a ** 2) - math.exp(-a)
    while i <= M:
        p = (a + b) / 2
        FP = (1.5 * p ** 2) - math.exp(-p)
        if abs(b - a) / 2 < tol:
            print("Bisección: El resultado es =", p)
            return p
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
        print(f"\tIteración [{i}] valor = {p}")
        i += 1
    print("Lo siento, no se alcanzó la tolerancia deseada.")
    return p

def newton_raphson(p0, tol, M):
    i = 1
    while i <= M:
        fx = (1.5 * p0 ** 2) - math.exp(-p0)
        dx = 3 * p0 + math.exp(-p0)
        p = p0 - (fx / dx)
        if abs(p - p0) < tol:
            print("Newton-Raphson: El resultado es =", p)
            return p
        p0 = p
        print(f"\tIteración [{i}] valor = {p}")
        i += 1
    print("Lo siento, no se alcanzó la tolerancia deseada.")
    return p

def secante(p0, p1, tol, M):
    i = 2
    q0 = (1.5 * p0 ** 2) - math.exp(-p0)
    q1 = (1.5 * p1 ** 2) - math.exp(-p1)
    while i <= M:
        p = p1 - (q1 * (p1 - p0) / (q1 - q0))
        if abs(p - p1) < tol:
            print("Secante: El resultado es =", p)
            return p
        p0, p1 = p1, p
        q0, q1 = q1, (1.5 * p1 ** 2) - math.exp(-p1)
        print(f"\tIteración [{i}] valor = {p}")
        i += 1
    print("Lo siento, no se alcanzó la tolerancia deseada.")
    return p

def seccion_aurea(a, b, tol, M):
    phi = (math.sqrt(5) - 1) / 2
    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)
    f1 = (0.5 * x1 ** 3) + math.exp(-x1)
    f2 = (0.5 * x2 ** 3) + math.exp(-x2)
    i = 1
    while i <= M:
        if abs(b - a) < tol:
            print("Sección Áurea: El resultado es =", (a + b) / 2)
            return (a + b) / 2
        if f1 < f2:
            b = x2
            x2 = x1
            x1 = b - phi * (b - a)
            f2 = f1
            f1 = (0.5 * x1 ** 3) + math.exp(-x1)
        else:
            a = x1
            x1 = x2
            x2 = a + phi * (b - a)
            f1 = f2
            f2 = (0.5 * x2 ** 3) + math.exp(-x2)
        print(f"\tIteración [{i}] valor = {(a + b) / 2}")
        i += 1
    print("Lo siento, no se alcanzó la tolerancia deseada.")
    return (a + b) / 2

def main():
    header()

    time.sleep(1)

    print(f"Parámetros globales:\nTol = {tol}\nMáx Iteraciones = {Iteraciones_max}\nPuntos Iniciales: p0 = {p0}, p1 = {p1}\nIntervalo [a,b] = [{a},{b}]\n")

    for i in range(3, 0, -1):
        print(f"Iniciando en {i}...")
        time.sleep(1)
    print("Ejecutando...\n")

    punto_fijo(p0, tol, Iteraciones_max)
    biseccion(a, b, tol, Iteraciones_max)
    newton_raphson(p0, tol, Iteraciones_max)
    secante(p0, p1, tol, Iteraciones_max)
    seccion_aurea(a, b, tol, Iteraciones_max)

if __name__ == "__main__":
    main()
