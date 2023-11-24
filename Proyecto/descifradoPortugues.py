texto = "Ez lidegõxz zãu etviqz auz jeougxz ngxaeaugxz au medolel jegoqmu. \
Zãu nxoyxz vxgetjxqlx vgeqaxz x heglotevoquzuz, xyhxlu nxtuz axqlxz, rugjeauz nug axqlxz \
nuqloeviauz x lgoeqvitegxz, ax jeoug ui jxqug lejeqmu. Enxzeg ax zie enegxqhoe ejxeçeauge, aez \
375 xznxhoxz huqmxhoaez ax lidegõxz qu jiqau, enxqez aiez ui lgxz gxetocegej elesixz qãu ngukuheauz \
e mijequz, vxgetjxqlx nug huqriqao-tuz huj etvij jejorxgu jegoqmu six rec neglx ax zie aoxle, huju \
zigrozlez huj ruhez. . Gxtehouqeauz ez geoez x siojxgez, uz lidegõxz jiaegej gxtelokejxqlx nuihu \
axzax ziez ugovxqz xkutilokez qu nxgouau Axkuqoequ, me siezx 400 jotmõxz ax equz."


alfabeto='abcdefghijklmnopqrstuvwxyz'

def descifraSustituye(cadena, alfabetoLlave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'    
    nuevaCadena = ""    
    for letra in cadena.lower():
        if letra in alfabeto:
            posicion=alfabeto.find(letra)
            nuevaCadena= nuevaCadena+ alfabetoLlave[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

def cargaPalabras():
  archivo = open('diccionarioPortugues2.txt', 'r')
  renglon = archivo.readline()
  palabras = renglon.split()
  print(len(palabras),'palabras leidas')
  return palabras

def frecuencia(parrafo):
    frecuencias = {}
    for c in alfabeto:
        frecuencias [c] = 0
    for e in parrafo.lower():
        if e in alfabeto:
            frecuencias[e] += 1
    orden = dict(sorted(frecuencias.items(), key=lambda item:item[1],reverse=True))
    print (orden)

dic = cargaPalabras() 
frecuencia(texto)

posA='d'
#posB='abcdefghijklmnopqrstuvwxyz'
posC='abcdefghijklmnopqrstuvwxyz'
posD='abcdefghijklmnopqrstuvwxyz'
posE='a'
#posF='abcdefghijklmnopqrstuvwxyz'
posG='abcdefghijklmnopqrstuvwxyz'
posH='abcdefghijklmnopqrstuvwxyz'
posI='abcdefghijklmnopqrstuvwxyz'
posJ='abcdefghijklmnopqrstuvwxyz'
posK='abcdefghijklmnopqrstuvwxyz'
posL='abcdefghijklmnopqrstuvwxyz'
posM='abcdefghijklmnopqrstuvwxyz'
posN='abcdefghijklmnopqrstuvwxyz'
posO='abcdefghijklmnopqrstuvwxyz'
#posP='abcdefghijklmnopqrstuvwxyz'
posQ='abcdefghijklmnopqrstuvwxyz'
posR='abcdefghijklmnopqrstuvwxyz'
posS='abcdefghijklmnopqrstuvwxyz'
posT='abcdefghijklmnopqrstuvwxyz'
posU='abcdefghijklmnopqrstuvwxyz'
posV='abcdefghijklmnopqrstuvwxyz'
#posW='abcdefghijklmnopqrstuvwxyz'
posX='e'
posY='abcdefghijklmnopqrstuvwxyz'
posZ='s'

c=0
#probamos con nxoyxz
# for p in dic: 
#     if len(p) == 6:
#         if (p[1] == p[4]):
#             print(p)

#probamos con mendolel
# for p in dic: 
#     if len(p) == 8: 
#         if (p[3] == p[8]):
#             print(p)


#probamos con lgoeqvitegxz
# for p in dic: 
#     if len(p) == 13: 
#         if(p[1] == p[9] == p[12]) and (p[3] == p[7]):
#             print(p)

#probando con gxtelokejxqlx
c=0
# for p in dic: 
#     if len(p) == 13: 
#         if(p[1] == p[9] == p[12]) and (p[3] == p[7]):
#             print(p)


#probamos con enegxqhoe
# for p in dic: 
#     if len(p) == 9: 
#         if p[0] == p[2] == p[-1]:
#             if len(set(p[1:-1])) == len(p[1:-1]):
#                 print(p)
#                 c+=1
                    
#probando con axzax
# for p in dic: 
#     if len(p) == 5: 
#         if p[0] == p[-2] and p[1] == p[-1]:
#             if (p[1] and p[-1]) in posX:
#                 c+=1
#                 print(p)

#probando con vxgetjxqlx 
# for p in dic: 
#     if len(p) == 10: 
#         if (p[1] == p[-1] == p[-4]):
#             if (p[1] and p[-1] and p[-4]) == posX:
#                 c+=1

#probando con jiaegej
# for p in dic: 
#     if len(p) == 7: 
#         if p[0] == p[-1] and p[3] == p[-2]:
#             if (p[3] and p[-2]) in posE:
#                 print(p)
#                 c+=1


alfabetoLlave= "dxzbaXrcumvthpiXnfqlogXexs"
b=descifraSustituye(texto,alfabetoLlave)

print(b)
