from random import randint

print(".-.-.-. PARTE 1 .-.-.-.")

def calculaDia(dia, diaPost):
    return semana[(dia+diaPost)%7]

semana = {0:"domingo", 1:"lunes", 2:"martes", 3:"miercoles", 4:"jueves", 5:"viernes", 6:"sabado"}

for x in range(5):
    i = randint(0,7)
    print(f"El día {semana[x]} + {i} días =", calculaDia(x,i) )




print(".-.-.-. PARTE 2 .-.-.-.")


def anioBisiesto2(anio): 
    if anio % 4 == 0:
        if (anio  % 100 == 0) and (anio % 400 != 0):
            return False
        else:
            return True
    else:
        return False

aniosPrueba=[1996,2023,1900,1994, 1996,2024]

for a in aniosPrueba: 
    print(f"¿El año {a} es bisesto?", "Sí es año bisiesto" if anioBisiesto2(a) else "No es año bisiesto")



