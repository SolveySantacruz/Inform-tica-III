calificaciones={"001": {"Nombre": "Cristian Pachon",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.2,   "Artes": 4.0,  "Musica": 0.5},
"002": {"Nombre": "Daniela Pineda",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 4.0,   "Artes": 3.1,  "Musica": 4.0}}

d_001=[]
dd_001=[]
prom=[]
promedios=[]
promediosPorEstudiante=[]
claves=[]

for j in calificaciones.keys():
    for i in calificaciones[j].values():
        d_001.append(i)
        if type(i)==float:
            dd_001.append(i)   
        elif type(i)==str:
            claves.append(i)

for i in range(0,len(dd_001),5):
    prom=sum(dd_001[i:i+5])/5
    promedios.append(prom)

print(promedios)
print(promedios.index(2.58))

sem={'semana':{'2D':{'nino':5000,'adulto':8000},'3D':{'nino':8000},'adulto':12000}}
finde={'finde':{'2D':{'nino':7000,'adulto':9000},'3D':{'nino':9000},'adulto':15000}}

#lunes
print(7*sem['semana']['2D']['nino'])
