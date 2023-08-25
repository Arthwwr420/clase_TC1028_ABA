"""
Generador de imagenes chistosas
El programa final elige 2 de distintas carpetas para compararlas o juntarlas
Las imagenes son de 2 tipos: sources y plantillas o templates. La principal difrencia
es que las sources estan pensadas para ser colocadas en las plantillas, por lo que las
plantillas incluyen mas datos entre los que estan el numero de sources que admiten

Esta version del programa tomara 2 "imagenes" (en realidad representaciones de las mismas,
guardadas en clases) y verificará si son compatibles basandose en las etiquetas, además de
redimensionar la source en caso de ser necesario
"""
#source image: para guardar los datos, incluyendo tamaño y etiquetas, de una imagen
class source_image:
    #funcion al crear nuevo objeto,
    #toma el nombre de imagen, tamaño en pixeles y una etiqueta
    def __init__(self, image, size, tag):
        self.image = image
        self.size = size
        self.tag = tag
        
#Plantilla: para guardar los datos, incluyendo etiquetas y numero de sources aceptadas
class template:
    #funcion al crear nuevo objeto (plantilla),
    #Toma el nombre de imagen. tamaño en pixeles del espacio para la source, una etiqueta y
    #el numero de sources que puede contener la imagen
    def __init__(self, image, size, tag, source_capacity):
        self.image = image
        self.size = size
        self.tag = tag
        self.source_capacity = int(source_capacity)
        
temp_ex1 = template("ejemplo plantilla.png", 512, "etiqueta 1", 1)
temp_ex2 = template("ejemplo plantilla2.png", 1024, "etiqueta 2", 1)
src_ex1 = source_image("ejemplo.png", 256, "etiqueta 1")
src_ex2 = source_image("ejemplo2.png", 1024, "etiqueta 2")
src_ex3 = source_image("ejemplo3.png", 1024, "etiqueta 1")

#Para esta demostracion, para que se puedan combinar las imagenes deben de tener el mismo tag

#intentar combinar un ejemplo de plantilla y un ejemplo de source
def combine(src, temp):
    if(temp.tag == src.tag):
        print("Combinacion posible")
        diference = temp.size - src.size
        if(diference > 0):
            percent = (diference*100)/src_ex1.size
            new_size = temp.size
            print("Redimension necesaria. El tamaño de la source image ahora es", new_size,", aumento un %", percent)
        elif(diference < 0):
            percent = (-diference*100)/src_ex1.size
            new_size = temp.size
            print("Redimension necesaria. El tamaño de la source image ahora es", new_size,", disminuyo un %", percent)
        else:
            print("No hubo necesidad de redimension")
    else:
        print("Combinacion no posible, etiquetas distintas")
            
combine(src_ex1, temp_ex1)
combine(src_ex2, temp_ex1)
combine(src_ex3, temp_ex1)
combine(src_ex2, temp_ex2)
