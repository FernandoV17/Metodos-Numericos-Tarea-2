# Solución de Ecuaciones y Optimización - Métodos Numéricos para Ingeniería Biomédica

Este repositorio contiene un programa desarrollado como respuesta a la **Actividad 5: Solución de Ecuaciones y Optimización** para el curso de **Métodos Numéricos para Ingeniería Biomédica** impartido en la **Universidad Autónoma de Nuevo León**. La tarea consiste en implementar cinco métodos numéricos que permitan encontrar el punto mínimo de una función dada. El programa está escrito en Python y realiza los cálculos de forma automática, mostrando los resultados iterativos de cada método.

## Función a Optimizar

La función dada es:

f(x) = (1/2) * x^3 + e^(-x)

Para encontrar su punto mínimo, utilizamos los siguientes métodos numéricos:

1. **Método de Bisección**
2. **Iteración de Punto Fijo**
3. **Método de Newton-Raphson**
4. **Método de la Secante**
5. **Método de la Sección Áurea**

Cada método se ejecuta de forma automática, partiendo de los parámetros iniciales definidos globalmente.

## Estructura del Código

El código está organizado de la siguiente manera:

- **Parámetros Globales**: Los parámetros globales como la tolerancia (`tol`), el número máximo de iteraciones (`Iteraciones_max`) y los puntos de inicio (`p0`, `p1`, `a`, `b`) están definidos al inicio del programa.
- **Encabezado del Programa**: Se imprime un encabezado al inicio del programa que describe la tarea que realiza.
- **Métodos Numéricos**: Se implementan las funciones correspondientes a cada uno de los cinco métodos numéricos.
- **Resultados Iterativos**: Se muestra el valor aproximado de la solución en cada iteración para cada método.

## Uso

Para ejecutar el programa, simplemente clona este repositorio y corre el script `main.py`. El programa iniciará automáticamente y calculará el punto mínimo de la función dada utilizando los cinco métodos numéricos.

### Requisitos

- Python 3.x
- Módulo `math` (disponible en la biblioteca estándar de Python)
- Módulo `time` (disponible en la biblioteca estándar de Python)

### Ejecución

Clona este repositorio:

```bash
git clone https://github.com/FernandoV17/Metodos-Numericos-Tarea-2.git
cd Metodos-Numericos-Tarea-2
```

Ejecuta el script:

```bash
python3 main.py
```

### Ejemplo de Salida

El programa imprimirá lo siguiente en la consola:

```
###########################
# Programa que hace algo  #
###########################

Parámetros globales:
Tol = 1e-05
Máx Iteraciones = 100
Puntos Iniciales: p0 = 1.0, p1 = 2.0
Intervalo [a,b] = [0.5,1.5]

Iniciando en 3...
Iniciando en 2...
Iniciando en 1...
Ejecutando...

Iteración [1] valor = ...
Iteración [2] valor = ...
...
```

## Resultados

El programa muestra una tabla resumen de los valores aproximados de la solución para cada método en cada iteración. Estos resultados deben ser presentados en el informe final, junto con el código y una explicación clara y ordenada de los métodos y resultados obtenidos.

### Autor

El codigo fue escrito originalmente por Fernando Villarreal. Equipo con Oscar Eduardo Reyes Pereyra y Julio Alejandro Galindo Estrada

Este proyecto fue desarrollado como parte de la **Actividad 5** del curso de **Métodos Numéricos para Ingeniería Biomédica** de la **Universidad Autónoma de Nuevo León**.

Catedrático: **Dr. Miguel Mata Pérez**

Fecha de entrega: *[Completa con la fecha de entrega correspondiente]*
