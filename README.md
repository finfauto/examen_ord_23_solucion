### Fundamentos de Informática. Grado Ingeniería del automóvil

# Examen convocatoria ordinaria - 18 de enero de 2023

## Parte 1.

En el fichero errores.py se encuentran una serie de funciones que contienen errores tanto sintácticos por un mal uso del lenguaje como lógicos por un algoritmo erróneo.

Cada función va acompañada de un test que se puede localizar en tests/test_errores.py, de forma que al ejecutar cada uno de esos tests podemos:

* Lanzar cada test y comprobar el tipo de error que tiene nuestro código, para así poder arreglar nuestra función.
* Una vez arreglada nuestra función podemos comprobar que el arreglo es correcto si el test ejecuta sin fallo.

En dicho fichero se prueba la función para distintas entradas. El caso que falla está marcado con un comentario.

Por ejemplo, en el ejercicio 1.A los datos de entrada que se prueban son estos:

```python
testdata_mayor_de_edad = [
    (-inf, False),
    (-18, False),
    (0, False),
    (17, False),
    (18, True),  # <- Falla en este caso
    (+inf, True)
]
```

Cada entrada de la lista testdata_mayor_de_edad es un test diferente cuyos datos vienen en una tupla. En la primera posición viene la edad propuesta y en la segunda el resultado que se espera que dé la función a probar.

En el caso que falla se espera que si la edad de entrada son 18 años, la función indique efectivamente es mayor de edad (True). Pero la función que tenéis que arreglar está devolviendo False.

De esta forma podéis saber los datos para los que la función falla y que hay que corregir. **Si además queréis usar el depurador**, en la carpeta *programas_para_depurar* tenéis un pequeño programa para cada una de las funciones a arreglar. Tendréis que completar el programa de prueba con los datos que queréis probar, que podéis obtener de los tests como habéis visto.


### Peso de cada apartado

* 1.A -> 0.5 puntos
* 1.B -> 0.75 puntos
* 1.C -> 1.25 punto
* 1.D -> 1.5 punto



## Parte 2.

Nos piden diseñar un programa que vaya monitorizando el consumo de combustible de un coche de carreras.

### Parte 2.A (1 punto)
En primer lugar haremos una función que nos devuelva la cantidad de combustible consumida según el modo del motor

El modo motor es un entero que solamente puede tener 4 valores:
  * 0 o menor, cuando el motor está en máximo ahorro. En este caso el consumo será de 1 litro cada 10 kilómetros (10_000 metros)
  * 1, cuando el motor está en modo ahorro. En este caso el consumo será de 1 litro cada 8 kilómetros (8_000 metros)
  * 2, cuando el motor está en modo carrera. En este caso el consumo será de 1 litro cada 6 kilómetros (6_000 metros)
  * 3 o mayor, cuando el motor está en modo clasificación. En este caso el consumo será de 1 litro cada 4 kilómetros (4_000 metros)

La declaración de la función es:

```python
def obtener_consumo_por_kilómetro(modo_motor: int) -> float:
```

### Parte 2.B (2.5 puntos)

Una vez que sabemos calcular el consumo al kilómetro según el modo motor, podemos saber cuánto se consume durante un sector cualquier de cualquier circuito.

Se pide definir una función según esta declaración:

```python
def obtener_consumo_sector(longitud_sector: int, modo_motor: int) -> float:
    """
    Obtener la cantidad de combustible consumido en un sector según modo motor. Para ello, ayudarse de la función obtener_consumo_por_kilometro

    Nota: Se considera que el modo motor es el mismo durante el transcurso de todo el sector

    Importante: La longitud del sector viene expresada en metros.

    :param longitud_sector:
    :param modo_motor:
    :return:
    """
```

### Parte 2.C (2.5)

Cada vuelta se compone de una lista de sectores. Nos piden definir una función que calcule el consumo en una vuelta teniendo como datos de entrada una lista de sectores, donde cada sector es un diccionario con los sigiuentes elementos:

* id_sector: Identificador del sector.
* longitud_sector: Longitud en metros del sector
* modo_motor: Modo usado durante el recorrido del sector

```python
def obtener_consumo_vuelta(sectores_vuelta: [{}]) -> float:
    """
    Obtener la cantidad de combustible consumida durante una vuelta. La vuelta viene representada por el parámetro sectores_vuelta, que es una lista en la que
    cada elemento es un diccionario con información del sector

    :param sectores_vuelta:
    :return:
    """
```