from PIL import Image
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

SOURCE_FOLDER = "sources\\"
TEMP_FOLDER = "templates\\"

#source image: para guardar los datos, incluyendo tamaño y etiquetas, de una imagen
class source_image:
    #funcion al crear nuevo objeto,
    #toma el nombre de imagen y una etiqueta, abre la imagen a partir del nombre
    def __init__(self, image, tag):
        self.image = image
        self.tag = tag
        self.img = Image.open(SOURCE_FOLDER + image)
    
    
        
#Plantilla: para guardar los datos, incluyendo etiquetas y numero de sources aceptadas
class template:
    #funcion al crear nuevo objeto (plantilla),
    #Toma el nombre de imagen. tamaño en pixeles del espacio para la source, coordenadas para dicho espacio,
    #una etiqueta y el numero de sources que puede contener la imagen
    def __init__(self, image, size, coor,  tag, source_capacity):
        self.image = image
        self.size = size
        self.tag = tag
        self.coor = coor
        self.source_capacity = int(source_capacity)
        self.img = Image.open(TEMP_FOLDER + image)
        

#intentar combinar un ejemplo de plantilla y un ejemplo de source, regresa la imagen final
def combine(src:source_image, temp:template):

    if(temp.tag == src.tag):
        print("Combinacion posible")
        diference = temp.size[0]*temp.size[1] - src.img.size[0]*src.img.size[1]

        if(diference != 0):
            new_size = temp.size
            print("Redimension necesaria. El tamaño de la source image ahora es", new_size)
            resize = src.img.resize(temp.size)
            final = temp.img
            final.paste(resize, temp.coor)
            return final
        
        else:
            print("No hubo necesidad de redimension")
            final = temp.img
            final.paste(src.img, temp.coor)
            return final
    else:
        print("Combinacion no posible, etiquetas distintas")
            
SRC1 = source_image("SOURCE(0).png", "1")
TMP1 = template("TEMP(0).png", (300, 300), (315, 180), "1", 1)

final_image = combine(SRC1, TMP1)
final_image.save("newimage.png") #guarda la imagen final

