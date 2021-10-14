
#Hola becario me preguntaba si me puedes ayudar a checar el código completo y los comentarios, gracias <3
"""
Un diccionario funciona como un
 libro en el que cada página es el elemento y cuando tu la buscas en el
 indice te da la información que yo ingrese en esa página: aquí cree el libro
 """
mydict = {'H': ['Hidrógeno', 'Num Atómico : 1', 'Periodo,Grupo:1,1', 'Peso atómico:1.00784(7)^2^3^4'],
          'He': ['Helio', 'Num Atómico : 2', 'Periodo,Grupo:1,18', 'Peso atómico:4.002602(2)^2^4'],
          'Li': ['Litio', 'Num Atómico : 3', 'Periodo,Grupo:2,1', 'Peso atómico:6.941(2)2^3^4^5'],
          'Be': ['Berilio', 'Num Atómico : 4', 'Periodo,Grupo:2,2', 'Peso atómico:9.012182(3)'],
          'B': ['Boro', 'Num Atómico : 5', 'Periodo,Grupo:2,13', 'Peso atómico:10.811(7)^2^3^4'],
          'C': ['Carbono', 'Num Atómico : 6', 'Periodo,Grupo:2,14', 'Peso atómico:12.0107(8)^2^4'],
          'N': ['Nitrógeno', 'Num Atómico : 7', 'Periodo,Grupo:2,15', 'Peso atómico:14.0067(2)^2^4'],
          'O': ['Oxígeno', 'Num Atómico : 8', 'Periodo,Grupo:2,16', 'Peso atómico:15.9994(3)^2^4'],
          'F': ['Flúor', 'Num Atómico : 9', 'Periodo,Grupo:2,17', 'Peso atómico:18.9984032(5)'],
          'Ne': ['Neón', 'Num Atómico : 10', 'Periodo,Grupo:2,18', 'Peso atómico:20.1797(6)^2^3'],
          'Na': ['Sodio', 'Num Atómico : 11', 'Periodo,Grupo:3,1', 'Peso atómico:22.98976928(2)'],
          'Mg': ['Magnesio', 'Num Atómico : 12', 'Periodo,Grupo:3,2', 'Peso atómico:24.3050(6)'],
          'Al': ['Aluminio', 'Num Atómico : 13', 'Periodo,Grupo:3,13', 'Peso atómico:26.9815386(8)'],
          'Si': ['Silicio', 'Num Atómico : 14', 'Periodo,Grupo:3,14', 'Peso atómico:28.0855(3)^4'],
          'P': ['Fósforo', 'Num Atómico : 15', 'Periodo,Grupo:3,15', 'Peso atómico:30.973762(2)'],
          'S': ['Azufre', 'Num Atómico : 16', 'Periodo,Grupo:3,16', 'Peso atómico:32.065(5)^2^4'],
          'Cl': ['Cloro', 'Num Atómico : 17', 'Periodo,Grupo:3,17', 'Peso atómico:35.453(2)^2^3^4'],
          'Ar': ['Argón', 'Num Atómico : 18', 'Periodo,Grupo:3,18', 'Peso atómico:39.948(1)^2^4'],
          'K': ['Potasio', 'Num Atómico : 19', 'Periodo,Grupo:4,1', 'Peso atómico:39.0983(1)'],
          'Ca': ['Calcio', 'Num Atómico : 20', 'Periodo,Grupo:4,2', 'Peso atómico:40.078(4)^2'],
          'Se': ['Selenio', 'Num Atómico : 34', 'Periodo,Grupo:4,16', 'Peso atómico:78.96(3)^4'],
          'Ti': ['Talio', 'Num Atómico : 81', 'Periodo,Grupo:6,13', 'Peso atómico:204.3833(2)'],
          'V': ['Vanadio', 'Num Atómico : 23', 'Periodo,Grupo:4,5', 'Peso atómico:50.9415(1)'],
          'Cr': ['Cromo', 'Num Atómico : 24', 'Periodo,Grupo:4,6', 'Peso atómico:51.9961(6)'],
          'Mn': ['Manganeso', 'Num Atómico : 25', 'Periodo,Grupo:4,7', 'Peso atómico:54.938045(5)'],
          'Fe': ['Hierro', 'Num Atómico : 26', 'Periodo,Grupo:4,8', 'Peso atómico:55.845(2)'],
          'Co': ['Cobalto', 'Num Atómico : 27', 'Periodo,Grupo:4,9', 'Peso atómico:58.933200(9)'],
          'Ni': ['Niquel', 'Num Atómico : 28', 'Periodo,Grupo:4,10', 'Peso atómico:58.6934(2)'],
          'Cu': ['Cobre', 'Num Atómico : 29', 'Periodo,Grupo:4,11', 'Peso atómico:63.546(3)^4'],
          'Zn': ['Cinc', 'Num Atómico : 30', 'Periodo,Grupo:4,12', 'Peso atómico:65.409(4)'],
          'Ga': ['Galio', 'Num Atómico : 31', 'Periodo,Grupo:4,13', 'Peso atómico:69.723(1)'],
          'Ge': ['Germanio', 'Num Atómico : 32', 'Periodo,Grupo:4,14', 'Peso atómico:72.64(1)'],
          'As': ['Arsénico', 'Num Atómico : 33', 'Periodo,Grupo:4,15', 'Peso atómico:74.92160(2)'],
          'Br': ['Bromo', 'Num Atómico : 35', 'Periodo,Grupo:4,17', 'Peso atómico:79.904(1)'],
          'Kr': ['Kriptón', 'Num Atómico : 36', 'Periodo,Grupo:4,18', 'Peso atómico:83.798(2)^2^3'],
          'Rb': ['Rubidio', 'Num Atómico : 37', 'Periodo,Grupo:5,1', 'Peso atómico:85.4678(3)^2'],
          'Sr': ['Estroncio', 'Num Atómico : 38', 'Periodo,Grupo:5,2', 'Peso atómico:87.62(1)^2^4'],
          'Y': ['Ytrio', 'Num Atómico : 39', 'Periodo,Grupo:5,3', 'Peso atómico:88.90585(2)'],
          'Zr': ['Circonio', 'Num Atómico : 40', 'Periodo,Grupo:5,4', 'Peso atómico:91.224(2)^2'],
          'Nb': ['Niobio', 'Num Atómico : 41', 'Periodo,Grupo:5,5', 'Peso atómico:92.906 38(2)'],
          'Mo': ['Molibdeno', 'Num Atómico : 42', 'Periodo,Grupo:5,6', 'Peso atómico:95.94(2)^2'],
          'Tc': ['Tecnecio', 'Num Atómico : 43', 'Periodo,Grupo:5,7', 'Peso atómico:[98.9063]^6'],
          'Ru': ['Rutenio', 'Num Atómico : 44', 'Periodo,Grupo:5,8', 'Peso atómico:101.07(2)^2'],
          'Rh': ['Rodio', 'Num Atómico : 45', 'Periodo,Grupo:5,9', 'Peso atómico:102.90550(2)'],
          'Pd': ['Paladio', 'Num Atómico : 46', 'Periodo,Grupo:5,10', 'Peso atómico:106.42(1)^2'],
          'Ag': ['Plata', 'Num Atómico : 47', 'Periodo,Grupo:5,11', 'Peso atómico:107.8682(2)^2'],
          'Cd': ['Cadmio', 'Num Atómico : 48', 'Periodo,Grupo:5,12', 'Peso atómico:112.411(8)^2'],
          'In': ['Indio', 'Num Atómico : 49', 'Periodo,Grupo:5,13', 'Peso atómico:114.818(3)'],
          'Sn': ['Estaño', 'Num Atómico : 50', 'Periodo,Grupo:5,14', 'Peso atómico:118.710(7)^2'],
          'Sb': ['Antimonio', 'Num Atómico : 51', 'Periodo,Grupo:5,15', 'Peso atómico:121.760(1)^2'],
          'Te': ['Teluro', 'Num Atómico : 52', 'Periodo,Grupo:5,16', 'Peso atómico:127.60(3)^2'],
          'I': ['Yodo', 'Num Atómico : 53', 'Periodo,Grupo:5,17', 'Peso atómico:126.90447(3)'],
          'Xe': ['Xenón', 'Num Atómico : 54', 'Periodo,Grupo:5,18', 'Peso atómico:131.293(6)^2^3'],
          'Cs': ['Cesio', 'Num Atómico : 55', 'Periodo,Grupo:6,1', 'Peso atómico:132.9054519(2)'],
          'Ba': ['Bario', 'Num Atómico : 56', 'Periodo,Grupo:6,2', 'Peso atómico:137.327(7)'],
          'La': ['Lantano', 'Num Atómico : 57', 'Periodo:6', 'Peso atómico:138.90547(7)^2'],
          'Ce': ['Cerio', 'Num Atómico : 58', 'Periodo:6', 'Peso atómico:140.116(1)^2'],
          'Pr': ['Praseodimio', 'Num Atómico : 59', 'Periodo:6', 'Peso atómico:140.90765(2)'],
          'Nd': ['Neodimio', 'Num Atómico : 60', 'Periodo:6', 'Peso atómico:144.242(3)^2'],
          'Pm': ['Prometio', 'Num Atómico : 61', 'Periodo:6', 'Peso atómico:[146.9151]^6'],
          'Sm': ['Samario', 'Num Atómico : 62', 'Periodo:6', 'Peso atómico:150.36(2)^2'],
          'Eu': ['Europio', 'Num Atómico : 63', 'Periodo:6', 'Peso atómico:151.964(1)^2'],
          'Gd': ['Gadolinio', 'Num Atómico : 64', 'Periodo:6', 'Peso atómico:157.25(3)^2'],
          'Tb': ['Terbio', 'Num Atómico : 65', 'Periodo:6', 'Peso atómico:158.92535(2)'],
          'Dy': ['Disprosio', 'Num Atómico : 66', 'Periodo:6', 'Peso atómico:162.500(1)^2'],
          'Ho': ['Holmio', 'Num Atómico : 67', 'Periodo:6', 'Peso atómico:164.93032(2)'],
          'Er': ['Erbio', 'Num Atómico : 68', 'Periodo:6', 'Peso atómico:167.259(3)^2'],
          'Tm': ['Tulio', 'Num Atómico : 69', 'Periodo:6', 'Peso atómico:168.93421(2)'],
          'Yb': ['Iterbio', 'Num Atómico : 70', 'Periodo:6', 'Peso atómico:173.04(3)^2'],
          'Lu': ['Lutecio', 'Num Atómico : 71', 'Periodo,Grupo:6,3', 'Peso atómico:174.967(1)^2'],
          'Hf': ['Hafnio', 'Num Atómico : 72', 'Periodo,Grupo:6,4', 'Peso atómico:178.49(2)'],
          'Ta': ['Tántalo', 'Num Atómico : 73', 'Periodo,Grupo:6,5', 'Peso atómico:180.9479(1)'],
          'W': ['Wolframio', 'Num Atómico : 74', 'Periodo,Grupo:6,6', 'Peso atómico:183.84(1)'],
          'Re': ['Renio', 'Num Atómico : 75', 'Periodo,Grupo:6,7', 'Peso atómico:186.207(1)'],
          'Os': ['Osmio', 'Num Atómico : 76', 'Periodo,Grupo:6,8', 'Peso atómico:190.23(3)^2'],
          'Ir': ['Iridio', 'Num Atómico : 77', 'Periodo,Grupo:6,9', 'Peso atómico:192.217(3)'],
          'Pt': ['Platino', 'Num Atómico : 78', 'Periodo,Grupo:6,10', 'Peso atómico:195.084(9)'],
          'Au': ['Oro', 'Num Atómico : 79', 'Periodo,Grupo:6,11', 'Peso atómico:196.966569(4)'],
          'Hg': ['Mercurio', 'Num Atómico : 80', 'Periodo,Grupo:6,12', 'Peso atómico:200.59(2)'],
          'Pb': ['Plomo', 'Num Atómico : 82', 'Periodo,Grupo:6,14', 'Peso atómico:207.2(1)^2^4'],
          'Bi': ['Bismuto', 'Num Atómico : 83', 'Periodo,Grupo:6,15', 'Peso atómico:208.98040(1)'],
          'Po': ['Polonio', 'Num Atómico : 84', 'Periodo,Grupo:6,16', 'Peso atómico:[208.9824]^6'],
          'At': ['Astato', 'Num Atómico : 85', 'Periodo,Grupo:6,17', 'Peso atómico:[209.9871]^6'],
          'Rn': ['Radón', 'Num Atómico : 86', 'Periodo,Grupo:6,18', 'Peso atómico:[222.0176]6'],
          'Fr': ['Francio', 'Num Atómico : 87', 'Periodo,Grupo:7,1', 'Peso atómico:[223.0197]^6'],
          'Ra': ['Radio', 'Num Atómico : 88', 'Periodo,Grupo:7,2', 'Peso atómico:[226.0254]^6'],
          'Ac': ['Actínidos', 'Num Atómico : 89', 'Periodo:7', 'Peso atómico:[227.0278]^6'],
          'Th': ['Torio', 'Num Atómico : 90', 'Periodo:7', 'Peso atómico:232.03806(2)^6^2'],
          'Pa': ['Praseodimio', 'Num Atómico : 91', 'Periodo:7', 'Peso atómico:231.03588(2)^6'],
          'U': ['Uranio', 'Num Atómico : 92', 'Periodo:7', 'Peso atómico;238.02891(3)^6^3^2'],
          'Np': ['Neptunio', 'Num Atómico : 93', 'Periodo:7', 'Pesoa atómico:[237.0482]^6'],
          'Pu': ['Plutonio', 'Num Atómico : 94', 'Periodo:7', 'Peso atómico:[244.0642]^6'],
          'Am': ['Americio', 'Num Atómico : 95', 'Periodo:7', 'Peso atómico:[243.0614]^6'],
          'Cm': ['Curio', 'Num Atómico : 96', 'Periodo:7', 'Peso atómico:[247.0703]^6'],
          'Bk': ['Berkelio', 'Num Atómico : 97', 'Periodo:7', 'Peso atómico:[247.0703]^6'],
          'Cf': ['Californio', 'Num Atómico : 98', 'Periodo:7', 'Peso atómico:[251.0796]^6'],
          'Es': ['Einsteinio', 'Num Atómico : 99', 'Periodo:7', 'Peso atómico:[252.0829]^6'],
          'Fm': ['Fermio', 'Num Atómico : 100', 'Periodo:7', 'Peso atómico:[257.0951]^6'],
          'Md': ['Mendelevio', 'Num Atómico : 101', 'Periodo:7', 'Peso atómico:[258.0986]^6'],
          'No': ['Nobelio', 'Num Atómico : 102', 'Periodo:7', 'Peso atómico:[259.1009]^6'],
          'Lr': ['Lawrencio', 'Num Atómico : 103', 'Periodo,Grupo:7,3', 'Peso atómico:[260.1053]^6'],
          'Rf': ['Rutherfordido', 'Num Atómico : 104', 'Periodo,Grupo:7,4', 'Peso atómico:[261.1087]^6'],
          'Db': ['Dubnio', 'Num Atómico : 105', 'Periodo,Grupo:7,5', 'Peso atómico:[262.1138]^6'],
          'Sg': ['Seaborgio', 'Num Atómico : 106', 'Periodo,Grupo:7,6', 'Peso atómico:[263.1182]^6'],
          'Bh': ['Bohrio', 'Num Atómico : 107', 'Periodo,Grupo:7,7', 'Peso atómico:[262.1229]^6'],
          'Hs': ['Hassio', 'Num Atómico : 108', 'Periodo,Grupo:7,8', 'Peso atómico:[265]^6'],
          'Mt': ['Meitnerio', 'Num Atómico : 109', 'Periodo,Grupo:7,9', 'Peso atómico:[266]^6'],
          'Ds': ['Darmstadtio', 'Num Atómico : 110', 'Periodo,Grupo:7,10', 'Peso atómico:[269]^6'],
          'Rg': ['Roentgenio', 'Num Atómico : 111', 'Periodo,Grupo:7,11', 'Peso atómico:[272]^6'],
          'Cn': ['Copernicio', 'Num Atómico : 112', 'Periodo,Grupo:7,12', 'Peso atómico:[285]^6'],
          'Uut': ['Ununtrio', 'Num Atómico : 113', 'Periodo,Grupo:7,13', 'Peso atómico:[284]^6'],
          'Fl': ['Flerovio', 'Num Atómico : 114', 'Periodo,Grupo:7,14', 'Peso atómico:[289]^6'],
          'Uup': ['Ununpentio', 'Num Atómico : 115', 'Periodo,Grupo:7,15', 'Peso atómico:[288]^6'],
          'Lv': ['Livermorio', 'Num Atómico : 116', 'Periodo,Grupo:7,16', 'Peso atómico:[290]^6'],
          'Uus': ['Ununseptio', 'Num Atómico : 117', 'Periodo,Grupo:7,17', 'Peso atómico:[266]^6'],
          'Uuo': ['Ununoctio', 'Num Atómico : 118', 'Periodo,Grupo:7,18', 'Peso atómico:[294]^6']}

"""Este es la presentación de mi programa aquí le digo al usuario lo que puede hacer con este y le pido que ingrese 
un número que funcionara como la llave o input de las diferentes funciones que mi programa puede hacer incluyendo una 
opción de salida """


def menu():
    print("\n")
    print("Hola Bienvenido a Chimie un programa que te ayudara en Química")
    print("Este programa cuenta con cuatro opciónes : ")
    print("La primera es obtener datos sobre el elemento que deseas")
    print(
        "La Segunda es sacar los datos necesarios para que puedas hacer tu estructura de Lewis en compuestos")
    print("La Tercera es visualizar los elementos por sus categorías")
    print("La Cuarta es un juego que te pondra a prueba al preguntarte el número atómico de un elemento")
    print("\n")
    print(
        "Si deseas la opción uno ingresa 1, en caso de querer la segunda ingresa 2, en caso de querer la tercera "
        "ingresa 3 y si desea jugar el juego ingresa 4")

    print("En caso de querer salir, ingresa 5 ")
    print("\n")


"""Esta función se activa en el momento en el que el usuario ingresa "1" en la introducción al programa(choice=1).Con 
esta función llamamos al diccionario. Lo primero que hace esta función es imprimir la lista completa de elementos que 
puede llamar el usuario para obtener su información. Despues pide al usuario que ingrese uno de estos elementos que 
sera buscado y llamado en el diccionario para que así con la función "mydict[y el elemento que ingreso el usuario]" 
imprima la información que hay sobre este disponible.Después da la opción de buscar otro elemento o volver a la 
introducción del programa.
 
 En esta función usé el El método shuffle () que toma una secuencia, como una lista, y reorganiza el orden de los 
 elementos. W3Schools. (s.f). Python Random shuffle() Method. 13/10/2021, de W3Schools Sitio web: 
 https://www.w3schools.com/python/ref_random_shuffle.asp """


def juego():
    from random import shuffle
    ele = list(mydict.keys())
    shuffle(ele)
    print('Adivina el número atómico del elemento ', ele[-1])
    res = int(input('Introduzca su respuesta : '))
    if str(res) in mydict[ele[-1]][1]:
        print('La Respuesta es correcta !')
    else:
        print('La Respuesta es incorrecta !')
        print('La Respuesta correcta es ', mydict[ele[-1]][1][-3:])


'''Esta función se manda a llamar cuando el usuario escoge la opción 5 Esta función utiliza la función shuffle de la 
librería random para revolver los elementos de una lista, la cual contiene los elementos de la tabla periódica, 
para posteriormente cuestionar al usuario acerca del número atómico del último elemento de la lista. Debido a que 
cada vez que se manda llamar la función la lista es revuelta, el último elemento de la lista cambiará constantemente. 
De igual manera se utilizaron cadenas de strings para la verificación del resultado al igual que para la impresión de 
la respuesta correcta. '''


def dicti():
    check = True
    while check:
        print("Tenemos todos estos elementos disponibles", list(mydict.keys()))
        elemento = input("Ingresa el simbolo del elemento que quieres analizar: ")

        if elemento in list(mydict.keys()):
            print("\n")
            print(mydict[elemento])
            print("\n")
            seguir = input("Si desea buscar otro elemento escriba Si.\n De lo contario presione cualquier tecla: ")

            if seguir == "Si":
                check = True

            else:
                check = False
        else:
            print("No existe ese elemento")


"""Esta función se activa en el momento en el que el usuario ingresa "3" en la introducción al programa(choice=3).Con 
esta función llamamos a una matriz que tiene como próposito imprimir los elementos que sean: metales, gases nobles, 
metaloides, y no metales.Al usuario se le pregunta que categoria quiere saber y en base a esta respuesta/input se 
imprimen los datos dentro de ese elemento de la matriz/ la lista anidada. """


def elementos():
    metales = ['Li', 'Be', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Se', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
               'Cu', 'Zn', 'Ga', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc',
               'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Cs', 'Ba', 'La',
               'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
               'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Pb', 'Bi',
               'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
               'Md', 'No', 'Lr']

    gases_nobles = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']

    metaloides = ['B', 'Si', 'Ge', 'As', 'Sb', 'Te', 'Po', 'At']

    no_metales = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl', 'Se', 'Br', 'I']

    matriz = [metales, gases_nobles, no_metales, metaloides]

    print(
        "Si quieres saber que elementos son Metales ingresa 1\nPara saber que elementos son Gases Nobles ingresa "
        "2\nPara saber que elementos son No Metales ingresa 3\nY para saber que elementos son Metaloides ingresa 4")
    choice = input()
    if choice == "1":
        for elem in matriz[0]:
            print(elem)
    elif choice == "2":
        for elem in matriz[1]:
            print(elem)
    elif choice == "3":
        for elem in matriz[2]:
            print(elem)

    elif choice == "4":
        for elem in matriz[3]:
            print(elem)
    else:
        print("Opción no encontrada")
        elementos()


"""Esta función se activa en el momento en el que el usuario ingresa "2" en la introducción al programa(choice=2).Con 
esta función llamamos a la función que se va a encargar de calcular el numero de enlaces y el número de electornes no 
compartidos que facilitara el dibujo del esquema de lewis de este compuesto al usuario. . """


def lewis(v, r):
    numero_de_enlaces = (r - v) / 2
    electrones_no_compartidos = v - (2 * numero_de_enlaces)
    if numero_de_enlaces < 0:
        print("No se puede resolver ya que es una excepción")
    elif numero_de_enlaces > 0:
        print("\n")
        print("El primer valor son los enlaces y el segundo los electrones no compartidos")
        return numero_de_enlaces, electrones_no_compartidos


"""Esta es la función más importante, ya que recibe la opción/choice que el usuario ingreso en la introducción del 
programa dependiendo de lo que quiera hacer con este y en base a este llama a la función que se va a encargar de 
generar y correr el  respectivo programa y hacerlo funcionar.Si se ingresa una opción que no esta disponible, se le
 avisa al usuarioy también hay una opción para salir y terminar el programa.
 Al ingresar la opción dos pide dos parametros o datos iniciales que al llamar la función serán usados para 
 calcular los resultados con términos químicos. """


def chimie():
    while True:
        menu()
        opcion = (input("Ingrese una Opción: "))
        print('\n')

        if opcion == "1":
            dicti()

        elif opcion == "2":
            v = int(input('Por favor ingresa la suma de electrones de valencia por cada átomo en tu compuesto : '))
            r = int(input(
                'Por favor ingresa la suma de electrones requeridos por cada átomo en tu compuesto para conseguir su '
                'octeto : '))
            respuesta = lewis(v, r)
            print(respuesta)
        elif opcion == "3":
            elementos()
        elif opcion == "4":
            juego()
        elif opcion == "5":
            print("Gracias por usar este programa")
            break

        else:
            print('Esta opción no esta disponible')


chimie()
