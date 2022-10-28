"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""





def pregunta_01():
    x = open("./data.csv", "r").readlines()
    # Eliminamos saltos de linea
    x = [z.replace("\n", "") for z in x]
    # Separamos por el delimitador 
    x = [z.split("\t") for z in x]
    # Utilizamos ListComprehension para extraer solo la columna 2
    column2=[int(z[1]) for z in x ]
    #Realizamos la suma de la columna 2 y la guardamos en una variable
    listSum = sum(column2)
    return listSum


def pregunta_02():
    column1=[x[0] for x in x ]
    from collections import Counter
    listatuple = Counter(column1)
    listatuple = [(k, v) for k, v in dict.items(listatuple)]
    listatuple=listatuple.sort()
    return listatuple


def pregunta_03():
    x = open("./data.csv", "r").readlines()
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        x = [c[0:2] for c in rows]
        d = {}
        for i in x:
            if i[0] not in d.keys():
                d[i[0]] = int(i[1])
            else:
                d[i[0]] = d[i[0]] + int(i[1])

    listatuple = [(k, v) for k, v in d.items()]
    listatuple.sort()

    return listatuple

def pregunta_04():
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]
        col3 = [c[2] for c in rows]
        months = [k.split('-')[1] for k in col3]
        listatuple =[tuple([i,months.count(i)])for i in sorted (set(months))]
    return listatuple


def pregunta_05():
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
    listatuple=[tuple([i,max(d[i]),min(d[i])]) for i in d.keys()]
    return listatuple

def pregunta_06():
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
    listatuple = [(k, v) for k, v in d.items()]
    listatuple.sort()
    return listatuple


def pregunta_08():
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

    listatuple =[tuple([k,sorted(set(d[k]))]) for k in sorted(d.keys())] 
    return listatuple


def pregunta_09():
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [c[4].split(',') for c in rows]
        g = [k[:3] for i in x for k in i]
    listatuple =[tuple([l,g.count(l)]) for l in set(g)]
    listatuple=listatuple.sort()
    return listatuple


def pregunta_10():
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        rows = [line.split('\t') for line in lines]    
        x = [[c[0], c[3], c[4]] for c in rows]

        listatuple =[tuple([i[0],len(i[1].split(',')),len(i[2].split(','))]) for i in x]
    return listatuple


def pregunta_11():
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

    listatuple =[tuple([i,sum(d[i])]) for i in d.keys()]
    listatuple=listatuple.sort()

    return listatuple


def pregunta_12():
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
