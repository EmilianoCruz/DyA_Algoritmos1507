
vocabulario = []

#Definimos una función que lea el archivo y retornamos los renglones leídos
def leerArchivo():
  archivo = open('Textos/textoItaliano.txt', 'r', encoding="utf8")
  renglon = archivo.readlines()
  return renglon

#Creamos una función que sirve para filtrar las palabras y solo se agreguen 
# al diccionario palabras validas y no signos de puntuación, exclamación, etc..
def filtrarPalabras(caracteres):
    vocabulario=caracteres.split()
    filtradas = []
    for palabra in vocabulario:
        palabraFiltrada= ''.join(caracter for caracter in palabra if caracter.isalpha())
        if palabraFiltrada:
            filtradas.append(palabraFiltrada.lower())
    return filtradas

#Creamos una función que cree el diccionario filtrando los caracteres con ayuda 
#de la función filtrarPalabras()
def crearDiccionario(palabras, renglones):
    for c in renglones:
        renglon = filtrarPalabras(c)
        for palabra in renglon:
            if palabra not in vocabulario:
                palabras.append(palabra)
    palabras.sort()
    nuevoArchivo = "diccionarioItaliano.txt"
    archivo = open(nuevoArchivo, "w")
    for palabra in vocabulario:
        archivo.write(palabra + " ")


fila = leerArchivo()
crearDiccionario(vocabulario, fila)
print(len(vocabulario), "palabras leídas")

