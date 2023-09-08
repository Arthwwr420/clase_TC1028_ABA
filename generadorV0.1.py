import random
"""
Generador de imagenes chistosas
El programa final elige 2 de distintas carpetas para compararlas o juntarlas
Las imagenes son de 2 tipos: sources y plantillas o templates. La principal difrencia
es que las sources estan pensadas para ser colocadas en las plantillas, por lo que las
plantillas incluyen mas datos entre los que estan el numero de sources que admiten

Esta version del programa tomara 2 imagenes y verificará si son compatibles basandose en
las etiquetas, para luego llamar una funcion que regresa la combinacion de ambas imagenes,
la cual se guardara en el folder en el cual se encuentra el script
"""


#source image: para guardar los datos, incluyendo tamaño y etiquetas, de una imagen
class source_image:
    #funcion al crear nuevo objeto,
    #toma el nombre de imagen y una etiqueta, abre la imagen a partir del nombre
    def __init__(self, image: str, tag: str, tag2: str):
        self.image = image
        self.tag = tag
        self.tag2 = tag2
        self.img = None
    
    
        
#Plantilla: para guardar los datos, incluyendo etiquetas y numero de sources aceptadas
class template:
    #funcion al crear nuevo objeto (plantilla),
    #Toma el nombre de imagen. tamaño en pixeles del espacio para la source, coordenadas para dicho espacio,
    #una etiqueta y el numero de sources que puede contener la imagen
    def __init__(self, image: str, size: tuple, coor: tuple,  tag: str, source_capacity: int):
        self.image = image
        self.size = size
        self.tag = tag
        self.coor = coor
        self.source_capacity = int(source_capacity)
        self.img = None

n_of_src = 2
n_of_temp = 2

#intentar combinar un ejemplo de plantilla y un ejemplo de source, regresa la imagen final
def combine(src:source_image, temp:template):
    diference = temp.size
    if(diference != 0):
        new_size = temp.size
        print("Redimension necesaria. El tamaño de la source image ahora es", new_size)
        
    else:
        print("No hubo necesidad de redimension")
    print("Imagenes combiadas:")
    print("Plantilla: ", temp.image)
    print("Source: ", src.image)

#Comprueba 
def are_tags_same(src:source_image, temp:template):
    if src.tag == temp.tag or src.tag2 == temp.tag:
        return True
    else:
        return False
    
#Toma 2 numeros y regresa la plantilla y SI referentes a dichos numeros
def get_src_temp(src_num, tmp_num):
    match src_num:
        case 0:
            s_img = SRC0
        case 1:
            s_img = SRC1
        case _:
            raise TypeError("Number given exceeds the number of Source Images or is less than 0")
        
    match tmp_num:
        case 0:
            temp = TMP0
        case 1:
            temp = TMP1
        case _:
            raise TypeError("Number given exceeds the number of Source Images or is less than 0")
    return s_img, temp


#Para imagenes aleatorias
def random_image():
    RNG = random.randrange(0, n_of_src)
    RNG2 = random.randrange(0, n_of_src)
    s_img, temp = get_src_temp(RNG, RNG2)
    
    combine(s_img, temp)
    
#Para etiquetas
def tags():
    RNG = random.randrange(0, n_of_src)
    RNG2 = random.randrange(0, n_of_src)
    src_img, tmp = get_src_temp(RNG, RNG2)
    possible = are_tags_same(src_img, tmp)

    while not possible:
        if(tmp.tag == src_img.tag) or (tmp.tag == src_img.tag2):
            combine(src_img, tmp)
            possible = True
            break
        
        else:
            RNG = random.randrange(0, 2)
            src_img, x = get_src_temp(RNG, 0)
            print("Etiquetas no coinciden, volviendo a intentar")

#Para eleccion manual de imagenes
def manual():
    print("Has escogido la seleccion manual de imagenes \n Actualmente hay ", n_of_src, " source images y ", n_of_temp, " plantillas")
    print("Cada imagen tiene un numero asignado, en sources estas van de 0 a ", (n_of_src -1), ". Ingresa un numero para\
 seleccionar la source")
    select = int(input())

    if select >= n_of_src:
        print("Numero de Source Image no valido")
        return
    
    src, x = get_src_temp(select, 0)
    del x
    print("Tu imagen tiene de nombre " + src.image)

    print("Cada plantilla tambien tiene su numero, del 0 al ", (n_of_temp -1), ". Selecciona una mediante este numero")
    select = int(input())

    if select >= n_of_src:
        print("Numero de platilla no valida")
        return
    
    x, tmp = get_src_temp(0, select)
    del x
    print("Tu plantilla seleccionada tiene de nombre "+  tmp.image)

    select = int(input("Deseas continuar con la combinacion de estas imagenes? Si - 1, No - 0"))
    if select == 1:
        combine(src, tmp)
    else:
        return

SRC0 = source_image("SOURCE(0).png", "anime", "desamparo")
SRC1 = source_image("SOURCE(001).png", "animal", "ser")
TMP0 = template("TEMP(0).png", (300, 300), (315, 180), "ser", 1)
TMP1 = template("TEMP(001).PNG", (1079, 526), (0, 134), "ser", 1)

print("Generador de imagenes V0.1: Aun no funcional")
print("Bienvenido al generador de imagenes chistosas, debido a... problemas... esta sera una simulacion, por lo que no se usaran imagenes")
print(" Selecciona el tipo de generacion que deseas: \n Aleatoria - 1  Aleatoria Basada en etiquetas - 2  Manual - 3")

inp = int(input())
if inp == 1:
    random_image()
elif inp == 2:
    tags()
elif inp == 3:
    manual()
else:
    print("Tu respuesta no esta incluida en la lista de posibles respuestas, recuerda que solo acepta\
 numeros del 1 al 3. Terminando programa")

