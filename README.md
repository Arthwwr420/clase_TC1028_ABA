# Generador de imagenes chistosas
## Contexto

La comedia en los ultimos años ha sido sumamente influenciada por imagenes chistosas en el internet, o memes, eventualmente llegando a la creacion de paginas dedicadas a estos.  Un usuario, conocido como JECR147, decidio hacer algo un tanto más, distinto. Desarrolló un algoritmo capaz de combinar plantillas y source images, generando asi memes de manera completamente para subir a redes sociales. A este proyecto se le conoce como Momosbot4000, con cuentas en redes sociales como Twitter en las cuales publica estos memes de manera periodica.

Sin embargo, debido a la completa aleatoriedad al momento de generar las imagenes, el resultado termina siendo muy inconsistente, habiendo imagenes que simplemente funcionan mejores que otras. A partir de esto, surge este proyecto, que busca crear un programa similar pero que pueda generar imagenes más congruentes, pero sin perder por completo la aleatoriedad.

Este programa tiene como objetivo editar imagenes, o plantillas, añadiendo texto u otras imagenes con fines comedicos, aunque sin estar limitado a estos, de manera aleatoria. Selecciona una imagen base o plantilla de manera aleatoria, la cual después modificara añadiendo otras imagenes (las cuales varian en numero segun la plantilla elegida), las cuales tambien serán elegidas de manera procedural, siguiendo parametros dados por etiquetas para que la imagen divertida resultado del producto de estas tenga mas sentido. Estas etiquetas seran la base para el programa, pues permitiran al usuario decidir si se desea una imagen completamente aleatoria, sin sentido, o una mas convencional haciendo que las etiquetas de las imagenes combinadas coincidan.

## Algoritmo
El funcionamiento base del programa se basaria en lo siguiente

E0()
1. Seleccionar una plantilla de manera aleatoria
2. Checar el numero de espacios para imagenes secundarias que se pueden agregar en la plantilla y guardarlo en una variable
3. Por cada espacio para imagen secundaria
	3.1. Seleccionar una imagen secundaria
	3.2. Si la etiqueta de la plantilla coincide con la de la imagen secundaria seleccionada
		Guardar la imagen secundaria en una lista
   	si no
		Volver al paso 3.1
4. Por cada imagen secundaria
	4.1. Conseguir las coordenadas del espacio para la imagen secundaria en la plantilla
	4.2. Editar la plantilla para que quede colocada sobre dicha coordenada
5. Guardar imagen final
EF(imagen_final)
