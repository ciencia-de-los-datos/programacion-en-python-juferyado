"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------
Este archivo contiene las preguntas que se van a realizar en el laboratorio.
No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.
Utilice el archivo `data.csv` para resolver las preguntas.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    x = open("./data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    column2=[int(z[1]) for z in x ]
    listSum = sum(column2)
    return listSum

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
    x = open("./data.csv", "r").readlines()
    column1=[x[0] for x in x ]
    print (column1)
    listatuple =[tuple([x,column1.count(x)]) for x in set(column1)]
    listatuple.sort()
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        print (rows)
        x = [c[0:2] for c in rows]
        print (x)
        d = {}
        for i in x:
            if i[0] not in d.keys():
                d[i[0]] = int(i[1])
            else:   
                d[i[0]] = d[i[0]] + int(i[1])      
    list = [(k, v) for k, v in d.items()]
    list.sort()
    return list


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        col3 = [c[2] for c in rows]
        months = [k.split('-')[1] for k in col3]
        listatuple =[tuple([i,months.count(i)])for i in sorted (set(months))]
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        x = [c[0:2] for c in rows]
        d = {}
        for i in x:
            if i[0] not in d.keys():
                d[i[0]] = [int(i[1])]
            else:
                d[i[0]].append(int(i[1]))
    listatuple=[tuple([i,max(d[i]),min(d[i])]) for i in sorted(d.keys())]
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [c[4].split(',') for c in rows]
        d = {}
        for l in x:
            for e in l:
                if e[:3] not in d.keys():
                    r=e[:].split(":")
                    r=r[1]
                    d[e[:3]] = [int(r)]
                                
                else:
                    r=e[:].split(":")
                    r=r[1]
                    d[e[:3]].append(int(r))
    listatuple =[tuple([i,min(d[i]),max(d[i])]) for i in d.keys()]
    listatuple.sort()
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        x = [c[:2] for c in rows]
        d = {}
        for i in x:
            if i[1] not in d.keys():
                d[i[1]] = [i[0]]
            else:
                d[i[1]].append(i[0])
    listatuple=[tuple([int(k),d[k]]) for k in sorted(d.keys())]
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        x = [c[:2] for c in rows]
        d = {}
        for i in x:
            if i[1] not in d.keys():
                d[i[1]] = [i[0]]
            else:
                d[i[1]].append(i[0])
    listatuple=[tuple([int(k),sorted(set(d[k]))]) for k in sorted(d.keys())]
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [c[4].split(',') for c in rows]
        g = [k[:3] for i in x for k in i]
    d={l:g.count(l) for l in sorted(set(g))}
    return d


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [[c[0], c[3], c[4]] for c in rows]

        listatuple =[tuple([i[0],len(i[1].split(',')),len(i[2].split(','))])for i in x]
    return listatuple


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
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [[c[1], c[3].split(',')] for c in rows]
        d = {}
        for r in x:        
            for l in r[1]:
                if l not in d.keys():
                    d[l] = [int(r[0])]
                else:
                    d[l].append(int(r[0]))
    d={i:sum(d[i]) for i in sorted(d.keys())}
    return d


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
    import re
    d = {}
    Lista=[]
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [[c[0], c[4]] for c in rows]
        for k in x:
            num = re.findall('\d+', k[1])
            num = [int(i) for i in num]
            Lista+=[[k[0],sum(num)]]
        for i in Lista:
            if i[0] not in d.keys():
                d[i[0]] = int(i[1])
            else:
                d[i[0]] = d[i[0]] + int(i[1])
                
    d=dict(sorted(d.items()))
    return d
