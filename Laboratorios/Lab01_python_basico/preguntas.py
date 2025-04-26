"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

x = 1
m = x + 2

data = open("data.csv")


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv") as hd:
        lista = []
        for linea in hd:
            linea = linea.strip().split()
            numero = int(linea[1])
            lista.append(numero)
    return sum(lista)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    hd = open("data.csv")
    lista = []
    diccionario = {}
    new_sequence = []
    for linea in hd:
        linea = linea.strip().split()
        letra = linea[0]
        lista.append((letra, 1))

    lista = sorted(lista, key=lambda x: x[0])
    # key = A  ---  value = 1
    for key, value in lista:
        diccionario[key] = diccionario.get(key, 0) + 1

    for key, value in diccionario.items():
        new_sequence.append((key, value))

    return new_sequence


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista = []
    lista2 = []
    diccionario = {}
    hd = open("data.csv")
    for linea in hd:
        linea = linea.split()
        lista.append(linea[0:2])

    for key, value in lista:
        diccionario[key] = diccionario.get(key, 0) + int(value)

    for key, value in diccionario.items():
        lista2.append((key, value))
        lista = sorted(lista2, key=lambda x: x[0])

    return lista


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista = []
    lista2 = []
    diccionario = {}
    with open("data.csv") as hd:
        lista = [linea.rstrip().split()[2] for linea in hd]
        for fecha in lista:
            fecha = fecha.split(sep="-")
            diccionario[fecha[1]] = diccionario.get(fecha[1], 0) + 1
        lista2 = sorted(
            [(key, value) for key, value in diccionario.items()], key=lambda x: x[0]
        )

    return lista2


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    diccionario = {}
    lista = []
    with open("data.csv") as hd:

        for linea in hd:
            linea = linea.strip().split()
            letra, num = (linea[0], int(linea[1]))
            lista.append((letra, num))

        for letra, valor in lista:
            if letra not in diccionario:
                diccionario[letra] = {"maxi": valor, "mini": valor}
            else:
                diccionario[letra]["maxi"] = max(diccionario[letra]["maxi"], valor)
                diccionario[letra]["mini"] = min(diccionario[letra]["mini"], valor)
    lista_resultados = [
        (letra, valores["maxi"], valores["mini"])
        for letra, valores in diccionario.items()
    ]
    lista_resultados = sorted(lista_resultados, key=lambda x: x[0])
    return lista_resultados


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista = []
    diccionario = {}
    with open("data.csv") as hd:

        for linea in hd:
            linea = linea.strip().split()[4].split(",")
            for elemento in linea:
                elemento, valor = elemento.split(":")
                lista.append((elemento, int(valor)))
        for elemento, valor in lista:
            if elemento not in diccionario:
                diccionario[elemento] = {"maxi": valor, "mini": valor}
            else:
                diccionario[elemento]["maxi"] = max(
                    diccionario[elemento]["maxi"], valor
                )
                diccionario[elemento]["mini"] = min(
                    diccionario[elemento]["mini"], valor
                )
    lista_resultados = [
        (elemento, valores["mini"], valores["maxi"])
        for elemento, valores in diccionario.items()
    ]
    lista_resultados = sorted(lista_resultados, key=lambda x: x[0])
    return lista_resultados


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    with open("data.csv") as hd:
        lista = []
        diccionario = {}
        for linea in hd:
            linea = linea.strip().split()
            letra, numero = linea[0:2]
            numero = int(numero)
            lista.append((numero, letra))
        for numero, letra in lista:
            if numero not in diccionario.keys():
                diccionario[numero] = []
            diccionario[numero].append(letra)
        nueva_lista = [
            (numero, letras)
            for numero, letras in sorted(diccionario.items(), key=lambda x: x[0])
        ]
    return nueva_lista


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv") as hd:
        lista = []
        diccionario = {}
        for linea in hd:
            linea = linea.strip().split()
            letra, numero = linea[0:2]
            numero = int(numero)
            lista.append((numero, letra))
        for numero, letra in lista:
            if numero not in diccionario.keys():
                diccionario[numero] = []
            diccionario[numero].append(letra)
        nueva_lista = [
            (numero, sorted(set(letras)))
            for numero, letras in sorted(diccionario.items(), key=lambda x: x[0])
        ]
        print(diccionario)
    return nueva_lista


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    lista = []
    diccionario = {}
    with open("data.csv") as hd:

        for linea in hd:
            linea = linea.strip().split()[4].split(",")
            # print(linea)
            for elemento in linea:
                elemento = elemento.split(":")[0]
                # print(elemento)
                diccionario[elemento] = diccionario.get(elemento, 0) + 1
                nuevo_diccionario = dict(
                    sorted(diccionario.items(), key=lambda x: x[0])
                )

    return nuevo_diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv") as hd:
        lista = []
        for linea in hd:
            linea = linea.strip().split()
            (num, cant, cant2) = (
                linea[0],
                len(linea[3].split(",")),
                len(linea[4].split(",")),
            )
            lista.append((num, cant, cant2))
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    diccionario = {}
    with open("data.csv") as hd:
        for linea in hd:
            _, num, _, letras, _ = linea.split()
            num = int(num)
            for letra in letras.split(","):
                diccionario[letra] = diccionario.get(letra, 0) + num
        nuevo = dict(sorted(diccionario.items(), key=lambda x: x[0]))
    return nuevo


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    lista = []
    with open("data.csv") as hd:
        for linea in hd:
            clave, _, _, _, valores = linea.split()
            valores = valores.split(",")
            for par in valores:
                _, valor = par.split(":")
                lista.append((clave, int(valor)))
        for clave, valor in lista:
            if clave not in diccionario.keys():
                diccionario[clave] = []
            diccionario[clave].append(valor)
        for clave, valor in diccionario.items():
            diccionario[clave] = sum(diccionario[clave])
        diccionario = dict(sorted(diccionario.items(), key=lambda x: x[0]))
    return diccionario


# print(pregunta_01())
# print(pregunta_02())
# print(pregunta_03())
# print(pregunta_04())
# print(pregunta_05())
# print(pregunta_06())
# print(pregunta_07())
# print(pregunta_08())
# print(pregunta_09())
# print(pregunta_10())
# print(pregunta_11())
# print(pregunta_12())