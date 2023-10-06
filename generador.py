import random
import os
try:
    from PIL import Image
except:
    print('Pillow no encontrado, asegurate de haberlo instalado siguiendo las instrucciones del readme\n\
Cerrando programa')
    quit()
    
"""
Generador de imagenes chistosas
El programa final elige 2 de distintas carpetas para compararlas o juntarlas
Las imagenes son de 2 tipos: sources y plantillas o templates. La principal difrencia
es que las sources estan pensadas para ser colocadas en las plantillas, por lo que las
plantillas incluyen mas datos entre los que estan el numero de sources que admiten

Esta version del programa permite al usuario elegir cuantas imagenes se generarán y de que
manera se generarán, guardando la imagen final en el folder en el cual se encuentra este script
El avance de matrices ya estaba listo, pues las clases de imagenes toman tuplas de tuplas
Esta version no usa OS para evitar problemas
"""

SOURCE_DIR = 'sources'
TEMP_DIR = 'templates'
n_of_src = 0
n_of_temp = 0

#source image: para guardar los datos, incluyendo tamaño y etiquetas, de una imagen
class source_image:
    #funcion al crear nuevo objeto,
    #toma el nombre de imagen y una etiqueta, abre la imagen a partir del nombre
    def __init__(self, image: str, tags: list):
        self.image = image
        self.tags = tags
        try:
            self.img = Image.open(image)
        except:
            print('No se encontro la imagen ', image, 'Asegurate de que este en el mismo folder que el script')
            quit()
        global n_of_src
        n_of_src +=1
    
        
#Plantilla: para guardar los datos, incluyendo etiquetas y numero de sources aceptadas
class template:
    #funcion al crear nuevo objeto (plantilla),
    #Toma el nombre de imagen. tamaño en pixeles del espacio para la source, coordenadas para dicho espacio,
    #una etiqueta y el numero de sources que puede contener la imagen
    def __init__(self, image: str, size: tuple, coor: tuple,  tag: tuple, source_capacity: int):
        self.image = image
        every = [size, coor, tag]
        for i in every:
            if len(i) != source_capacity:
                raise Exception("Amount of iterates in tuples must be equal to source capacity ", i, len(i))
            
        self.source_capacity = int(source_capacity)
        self.slot = []
        for i in range(self.source_capacity):
            self.slot.append(place(size[i], coor[i], tag[i]))

        try:
            self.img = Image.open(image)
        except:
            print('No se encontro la imagen ', image, 'Asegurate de que este en el mismo folder que el script')
            quit()
        global n_of_temp
        n_of_temp +=1

class place:
    def __init__(self, size: tuple, coor: tuple, tag: str):
        self.size = size
        self.coor = coor
        self.tag = tag


#intentar combinar un ejemplo de plantilla y un ejemplo de source, regresa la imagen final
def combine(srcs: list, temp:template):
    final =  temp.img
    i = 0
    for slotn in temp.slot:
        diference = (slotn.size[0] != srcs[i].img.size[0] and slotn.size[1] != srcs[i].img.size[1])
        if(diference):
            new_size = slotn.size
            resize = srcs[i].img.resize(slotn.size)
            final.paste(resize, slotn.coor)
            print("Redimension necesaria. El tamaño de la source image ahora es", new_size)
        
        else:
            print("No hubo necesidad de redimension")
            final.paste(srcs[i].img, slotn.coor)
        i +=1

    print("Imagenes combiadas:")
    print("Plantilla: ", temp.image)
    print("Source: ")
    for x in srcs:
        print(x.image)
    return final

#Comprueba 
def are_tags_same(src:source_image, slot:place):
    for x in src.tags:
        if x == slot.tag:
            return True
    return False
    
#Toma 2 numeros y regresa la plantilla y SI referentes a dichos numeros
def get_src_temp(src_num, tmp_num):
    if src_num == 0:
        s_img = SRC0
    elif src_num == 1:
        s_img = SRC1
    elif src_num == 2:
        s_img = SRC2
    elif src_num == 3:
        s_img =  SRC3
    elif src_num == 4:
        s_img = SRC4
    elif src_num == 5:
        s_img = SRC5
    else:
        raise TypeError("Number given exceeds the number of Source Images or is less than 0")
           
    if tmp_num == 0:
        temp = TMP0
    elif tmp_num == 1:
        temp = TMP1
    elif tmp_num == 2:
        temp = TMP2
    elif tmp_num == 3:
        temp = TMP3
    elif tmp_num == 4:
        temp = TMP4
    elif tmp_num == 5:
        temp = TMP5
    else:
        raise TypeError("Number given exceeds the number of Source Images or is less than 0")
    
    return s_img, temp

def try_again(slot:place):
    possible = False
    while not possible:
        print("Etiquetas no coinciden, volviendo a intentar")
        RNG = random.randrange(0, n_of_src)
        src_img, x = get_src_temp(RNG, 0)
        del x
        possible = are_tags_same(src_img, slot)
    if possible:
        return src_img

#Para imagenes aleatorias
def random_image():
    RNG = random.randrange(0, n_of_src)
    RNG2 = random.randrange(0, n_of_temp)
    s_img, temp = get_src_temp(RNG, RNG2)
    sources = [s_img]
    if temp.source_capacity == 1:
        return combine(sources, temp)
    else:
        for x in range(len(temp.slot)-1):
            RNG = random.randrange(0, n_of_src)
            s_img, t = get_src_temp(RNG, RNG2)
            del t
            sources.append(s_img)
        return combine(sources, temp)
    
        
    
#Para etiquetas
def tags():
    RNG = random.randrange(0, n_of_src)
    RNG2 = random.randrange(0, n_of_temp)
    src_img, tmp = get_src_temp(RNG, 5)
    sources = [src_img]
    possible = False

    if tmp.source_capacity == 1:
        possible = are_tags_same(src_img, tmp.slot[0])
        if not possible:
            src_img = try_again(tmp.slot[0])
            sources[0] = src_img
            possible = True

    else:
        sources = list(range(tmp.source_capacity))
        for x in range(len(tmp.slot)):
            RNG = random.randrange(0, n_of_src)
            possible = are_tags_same(src_img, tmp.slot[x])
            if possible:
                sources[x] = src_img
            else:
                src_img = try_again(tmp.slot[x])
                sources[x] = src_img
            
            src_img, t = get_src_temp(RNG, RNG2)
            del t
        possible=True

    if possible:
        return combine(sources, tmp)
    

#Para eleccion manual de imagenes
def manual():
    print("Has escogido la seleccion manual de imagenes \n Actualmente hay ", n_of_src, " source images y ", n_of_temp, " plantillas")
    print("Cada imagen tiene un numero asignado, en plantillas estas van de 0 a ", (n_of_temp -1), ". Ingresa un numero para\
 seleccionar la plantilla")
    select = int(input())

    if select >= n_of_src:
        print("Numero de platilla no valida")
        return
    
    x, tmp = get_src_temp(0, select)
    del x
    print("Tu plantilla seleccionada tiene de nombre "+  tmp.image)

    print ("La plantilla seleccionada tiene espacio para ", tmp.source_capacity, "sources, por lo que deberas seleccionar ", tmp.source_capacity)
    sources = []
    for x in range(tmp.source_capacity):
        print("Cada source tambien tiene su numero, del 0 al ", (n_of_src -1), ". Selecciona una mediante este numero")
        select = int(input())

        if select >= n_of_src:
            print("Numero de Source Image no valido")
            return
    
        src, x = get_src_temp(select, 0)
        del x
        sources.append(src)
        print("Tu imagen tiene de nombre " + src.image)

    select = int(input("Deseas continuar con la combinacion de estas imagenes? Si - 1, No - 0"))
    if select == 1:
        return combine(sources, tmp)
    else:
        return

#definicion de cada imagen
SRC0 = source_image("SOURCE(0).png", ["anime", "desamparo", "cara"])
SRC1 = source_image("SOURCE(001).png", ["animal", "ser", "cara"])
SRC2 = source_image("SOURCE(002).png", ["ser", "sinsentido"])
SRC3 = source_image("SOURCE(003).png", ["feliz", "ser"])
SRC4 = source_image("SOURCE(004).PNG", ["agresivo", "ser", "cara"])
SRC5 = source_image("SOURCE(005).png", ["molesto", "sinsentido", "cara"])
TMP0 = template("TEMP(0).png", ((300, 300),), ((315, 180),), ("ser",), 1)
TMP1 = template("TEMP(001).PNG", ((1080, 526),), ((0, 134),), ("ser",), 1)
TMP2 = template("TEMP(002).png", ((1080, 815),), ((0, 168),), ("sinsentido",), 1)
TMP3 = template("TEMP(003).png", ((691, 495),), ((0, 99),), ("agresivo",), 1)
TMP4 = template("TEMP(004).png", ((187, 125),), ((69, 152),), ("ser",), 1)
TMP5 = template("TEMP(005).png", ((100, 115), (76, 92), (68, 80), (72, 85), (74, 91)), ((192, 0), (110, 25), (22, 42), (304, 43), (419, 54)), 
("cara", "cara", "cara", "cara", "cara"), 5)

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
            name = str("new image("+ str(i) + ").png")
            f.save(name)
            done = True
        elif inp == 2:
            f = tags()
            name = str("new image("+ str(i) + ").png")
            f.save(name)
            done = True
        elif inp == 3:
            f = manual()
            if f != None:
                name = str("new image("+ str(i) + ").png")
                f.save(name)
            done = True
        else:
            print("Tu respuesta no esta incluida en la lista de posibles respuestas, recuerda que solo acepta\
 numeros del 1 al 3. Terminando programa")
     
    i +=1
