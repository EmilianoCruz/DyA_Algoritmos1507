texto="Iu Pzubfa, vppwfwaiiaoabq iu Zamtjiwnta pzub�uwxa, axq tb mudx lvbq iu ougatza muzqwa lt \
qazzwqvwza aq la iu mvmtiuqwvb axq xwqtaa ab Atzvma vffwlabquia, ouwx ntw fvomzabl utxxw la bvojzatr \
qazzwqvwzax zamuzqwx lubx iax Uoazwntax, i'vfaub Wblwab aq ia Mufwpwnta. Oaojza pvbluqatz la i'Tbwvb \
atzvmaabba, iu Pzubfa u mvtz fumwquia Muzwx, mvtz iubeta vppwfwaiia ia pzub�uwx aq mvtz ovbbuwa i'atzv.\
Iu Pzubfa oaqzvmviwquwba axq xwqtaa u tba lax arqzaowqax vffwlabquiax la i'Atzvma. Aiia axq jvzlaa muz iu oaz\
lt Bvzl ut bvzl, iu Oubfha ut bvzl-vtaxq, i'vfaub Uqiubqwnta u i'vtaxq aq iu oaz Oalwqazzubaa ut xtl-axq.\
Aiia axq pzvbquiwaza la iu Jaiewnta aq lt Itraojvtze ut bvzl-axq, la i'Uiiaoueba aq la iu Xtwxxa u i'axq,\
la i'Wquiwa aq la Ovbufv ut xtl-axq, la i'Axmueba aq l'Ublvzza ut xtl-vtaxq."


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
  archivo = open('diccionarioFrances.txt', 'r')
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

#Descartamos c,k,s,y porque no aparecen en el texto:
posA='e'
posB='n'
#posC:'fkvwz'
posD='y'
posE='g'
posF='c'
posG='j'
posH='h'
posI='l'
posJ='b'
#posK:'fkvwz'
posL='d'
posM='p'
posN='q'
posO='m'
posP='f'
posQ='t'
posR='x'
#posS='fkvwz'
posT='u'
posU='a'
posV='o'
posW='i'
posX='s'
#posY='fkvwz'
posZ='r'

#probamos con qazzwqvwza
c=0
# for p in dic:
#     if len(p)== 10: 
#         if (p[1] == p[-1]) and (p[2] == p[3]== p[-2]) and (p[0] == p[5]) and (p[4] == p[7]):
#             print(p)

#probamos con Oaojza 
# for p in dic: 
#     if len(p) == 6: 
#         if (p[0]==p[2]) and (p[1]==p[-1]):
#             c+=1
#             print(p)


#probando Aiia
# for p in dic: 
#     if len(p) == 4:
#         if (p[0]==p[-1]) and (p[1]==p[2]):
#             c+=1
#             print(p)

#probando con vffwlabquia
# for p in dic: 
#     if len(p) == 11: 
#         if (p[1]==p[2]) and (p[5]==p[-1]):
#             if len(set(p[3:-1])) == len(p[3:-1]):
#                 print(p)
#                 c+=1

#Probando con axq
# for p in dic: 
#     if len(p) == 3: 
#         if p[-1] == posQ and p[1] in posX:
#             print(p)
#             c+=1

#probando con mvmtiuqwvb
# for p in dic: 
#     if len(p) == 10: 
#         if p[0] == p[2] and (p[0] and p[2]) in posM and p[3] in posT: 
#             if p[-1] == posB:
#                 c+=1
#                 print(p)

#probando con ntw
# for p in dic: 
#     if len(p) == 3: 
#         if p[0] in posN and p[1] in posT and p[2] in posW:
#             print(p)
#             c+=1

#probando con iubeta
# for p in dic: 
#     if len(p) == 6:
#         if len(set(p[:])) == len(p[:]):
#             if (p[0] in posI) and (p[1] in posU) and (p[2]in posB):
#                 print(p)
#                 c+=1

#probando con ougatza
# for p in dic: 
#     if len(p) == 7: 
#         if p[3] == p[-1]:
#             if len(set(p[:-1])) == len(p[:-1]):
#                 if (p[0] in posO) and (p[1] in posU):
#                     print(p)
#                     c+=1

#Probando con mudx
# for p in dic: 
#     if len(p) == 4:
#         if len(set(p[:])) == len(p[:]):
#             if (p[0] in posM) and (p[1] in posU) and (p[2] in posD): 
#                 print(p)
#                 c+=1

#probando con bvojzatr
# for p in dic: 
#     if len(p) == 8: 
#         if len(set(p[:])) == len(p[:]): 
#             if (p[0] in posB) and (p[1] in posV) and (p[2] in posO):
#                 c+=1
#                 print(p)

llave='enXygcjhlbXdpqmftxXuaoisXr'
b=descifraSustituye(texto,llave)
print(b)


print(c)



  
            



