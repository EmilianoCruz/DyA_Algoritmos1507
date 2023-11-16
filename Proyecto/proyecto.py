#Textos
texto1= "Iu Pzubfa, vppwfwaiiaoabq iu Zamtjiwnta pzub�uwxa, axq tb mudx lvbq iu ougatza muzqwa lt qazzwqvwza aq la iu mvmtiuqwvb axq xwqtaa ab Atzvma vffwlabquia, ouwx ntw fvomzabl utxxw la bvojzatr qazzwqvwzax zamuzqwx lubx iax Uoazwntax, i'vfaub Wblwab aq ia Mufwpwnta. Oaojza pvbluqatz la i'Tbwvb atzvmaabba, iu Pzubfa u mvtz fumwquia Muzwx, mvtz iubeta vppwfwaiia ia pzub�uwx aq mvtz ovbbuwa i'atzv.Iu Pzubfa oaqzvmviwquwba axq xwqtaa u tba lax arqzaowqax vffwlabquiax la i'Atzvma. Aiia axq jvzlaa muz iu oaz lt Bvzl ut bvzl, iu Oubfha ut bvzl-vtaxq, i'vfaub Uqiubqwnta u i'vtaxq aq iu oaz Oalwqazzubaa ut xtl-axq. Aiia axq pzvbquiwaza la iu Jaiewnta aq lt Itraojvtze ut bvzl-axq, la i'Uiiaoueba aq la iu Xtwxxa u i'axq, la i'Wquiwa aq la Ovbufv ut xtl-axq, la i'Axmueba aq l'Ublvzza ut xtl-vtaxq."

texto2= "Texto 2: Ez lideg�xz z�u etviqz auz jeougxz ngxaeaugxz au medolel jegoqmu. Z�u nxoyxz vxgetjxqlx vgeqaxz x heglotevoquzuz, xyhxlu nxtuz axqlxz, rugjeauz nug axqlxz nuqloeviauz x lgoeqvitegxz, ax jeoug ui jxqug lejeqmu. Enxzeg ax zie enegxqhoe ejxe�eauge, aez 375 xznxhoxz huqmxhoaez ax lideg�xz qu jiqau, enxqez aiez ui lgxz gxetocegej elesixz q�u ngukuheauz e mijequz, vxgetjxqlx nug huqriqao-tuz huj etvij jejorxgu jegoqmu six rec neglx ax zie aoxle, huju zigrozlez huj ruhez. . Gxtehouqeauz ez geoez x siojxgez, uz lideg�xz jiaegej gxtelokejxqlx nuihu axzax ziez ugovxqz xkutilokez qu nxgouau Axkuqoequ, me siezx 400 jotm�xz ax equz."

#Definimos la función para calcular la frecuencia
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
def frecuencia(parrafo):
    frecuencias = {}
    for c in alfabeto:
        frecuencias [c] = 0
    for e in parrafo:
        if e in alfabeto:
            frecuencias[e] += 1
    #Para ordenar el texto de forma decreciente 
    orden = dict(sorted(frecuencias.items(), key=lambda item:item[1],reverse=True))
    print (orden)

print("*-"*8+"Primer Texto"+"*-"*8)
frecuencia(texto1)
print("*-"*8+"Segundo Texto"+"*-"*8)
frecuencia(texto2)




