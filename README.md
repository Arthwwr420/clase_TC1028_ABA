# Generador de imagenes chistosas
## Contexto

La comedia en los ultimos a�os ha sido sumamente influenciada por imagenes chistosas en el internet, o memes, eventualmente llegando a la creacion de paginas dedicadas a estos.  Un usuario, conocido como JECR147, decidio hacer algo un tanto m�s, distinto. Desarroll� un algoritmo capaz de combinar plantillas y source images, generando asi memes de manera completamente para subir a redes sociales. A este proyecto se le conoce como Momosbot4000, con cuentas en redes sociales como Twitter en las cuales publica estos memes de manera periodica.

Sin embargo, debido a la completa aleatoriedad al momento de generar las imagenes, el resultado termina siendo muy inconsistente, habiendo imagenes que simplemente funcionan mejores que otras. A partir de esto, surge este proyecto, que busca crear un programa similar pero que pueda generar imagenes m�s congruentes, pero sin perder por completo la aleatoriedad.

Este programa tiene como objetivo editar imagenes, o plantillas, a�adiendo texto u otras imagenes con fines comedicos, aunque sin estar limitado a estos, de manera aleatoria. Selecciona una imagen base o plantilla de manera aleatoria, la cual despu�s modificara a�adiendo otras imagenes (las cuales varian en numero segun la plantilla elegida), las cuales tambien ser�n elegidas de manera procedural, siguiendo parametros dados por etiquetas para que la imagen divertida resultado del producto de estas tenga mas sentido. Estas etiquetas seran la base para el programa, pues permitiran al usuario decidir si se desea una imagen completamente aleatoria, sin sentido, o una mas convencional haciendo que las etiquetas de las imagenes combinadas coincidan.

### Intrucciones
Descarga el archivo generador.py junto a las imagenes, el script esas imagenes mediante sus nombres asi que no los cambies. No es necesario descargar las carpetas ahora, lo importate es que las imagenes esten sueltas en el mismo directorio que el generador. El script y las imagenes deben de estar en el mismo folder. 
El script usa Pillow, por lo que debe de ser instalado primero, afortunadamente, Pillow esta incluido en los paquetes de PIP, que a su vez viene incluido en la instalacion de python. Puedes instalarlo con este comando:

	python -m pip install --upgrade Pillow

Si Pillow ya esta instalado, deberia regresar un mensaje similar al siguiente:

	Requirement already satisfied: Pillow in c:\users\Nombre\appdata\roaming\python\python311\site-packages (10.0.0)

Si eso no funciona, puedes consultar la pagina web de la instalaci�n: https://pillow.readthedocs.io/en/latest/installation.html
Una vez instalado todo, correr con el siguiente comando:

	python generador.py

Sigue las instrucciones dadas por el programa
Las imagenes finales ser� guardada en el folder en el que se encuentren el script y las carpetas de imagenes, por lo que recomiendo que estos se guarden en una carpeta aparte para que la imagen no se pierda entre los archivos o  se instale directamente el ZIP. La imagen generada ser� de nombre "new image(numero de la imagen).png".

#### Nota: Se generara el numero de imagenes que se desee, pero al volver a correr el archivo las imagenes generadas ser�n sobreescritas con las nuevas4
En esta version se incluye generadorSOS, en caso de que no funcione generador.py por problemas con Pillow, este archivo esta ahi para que se use sin usar esta librer�a.

### Avance:
En este avance se incorpora el generador SOS, ademas de acomodarse a las normas PEP8

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

