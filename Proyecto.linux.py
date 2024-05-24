#¡¡AVISO!!
#Este codigo precisa de varios paquetes de extensiónes de python, los cuales, tienes que descargar para que el codigo funcióne correctamente.
#Si no tienes ninguno de los paquetes, prueba a ejecutar los siguientes comandos en tu terminal para descargarlos.
#Paquete1 = pip install paquete1 (sustituyendo "paquete1" por el nombre de lo que quieres descargar).
#También necesitarás tener el buscador de Google Chrome instalado para que funcione.

import time
import os
from selenium import webdriver #ignorar posible error

os.system('clear')
#mensage de aviso (pre-mensage)
print ("Bienvenido a mi Proyeto!")
print ("En este codigo, podrás repasar todo el contenido que hemos dado de python en todo el curso.")
print ("Al aceptar la siguiente elección, entrarás en un bucle de While True que te repetirá un menú con opciones con las que podrás interactuar.")
print("Estás seguro que quieres iniciar el comando?")
time.sleep(6)
a = input ("s/n ")
if a == ("n"):
    print ("Adios!")
elif a == ("s"):
    os.system('clear')
    #mensage de inicio
    print ("Bien!")
    print ("Como ya bien sabrás, a lo largo del año hemos dado mucho contenido de python.")
    while True:
    #primer bucle (menú principal)
        print ("Contenido de python:")
        print ('    1 para ver "Comandos y conceptos basicos de Python"')
        print ('    2 para ver "Comandos de pygame"')
        print ('    3 para ver "Comandos de matplotlib"')
        print ('    4 para ver "Comandos de scrapy (Selenium)"')
        print ("    0 para cerrar el codigo")
        print ("")
        print ("¿Que opción te gustaria abrir? ")
        b = input ("")
#COMIENZA basicos de python
        if b == ("1"):
            while True:
                os.system('clear')
                print ("Comandos y conceptos basicos de python:")
                print ('    1 "print"')
                print ('    2 "input"')
                print ('    3 "if", "elif", "else"')
                print ('    4 "def" y creación de variables')
                print ('    5 "while"')
                print ('    6 "for"')
                print ("    7 para abrir una pagina web que te ayude a practicar estos comandos con ejercicios!")
                print ("    0 para volver al menú principal")
                print ("")
                print ("¿Que opción te gustaria abrir? ")
                c = input ("")
        #COMIENZA PRINT
                if c == ("1"):
                    os.system('clear')
                    print ('El "print" es un comando/función que hace que en el Output, aparezca lo que tu quieras.')
                    print ('Ejemplo:')
                    print ('    Input:')
                    print ('        print ("Hello World!")')
                    print ('    Output:')
                    print ('        Hello World!')
                    print ("")
                    print ("")
                    input ("Pulsa enter cuando quieras salir")
        #ACABA PRINT Y EMPIEZA INPUT
                elif c == ("2"):
                    os.system('clear')
                    print ('El "input" es un comando/función que hace que en el Output, al host, le dé la opción de añadir texto durante la ejecución')
                    print ('Ejemplo:')
                    print ('    Input:')
                    print ('        input ("Hola, ¿Como te llamas? ")')
                    print ('    Output:')
                    print ('        Hola, ¿Como te llamas? |')
                    print ('                          Aqui ^ podrias escribir')
                    print ("")
                    print ("")
                    input ("Pulsa enter cuando quieras salir")
        #ACABA INPUT Y EMPIEZA IF
                elif c == ("3"):
                    os.system('clear')
                    print ('El "if", al igual que "elif" y "else" es una condicional, parecida a decir "si..." en una frase castellana en condicional')
                    print ('Ejemplo:')
                    print ('    Input:')
                    print ('        variable1 = input ("si o no?")')
                    print ('        if variable1 == ("si"):')
                    print ('            print ("Bien!")')
                    print ('        elif variable1 == ("no"):')
                    print ('            print ("Pues no")')
                    print ('        else:')
                    print ('            print("Esa no es ninguna de las opciones.")')
                    print ("")
                    print ('Este comando, en el output, le preguntaria al usuario "si o no?".')
                    print ('Si le decias "si", te responderá: "Bien!"')
                    print ('Si le decias "no", te responderá: "Pues no"')
                    print ('Y, si le decias cualquier otra cosa, te diria "Esa no es ninguna de las opciones."')
                    print ("")
                    print ("")
                    input ("Pulsa enter cuando quieras salir")
        #ACABA EL IF Y EMPIEZA EL DEF
                elif c == ("4"):
                    os.system('clear')
                    print ('El "def", sirve para definir una variable, la cual, contiene una serie de comandos al ser ejecutado')
                    print ('Ejemplo:')
                    print ('    Input:')
                    print ('        def variable1():')
                    print ('            print ("cosa1")')
                    print ('            a = input ("si/no")')
                    print ('            if a == "si"')
                    print ('                print("Bien!")')
                    print ('            else:')
                    print ('                print ("Hello World!")')
                    print ("")
                    print ('         if "__name__" == "__main__"')
                    print ('            print (variable1)')
                    print ("")
                    print ('En este input, hemos consegido que al ejecutarlo, haga todas las cosas de nuestra "variable1" a la vez.')
                    print ('Como puedes ver al final del codigo, en vez de poner solo "print (variable1)" es importante recordar poner el "if "__name__" == "__main__"" de antes, ya que si no, daria error o printaria literalmente "variable1"')
                    print ("")
                    print ('Es importante saber que, como ya habrás visto a lo largo de los otros ejemplos, para definir una variable más simple, es mejor compararla a una letra.')
                    print ('Tal y como está en este ejemplo, el input que usamos es una variable, la variable "a", y luego esa variable es comparada a las posibles respuestas del usuario')
                    print ("")
                    print ("")
                    input ("Pulsa enter cuando quieras salir")
        #ACABA EL DEF Y EMPIEZA EL WHILE
                elif c == ("5"):
                    os.system('clear')
                    print ('El "while" se usa para crear bucles, iniciandolos con "while True" o con un "while False" y cerrandolos con un "break"')
                    print ('También se usa para hacer un bucle condicional, como por ejemplo...:')
                    print ("")
                    print ('    contador = 1')
                    print ('    while contador <= 5:')
                    print ('        print(contador)')
                    print ('        contador += 1')
                    print ("")
                    print ('En este codigo, tenemos un contador que estará generando numeros del 1 hasta el 5, entonces el codigo reconoceria que ahora contador ya no es menor que 5, y pararia')
                    print ("")
                    print ("")
                    print ('También se podria hacer este otro tipo de bucle condicional:')
                    print ("")
                    print ('    entrada = ""')
                    print ('    while entrada != "salir":')
                    print ('        entrada = input("Escribe algo (escribe "salir" para terminar): ")')
                    print ('        print("Escribiste:", entrada)')
                    print ("")
                    print ('En este codigo, hemos creado una variable llamada "entrada" que no era nada, y la hemos ligado a un bucle, para que hasta que "entrada" no sea "salir", no te deje salir del bucle.')
                    print ("")
                    print ("")
                    input ("Pulsa enter cuando quieras salir")
        #ACABA EL WHILE Y EMPIEZA EL FOR
                elif c == ("6"):
                    os.system('clear')
                    print ('El "for" se usa normalmente para crear listas, diccionarios, conjuntos y cadenas de elementos')
                    print ('Ejemplo:')
                    print ('    Input:')
                    print ('        frutas = ["manzana", "banana", "cereza"]')
                    print ('        for fruta in frutas:')
                    print ('            print(fruta)')
                    print ("")
                    print ('    Output:')
                    print ('        manzana')
                    print ('        banana')
                    print ('        cereza')
                    print ("")
                    print ('En este ejemplo, la variable fruta toma cada valor de la lista frutas en cada iteración y el print(fruta) imprime ese valor.')
                    print ("")
                    print ("")
                    print ('Ejemplo 2:')
                    print ('    Input:')
                    print ('        for i in range(5):')
                    print ('            print(i)')
                    print ("")
                    print ('    Output:')
                    print ('        0')
                    print ('        1')
                    print ('        2')
                    print ('        3')
                    print ('        4')
                    print ("")
                    print ('El range(5) genera una secuencia de números del 0 al 4 (5 no está incluido). En cada iteración, i toma el valor del siguiente número en la secuencia y print(i) lo imprime.')
                    print ("")
                    print ("")
                    input ("Pulsa enter cuando quieras salir")
        #ACABA FOR Y EMPIEZA BUSQUEDA
                elif c == ("7"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://aprendeconalf.es/docencia/python/ejercicios/"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif c == ("0"):
                    os.system('clear')
                    break
            #ELSE de basicos de python
                else:
                    print ("Esa no es ninguna de las opciones...")
                    time.sleep(4)
                    print ("Prueba de nuevo!")
                    time.sleep(2)
                    os.system('clear')
#ACABA basicos de python Y COMEINZA pygame
        elif b == ("2"):
            while True:
                os.system('clear')
                print ("Pygame es una extensión de python, en la cual, te permite llevar el codigo a un proximo nivel, la creación de tu propia aplicación")
                print ("En pygame, podrás crear una pantalla emergente al iniciar el codigo, en la que se reflejará tu codigo en forma de videojuego.")
                print ("Usando comandos como:")
                print ('"screen = pygame.display.set_mode((800, 600))"')
                print ("Y")
                print ('"imagen = pygame.image.load("ruta_a_tu_imagen.png")"')
                print ('Ya podrias crear un codigo en el que se mostrara un imagen (así como esta escrito, no funcionaria).')
                time.sleep(3)
                print ("")
                print ('Aqui tienes una serie de paginas que podrian ayudarte a aprender como funciona, y retarte a aprender más!')
                print ("")
                print ('    1 Para ver un ejercicio basico de pygame - "Pong"')
                print ('    2 Para ver un ejercicio medio de pygame - "Pacman"')
                print ('    3 Para ver un ejercicio dificil de pygame - "Snake Game"')
                print ("")
                print ('    0 Para volver al menú principal')
                print ("")
                d = input ("Que ejercicio te gustaria abrir?")
        #EMPIEZA IF (pygame)
                if d == ("1"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://www.mclibre.org/consultar/python/lecciones/pygame-pong.html"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif d == ("2"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://medium.com/@AIisDUMB/creating-a-pac-man-game-with-pygame-a-step-by-step-guide-a774b6691751/"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif d == ("3"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://www.edureka.co/blog/snake-game-with-pygame/"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif d == ("0"):
                        os.system('clear')
                        break
            #ELSE de pygame
                else:
                    print ("Esa no es ninguna de las opciones...")
                    time.sleep(4)
                    print ("Prueba de nuevo!")
                    time.sleep(2)
                    os.system('clear')
#ACABA pygame Y COMEINZA matplotlib
        elif b == ("3"):
            while True:
                os.system('clear')
                print ("Matplotlib, al igual que pygame, es una extensión de python.")
                print ("En esta, te abre la posibilidad de crear pantallas emergentes con graficos que muestren los datos y magnitudes que tu elijas para tu grafico.")
                print ("Se pueden crear todo tipo de graficos, y los estilos y formas, con complematente editables")
                print ("")
                print ("Para practicar y aprender el contenido de mathplotlib, lo mejór es entrar directamente a ejercicios practicos.")
                print ("")
                print ("    Pulsa 1 para abrir los ejercicios practicos de mathplotlib")
                print ("    Pulsa 0 para volver al menú principal.")
                print ("")
                print ("")
                e = input ("Que te gustaria hacer?")
        #EMPIEZA IF (matplotlib)
                if e == ("1"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://aprendeconalf.es/docencia/python/ejercicios/matplotlib/"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif e == ("0"):
                    os.system('clear')
                    break
        #ELSE de mathplotlib
                else:
                    print ("Esa no es ninguna de las opciones...")
                    time.sleep(4)
                    print ("Prueba de nuevo!")
                    time.sleep(2)
                    os.system('clear')
#ACABA matplotlib y comienza selenium
        elif b == ("4"):
            while True:
                os.system('clear')
                print ('Selenium es una versión de unos programas llamados "scrapy", los cuales, sirven para abrir paginas web y hacer procesos web automaticamente.')
                print ('Estos codigos, precisan de una extensión llamada "webmanager" para que el codigo de selenium sepa en qué buscador tiene que ser ejecutado su codigo.')
                print ('También, claramente, hará falta tener ese buscador descargado. Es por ese motivo por el que este codigo, sin Google Chrome, no funciona.')
                print ('')
                print ('Para empezar un programa en selenium, tendremos que comenzar siempre llamando a su libreria con un "import", la de webmanager y seguir especificando en que buscador se va a ejecutar el programa.')
                print ('Después, lo más común es crear una variable llamada "url", y que esta sea la url a la que queremos entrar, para así hacer más facil la tarea de escritura de codigo.')
                print ('Segimos con un "driver.get(url)" para que así nos abra la url.')
                print ('Ejemplo visual de todo junto:')
                print ("")
                print ("    import selenium")
                print ("    from selenium import webdriver")
                print ('    driver = webdriver.Chrome()')
                print ('    url = "url"')
                print ('    driver.get(url)')
                print ("")
                print ('Este codigo, abriria chrome, abriria la url, y luego la dejaria abierta. Pero también podriamos programarlo para que se cierre automaticamente, o para que haga algo más dentro de la web.')
                print ("")
                print ('Es importante saber que, si quieres que tu codigo tenga alguna interacción con los objetos que se muestran en tu url, tendrias que encontrar el id del objeto con el que quieras interactuar.')
                print ('este id de objeto, normalmente suele ser facilmente encontrado si le damos a "click derecho - inspeccionar" en la url')
                time.sleep(8)
                print ("")
                print ('Aqui tienes dos ejemplos de lo que hace selenium, además, las paginas que abrirán los ejemplos, te servirán para entender mejor selenium y para probar tus habilidades.')
                print ("")
                print ('    1 Para abrir una explicación mmás detallada del funcionamiento de selenium')
                print ('    2 Para un test')
                print ('    0 Para volver al menú principal')
                print ("")
                print ("Que te gustaria abrir?")
                f = input ("")
        #EMPIEZA IF (selenium)
                if f == ("1"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://aprendepython.es/pypi/scraping/selenium/"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif f == ("2"):
                    print ("Esto no deberia de llevar mucho tiempo.")
                    print ("Espera a que cargue...")
                    driver = webdriver.Chrome()
                    url = "https://www.testgorilla.com/es/catalogo-de-pruebas/habilidades-en-programacion/prueba-de-selenium-con-python/"
                    driver.get(url)
                    driver.content = driver.page_source
                    time.sleep(3)
                elif f == ("0"):
                    os.system('clear')
                    break
                else:
                    print ("Esa no es ninguna de las opciones...")
                    time.sleep(4)
                    print ("Prueba de nuevo!")
                    time.sleep(2)
                    os.system('clear')
#ACABA selenium
        elif b == ("0"):
            os.system('clear')
            print ("Adios!")
            break
    #ELSE de el menú principal
        else:
            print ("Esa no es ninguna de las opciones...")
            time.sleep(4)
            print ("Prueba de nuevo!")
            time.sleep(2)
            os.system('clear')
#ELSE de mensage de aviso (pre-mensage)
else:
    print ("Esa no es ninguna de las opciones...")
    time.sleep(4)
    print ("Prueba de nuevo reabriendo el codigo!")
    time.sleep(2)
    print ("Adios!")
    time.sleep(1)
    os.system('clear')