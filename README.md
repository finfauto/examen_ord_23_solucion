### Fundamentos de Informática. Grado Ingeniería del automóvil

# Examen convocatoria ordinaria - 18 de enero de 2023

## Parte 1. (3 puntos)

En el fichero errores.py se encuentran una serie de funciones que contienen errores que podrían ser tanto sintácticos por un mal uso del lenguaje como lógicos por un algoritmo erróneo.

Cada función va acompañada de un test que se puede localizar en *tests/test_errores.py*, de forma que al ejecutar cada uno de esos tests podemos:

* Comprobar el tipo de error que tiene nuestro código para así poder arreglar nuestra función.
* Una vez arreglada nuestra función podemos comprobar que el arreglo es correcto si el test ejecuta sin fallo.

En dicho fichero se prueba cada función con distintos valores de entradas y los casos que fallan están indicados con un comentario.

Por ejemplo, en el ejercicio 1.A, cada caso de entrada que se prueba proviene de cada una de las líneas mostradas a continuación:

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

Por lo tanto, en este caso la entrada de cada test viene definida por una tupla cuya primera posición indica la edad propuesta y en la segunda el resultado esperado que debe devolver nuestra función para ese valor de entrada.

En el caso que falla la edad de entrada son 18 años y se espera que la función devuelva que esa edad representa que se es mayor de edad (*True*). Sin embargo, la función que tenéis que arreglar está devolviendo False.

De esta forma podéis saber los datos para los que la función falla. **Si además queréis usar el depurador**, en la carpeta *programas_para_depurar* tenéis un pequeño programa para cada una de las funciones a arreglar.


### Peso de cada apartado

* 1.A -> 0.50 puntos
* 1.B -> 1 puntos
* 1.C -> 1.50 punto


## Parte 2.  (7 puntos)

Nos piden diseñar un programa que vaya monitorizando el consumo de combustible de un coche de carreras.

### Parte 2.A (2 puntos)
En primer lugar, haremos una función que nos devuelva la cantidad de combustible consumida según el modo del motor.

El modo motor es un entero que solamente puede tener 4 valores:
  * 0, cuando el motor está en máximo ahorro. En este caso el consumo será de 1 litro cada 10 kilómetros.
  * 1, cuando el motor está en modo ahorro. En este caso el consumo será de 1 litro cada 8 kilómetros.
  * 2, cuando el motor está en modo carrera. En este caso el consumo será de 1 litro cada 6 kilómetros.
  * 3, cuando el motor está en modo clasificación. En este caso el consumo será de 1 litro cada 4 kilómetros.

La declaración de la función es:

```python
def obtener_consumo_por_kilómetro(modo_motor: int) -> float:
```

### Parte 2.B (2.5 puntos)

Una vez que sabemos calcular el consumo al kilómetro según el modo motor, podemos saber cuánto se consume durante un sector cualquiera de cualquier circuito.

Se pide definir una función según esta declaración:

```python
def obtener_consumo_sector(longitud_sector: int, modo_motor: int) -> float:
    """
    Obtener la cantidad de combustible consumido en un sector según modo motor.

    Nota: Se considera que el modo motor es el mismo durante el transcurso de todo el sector

    Importante: La longitud del sector viene expresada en metros.

    :param longitud_sector:
    :param modo_motor:
    :return:
    """
```

### Parte 2.C (2.5 puntos)

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