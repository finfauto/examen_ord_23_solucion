def obtener_consumo_por_kilometro(modo_motor: int) -> float:
    """
    El resultado será un decimal con la cantidad de combustible consumida por kilómetro. El resultado usará el litro como unidad de medida

    :param modo_motor:
    :return:
    """
    # realizar la función completa
    if modo_motor <= 0:
        return 1/10
    elif modo_motor == 1:
        return 1/8
    elif modo_motor == 2:
        return 1/6
    else:
        return 1/4


def obtener_consumo_sector(longitud_sector: int, modo_motor: int) -> float:
    """
    Obtener la cantidad de combustible consumido en un sector según modo motor.

    Nota: Se considera que el modo motor es el mismo durante el transcurso de todo el sector

    Importante: La longitud del sector viene expresada en metros.

    :param longitud_sector:
    :param modo_motor:
    :return:
    """
    assert longitud_sector >= 0, "Longitud de sector inválido"  # no tocar: no permite sectores con longitud negativa

    # realizar la función completa desde aquí
    longitud_sector_kms = longitud_sector / 1000
    return longitud_sector_kms * obtener_consumo_por_kilometro(modo_motor)


def obtener_consumo_vuelta(sectores_vuelta: [{}]) -> float:
    """
    Obtener la cantidad de combustible consumida durante una vuelta. La vuelta viene representada por el parámetro sectores_vuelta, que es una lista en la que
    cada elemento es un diccionario con información del sector

    :param sectores_vuelta:
    :return:
    """
    # realidad la función completa desde aquí
    consumo_total = 0
    for sector in sectores_vuelta:
        consumo_sector = obtener_consumo_sector(sector["longitud_sector"], sector["modo_motor"])
        consumo_total += consumo_sector
    return consumo_total
