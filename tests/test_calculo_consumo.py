import pytest

from calculo_consumo import obtener_consumo_por_kilometro, obtener_consumo_vuelta, obtener_consumo_sector

testdata_consumo_por_kilometro = [
    (0, 1/10),
    (1, 1/8),
    (2, 1/6),
    (3, 1/4),
]


@pytest.mark.parametrize("modo_motor, consumo_por_kilometro_esperado", testdata_consumo_por_kilometro)
def test_consumo_por_kilometro(modo_motor, consumo_por_kilometro_esperado):
    assert obtener_consumo_por_kilometro(modo_motor) == pytest.approx(consumo_por_kilometro_esperado)


testdata_consumo_sector = [
    (500, 0, 0.05),
    (1000, 0, 0.1),
    (5000, 0, 0.5),
    (500, 1, 0.0625),
    (1000, 1, 0.125),
    (5000, 1, 0.625),
    (500, 2, 0.08333333333333333),
    (1000, 2, 0.16666666666666666),
    (5000, 2, 0.8333333333333333),
    (500, 3, 0.125),
    (1000, 3, 0.25),
    (5000, 3, 1.25),
]


@pytest.mark.parametrize("longitud_sector, modo_motor, consumo_esperado", testdata_consumo_sector)
def test_consumo_sector(longitud_sector, modo_motor, consumo_esperado):
    assert obtener_consumo_sector(longitud_sector, modo_motor) == pytest.approx(consumo_esperado)


testdata_consumo_vuelta = [
    (
        [
            {
                "id_sector": 0,
                "longitud_sector": 654,
                "modo_motor": 3
            },
            {
                "id_sector": 1,
                "longitud_sector": 420,
                "modo_motor": 3
            },
            {
                "id_sector": 2,
                "longitud_sector": 900,
                "modo_motor": 3
            },
            {
                "id_sector": 3,
                "longitud_sector": 439,
                "modo_motor": 3
            }
        ], 0.6032500000000001
    ),
    (
        [
            {
                "id_sector": 0,
                "longitud_sector": 654,
                "modo_motor": 2
            },
            {
                "id_sector": 1,
                "longitud_sector": 420,
                "modo_motor": 1
            },
            {
                "id_sector": 2,
                "longitud_sector": 900,
                "modo_motor": 2
            },
            {
                "id_sector": 3,
                "longitud_sector": 439,
                "modo_motor": 2
            }
        ], 0.38466666666666666
    ),
    (
        [
            {
                "id_sector": 0,
                "longitud_sector": 654,
                "modo_motor": 1
            },
            {
                "id_sector": 1,
                "longitud_sector": 420,
                "modo_motor": 1
            },
            {
                "id_sector": 2,
                "longitud_sector": 900,
                "modo_motor": 0
            },
            {
                "id_sector": 3,
                "longitud_sector": 439,
                "modo_motor": 0
            }
        ], 0.26815
    ),
    (
        [], 0
    )
]


@pytest.mark.parametrize("sectores, consumo_esperado", testdata_consumo_vuelta)
def test_consumo_vuelta(sectores, consumo_esperado):
    assert obtener_consumo_vuelta(sectores) == pytest.approx(consumo_esperado)
