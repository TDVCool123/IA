def pendiente(x,mini,maxi):
    y=(x-mini)/(maxi-mini)
    return y


mini=0
maxi=0
# Preguntar al usuario los datos
penales = int(input("¿Cuántos penales metiste de 25 tiros? "))
vueltas = int(input("¿Cuántas vueltas a la cancha das antes de cansarte? "))
tiempo_100m = int(input("¿En cuántos segundos haces 100m planos? "))



# Calcular la pendiente para cada premisa
if penales<=14:
    maxi=14
    mini=0
    p1 = pendiente(penales, mini, maxi)
elif 14 < penales <= 18:
    maxi=18
    mini=14
    p1 = pendiente(penales, mini, maxi)
elif 18 < penales <= 25:
    maxi=25
    mini=18
    p1 = pendiente(penales, mini, maxi)
    

if vueltas <= 4:
    p2 = 0
elif 4 < vueltas <= 8:
    maxi=8
    mini=4
    p2 = pendiente(vueltas, mini, maxi)
elif vueltas >= 9:
    p2 = 1
    
    
if tiempo_100m==0:
    p3 = 1
elif 0<tiempo_100m <=11:
    maxi=0
    mini=11
    p3 = pendiente(tiempo_100m, mini, maxi)
elif tiempo_100m>=12:
    p3=0
    
#print("Resultado p1:", p1)
#print("Resultado p2:", p2)
#print("Resultado p3:", p3)
    
r1=min(p1,p2)*0.8
r2=min(p1,p3)*0.9
r3=min(p2,p3)*0.75

#print("Resultado r1:", r1)
#print("Resultado r2:", r2)
#print("Resultado r3:", r3)

t=max(r1,r2,r3)

if t == r1:
    print(f"El candidato es adecuado para el equipo con certeza {t},porque se evaluó con 'alta resistencia' con valor de certeza {p2} (dio {vueltas} vueltas a la cancha en 10 min) y con 'buen tiro penal' con certeza {p1} (metió {penales} goles en 25 intentos) y tiene un 'sprint' de {tiempo_100m}s.")
elif t == r2:
    print(f"El candidato es adecuado para el equipo con certeza {t},porque se evaluó con 'buen tiro penal' con certeza {p1} (metió {penales} goles en 25 intentos) y con un 'buen sprint' de {tiempo_100m}s y tiene una resistencia con valor de certeza {p2} (dio {vueltas} vueltas a la cancha en 10 min) y ")
else:
    print(f"El candidato es adecuado para el equipo con certeza {t},porque se evaluó con 'alta resistencia' con valor de certeza {p2} (dio {vueltas} vueltas a la cancha en 10 min)  y con un 'buen sprint' de {tiempo_100m}s y tiene un tiro penal con certeza {p1} (metió {penales} goles en 25 intentos)")


