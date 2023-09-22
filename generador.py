import random
import os
from PIL import Image
"""
Generador de imagenes chistosas
El programa final elige 2 de distintas carpetas para compararlas o juntarlas
Las imagenes son de 2 tipos: sources y plantillas o templates. La principal difrencia
es que las sources estan pensadas para ser colocadas en las plantillas, por lo que las
plantillas incluyen mas datos entre los que estan el numero de sources que admiten

Esta version del programa permite al usuario elegir cuantas imagenes se generarán y de que
manera se generarán, guardando la imagen final en el folder en el cual se encuentra este script
"""

SOURCE_DIR = 'sources'
TEMP_DIR = 'templates'
n_of_src = 0
n_of_temp = 0

os.chdir(os.path.dirname(__file__))

#source image: para guardar los datos, incluyendo tamaño y etiquetas, de una imagen
class source_image:
    #funcion al crear nuevo objeto,
    #toma el nombre de imagen y una etiqueta, abre la imagen a partir del nombre
    def __init__(self, image: str, tag: str, tag2: str):
        self.image = image
        self.tag = tag
        self.tag2 = tag2
        os.chdir(SOURCE_DIR)
        self.img = Image.open(image)
        os.chdir(os.path.dirname(__file__))
        global n_of_src
        n_of_src +=1
    
        
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
        os.chdir(TEMP_DIR)
        self.img = Image.open(image)
        os.chdir(os.path.dirname(__file__))
        global n_of_temp
        n_of_temp +=1


#intentar combinar un ejemplo de plantilla y un ejemplo de source, regresa la imagen final
def combine(src:source_image, temp:template):
    diference = temp.size
    if(diference != 0):
        new_size = temp.size
        resize = src.img.resize(temp.size)
        final =  temp.img
        final.paste(resize, temp.coor)
        print("Redimension necesaria. El tamaño de la source image ahora es", new_size)
        
    else:
        print("No hubo necesidad de redimension")
        final = temp.img
        final.paste(src.img, temp.coor)

    print("Imagenes combiadas:")
    print("Plantilla: ", temp.image)
    print("Source: ", src.image)
    return final

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
        case 2:
            s_img = SRC2
        case 3:
            s_img = SRC3
        case 4:
            s_img = SRC4
        case 5:
            s_img = SRC5
        case _:
            raise TypeError("Number given exceeds the number of Source Images or is less than 0")
        
    match tmp_num:
        case 0:
            temp = TMP0
        case 1:
            temp = TMP1
        case 2:
            temp = TMP2
        case 3:
            temp = TMP3
        case 4:
            temp = TMP4
        case _:
            raise TypeError("Number given exceeds the number of Source Images or is less than 0")
    return s_img, temp


#Para imagenes aleatorias
def random_image():
    RNG = random.randrange(0, n_of_src)
    RNG2 = random.randrange(0, n_of_temp)
    s_img, temp = get_src_temp(RNG, RNG2)
    
    return combine(s_img, temp)
    
#Para etiquetas
def tags():
    RNG = random.randrange(0, n_of_src)
    RNG2 = random.randrange(0, n_of_temp)
    src_img, tmp = get_src_temp(RNG, RNG2)
    possible = are_tags_same(src_img, tmp)

    while not possible:
        if(tmp.tag == src_img.tag) or (tmp.tag == src_img.tag2):
            possible = True 
            break 
        else:
            RNG = random.randrange(0, 2)
            src_img, x = get_src_temp(RNG, 0)
            print("Etiquetas no coinciden, volviendo a intentar")

    if possible:
        return combine(src_img, tmp)
    

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
        return combine(src, tmp)
    else:
        return

#definicion de cada imagen
SRC0 = source_image("SOURCE(0).png", "anime", "desamparo")
SRC1 = source_image("SOURCE(001).png", "animal", "ser")
SRC2 = source_image("SOURCE(002).png", "ser", "sinsentido")
SRC3 = source_image("SOURCE(003).png", "feliz", "ser")
SRC4 = source_image("SOURCE(004).PNG", "agresivo", "ser")
SRC5 = source_image("SOURCE(005).png", "Molesto", "sinsentido")
TMP0 = template("TEMP(0).png", (300, 300), (315, 180), "ser", 1)
TMP1 = template("TEMP(001).PNG", (1080, 526), (0, 134), "ser", 1)
TMP2 = template("TEMP(002).png", (1080, 815), (0, 168), "sinsentido", 1)
TMP3 = template("TEMP(003).png", (691, 495), (0, 99), "agresivo", 1)
TMP4 = template("TEMP(004).png", (187, 125), (69, 152), "ser", 1)

#codigo principal
print("Generador de imagenes V0.2")
print("Bienvenido al generador de imagenes chistosas")
print("Por favor, ingresa el numero de imagenes que deseas generar")
num_of_images = int(input())
i = 0
while i < num_of_images:
    done = False
    while not done:
        print(" Selecciona el tipo de generacion que deseas: \n Aleatoria - 1  Aleatoria Basada en etiquetas - 2  Manual - 3")
        inp = int(input())
        if inp == 1:
            f = random_image()
            f.save("new image.png")
            done = True
        elif inp == 2:
            f = tags()
            f.save("new image.png")
            done = True
        elif inp == 3:
            f = manual()
            if f != None:
                f.save("new image.png")
            done = True
        else:
            print("Tu respuesta no esta incluida en la lista de posibles respuestas, recuerda que solo acepta\
 numeros del 1 al 3. Terminando programa")
     
    i +=1
