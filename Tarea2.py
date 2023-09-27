parrafo ="hola como estas espero que muy bien este es un set de palabras para crear un diccionario para la clase de disenio y analisis de algoritmos\
    ya no se que mas poner entonces voy a escribir palabras al azar como perro gato leopardo puma leon elefante programacio inteligencia artificial \
    renglon datos linea cerrar abrir escribir realizar bien mal oso sol sal negro blanco rojo color morado dulces de diferente sabor textura y calidad\
    cansancio lenguaje formal computadora estuche mueble cocina cuchillo mochila cuaderno lapiz pluma ganso sueter chamarra gorra playera estufa flores amarillo\
    botella agua fuego tierra vaso pastilla caja herramienta pants olor suave ruido flauta bocina silencio puerta facultad estudios aragon comida conocer\
    cabello camello pelo lengua ojos nariz olfato manos dedos dado lapicero cocinar coser escribir enviar contenido redes sociales correo telefono juguete\
    libro cuaderno pelota palo beso sastre cerro tarro carro peluche nene oreja nube nectar"

def diccionario(texto):
    palabras=list(set(texto.split())) #Separamos las palabras, a su vez evitamos repetirla y generamos la lista
    palabras.sort() #ordenamos las palabras
    archivo= open('diccionario.txt','w') #creamos el archivo .txt que contendra el diccionario
    limite= 0 
    for palabra in palabras:
        if limite == 5:      #definimos un limite de palabras por renglon para mejor presentación
            archivo.write('\n')
            limite= 0
        archivo.write(palabra + '   ') #escribimos las palabras en el archivo .txt
        limite += 1
    archivo.close() #por ultimo cerramos el archivo

diccionario(parrafo)
  



