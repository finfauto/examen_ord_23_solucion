#############################################################
#                        Parte 1.A                          #
#############################################################

def mayor_de_edad(edad: int) -> bool:
    """
    Esta función recibe la edad de una persona y devuelve si corresponde
    a una persona mayor de edad

    :param edad:
    :return:
    """
    # Modifica lo que creas oportuno desde aquí
    return edad >= 18
    # Hasta aquí

#############################################################


#############################################################
#                        Parte 1.B                          #
#############################################################

def extrae_vuelta_rapida(lista_de_vueltas: [{}]) -> float:
    """
    Dada una lista de vueltas donde cada vuelta está representada por un diccionario con las siguientes claves:
    - número: entero que indica el número de la vuelta
    - tiempo: decimal con el tiempo por vuelta en segundos. Por ejemplo, un tiempo de "1:10.100", estaría representado por el float 70.100

    Esta función devuelve el tiempo de la vuelta más rápida. En el caso de que no haya ninguna vuelta, la función devolverá None

    :param lista_de_vueltas:
    :return:
    """

    vuelta_rapida = None
    for datos_vuelta in lista_de_vueltas:
        tiempo_vuelta = datos_vuelta["tiempo"]
        if vuelta_rapida == None:  # El editor te subraya esta parte porque prefiere que pongas "if vuelta_rapida is None:". NO IMPORTA
            vuelta_rapida = tiempo_vuelta
        else:
            if tiempo_vuelta < vuelta_rapida:
                vuelta_rapida = tiempo_vuelta
    return vuelta_rapida


#############################################################


#############################################################
#                        Parte 1.C                          #
#############################################################

def intercambiar_variables(a, b):
    """
    Dados dos parámetros con forma de string, devolverlos intercambiados

    Por ejemplo:
    Si el valor de entrada a es 1 y el de b es 2, deberás conseguir que a
    la salida el valor de a sea 2 y el de 1

    Nota: No importa el tipo de los datos. En el ejemplo es un int, pero podría ser cualquier tipo
    :param a:
    :param b:
    :return:
    """
    # Añade o modifica lo que creas oportuno desde aquí
    a_aux = a
    a = b
    b = a_aux
    # Hasta aquí
    return a, b

#############################################################
