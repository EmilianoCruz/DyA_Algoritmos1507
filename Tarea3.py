texto="nsyqq ngtxlo leswitaatn dgns leswi xyttwi uwiw nlviwx sa pyk ltx pyn yxwl ae naqyx vakeais uln sa\
zw qwes yt gsswi naqysgxw eai sua ai spiww pagin. vatnwjgwtsqo, pw eyhwx pyn wow eyikqo gcat\
spw qlswns iwcaisn ae spw qwewziw-oanpyxl whcwxysyat sa klin (spyn atw uln sa slbw aee eiak\
qgtli zlnw ltx kyrps lvsglqqo ngvvwwx) ltx ciwswtxwx npw ulnt’s spwiw"

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def descifraSustituye(cadena, alfabetoLlave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'    
    nuevaCadena = ""    
    for letra in cadena:
        if letra in alfabeto:
            posicion=alfabeto.find(letra)
            nuevaCadena= nuevaCadena+ alfabetoLlave[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

def cargaPalabras():
  archivo = open('words.txt', 'r')
  renglon = archivo.readline()
  palabras = renglon.split()
  print(len(palabras),'palabras leidas')
  return palabras

def frecuencia(parrafo):
    frecuencias = {}
    for c in alfabeto:
        frecuencias [c] = 0
    for e in parrafo:
        if e in alfabeto:
            frecuencias[e] += 1
    print (frecuencias)

dic = cargaPalabras()
frecuencia(texto)

#Descartamos f y m porque no aparecen en el texto
posA= "o"
posB= "k"
posC= "p"
posD= "j"
posE= "f"
#posF= "abcdefghijklmnopqrstuvwxyz"
posG= "u"
posH= "x"
posI= "r"
posJ= "q"
posK= "m"
posL= "a"
#posM= "abcdefghijklmnopqrstuvwxyz"
posN= "s"
posO= "y"
posP= "h"
posQ= "l"
posR= "g"
posS= "t"
posT= "n"
posU= "w"
posV= "c"
posW= "e"
posX= "d"
posY= "i"
posZ= "b"

#probamos con ciwswtxwx en el diccionario
c=0
for p in dic: 
    if len(p)== 9:
        if p[2] == p[4] == p[-2] and p[-3] == p[-1]:
            c+=1
            print(p)

#probamos con whcwxysyat
for p in dic: 
    if len(p)==10:
        if p[0] == p[3] and p[5] == p[-3]:
            if (p[0] and p[3]) in posW and p[-1] in posT :
                c+=1
                print(p)

#probamos con lvsglqqo
for p in dic: 
    if len(p)==8:
        if p[0] == p[4] and p[-2] == p[-3]:
            if p[2] == posS and p[-2]==posQ:
                c+=1
                print(p)

#probando con leswitaatn
for p in dic: 
    if len(p)== 10:
        if p[5] == p[-2] and p[6] == p[7]:
            if (p[5] and p[-2]) == posT and (p[6] and p[7]) == posA:
                c+=1
                print(p)

#probando con spiww
for p in dic: 
    if len(p)== 5: 
        if p[-1] == p[-2]:
            if (p[-1] and p[-2]) == posW: 
                if p[0]==posS and p[2]==posI:
                    print(p)
                    c+=1

#probando con dgns
for p in dic: 
    if len(p) == 4:
        if p[0] in posD and p[1] == posG and p[2] == posN and p[3] == posS:
            c+=1
            print(p)

#probando con kyrps
for p in dic: 
    if len(p)==5:
        if p[0] in posK and p[1] == posY and p[2] in posR and p[3] == posP and p[4] == posS:
            print(p)
            c+=1

#probando con eyikqo
for p in dic:
    if len(p)==6: 
        if p[0]==posE and p[1] == posY and p[2] == posI and p[3] in posK and p[4] == posQ and p[-1] == posO:
            print(p)
            c+=1

#probando con slbw
for p in dic:
    if len(p)==4:
        if p[0]==posS and p[1] == posL and p[2] in posB and p[-1] == posW:
            c+=1
            print(p)

#probando con uwiw
for p in dic: 
    if len(p) == 4: 
        if p[1] == p[3]:
            if (p[1] and p[3]) == posW and p[-2] == posI and p[0] in posU:
                c+=1
                print(p)

#probando con zlnw
for p in dic: 
    if len(p) == 4: 
        if p[0] in posZ and p[1] == posL and p[2] == posN and p[3]== posW: 
            c+=1
            print(p)

#probando con zw
for p in dic: 
    if len(p)== 2:
        if p[0] in posZ and p[1] == posW:
            print(p)
            c+=1
print(c)


llave='okpjfXuxrqmaXsyhlgtnwcedib'
b=descifraSustituye(texto,llave)
print(b)


