from math import inf

import pytest

from errores import mayor_de_edad, elimina_n, extrae_vuelta_rapida, intercambiar_variables

#############################################################
#                      Test Parte 1.A                       #
#############################################################

testdata_mayor_de_edad = [
    (-inf, False),
    (-18, False),
    (0, False),
    (17, False),
    (18, True),  # <- Falla en este caso
    (+inf, True)
]


@pytest.mark.parametrize("edad, es_mayor_de_edad_esperado", testdata_mayor_de_edad)
def test_mayor_de_edad(edad, es_mayor_de_edad_esperado):
    assert mayor_de_edad(edad) == es_mayor_de_edad_esperado


#############################################################


#############################################################
#                      Test Parte 1.B                       #
#############################################################

testdata_extra_vuelta_rapida = [
    ([], None),
    ([{"número": 1, "tiempo": 70.100}, {"numero": 2, "tiempo": 69.180}], 69.180),  # <- Falla en este caso
    ([{"número": 1, "tiempo": 69.180}, {"numero": 2, "tiempo": 70.100}], 69.180)  # <- Falla en este caso
]


@pytest.mark.parametrize("vueltas, mejor_tiempo_esperado", testdata_extra_vuelta_rapida)
def test_extra_vuelta_rapida(vueltas, mejor_tiempo_esperado):
    assert extrae_vuelta_rapida(vueltas) == mejor_tiempo_esperado


#############################################################
#                      Test Parte 1.C                       #
#############################################################

testdata_intercambiar_variables = [
    (1, 2, 2, 1),  # <- Falla en este caso
    (1, 2000, 2000, 1),  # <- Falla en este caso
    ("hola", "adios", "adios", "hola"),  # <- Falla en este caso
    (1, "hola", "hola", 1)  # <- Falla en este caso
]


@pytest.mark.parametrize("a, b, nueva_a_esperada, nueva_b_esperada", testdata_intercambiar_variables)
def test_intercambiar_variables(a, b, nueva_a_esperada, nueva_b_esperada):
    assert intercambiar_variables(a, b) == (nueva_a_esperada, nueva_b_esperada)


#############################################################
