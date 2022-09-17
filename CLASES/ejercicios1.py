
# -----------Ejercicios informe 1----------------

#------------------------------------------------------------------------------------------

# Se debe calcular el módulo de la resta de los vectores

P1=(2,2,3)
P2=(2,3,4)
P3=(1,1,3)
P4=(0.5,0.5,2)
P5=(1,2,1)
P6=(1, 0.5, 1)
P7=(3, 2, 0.5)
P8=(3, 1, 2)
P9=(0, 0, 0)
P10=(2, 0, 0.5) 
pos=[]
min_mod=[]

# Dejando fijo el primer punto P1
MODULO1=[]
mod12=((P1[0]-P2[0])**2+(P1[1]-P2[1])**2+(P1[2]-P2[2])**2)**0.5
mod13=((P1[0]-P3[0])**2+(P1[1]-P3[1])**2+(P1[2]-P3[2])**2)**0.5
mod14=((P1[0]-P4[0])**2+(P1[1]-P4[1])**2+(P1[2]-P4[2])**2)**0.5
mod15=((P1[0]-P5[0])**2+(P1[1]-P5[1])**2+(P1[2]-P5[2])**2)**0.5
mod16=((P1[0]-P6[0])**2+(P1[1]-P6[1])**2+(P1[2]-P6[2])**2)**0.5
mod17=((P1[0]-P7[0])**2+(P1[1]-P7[1])**2+(P1[2]-P7[2])**2)**0.5
mod18=((P1[0]-P8[0])**2+(P1[1]-P8[1])**2+(P1[2]-P8[2])**2)**0.5
mod19=((P1[0]-P9[0])**2+(P1[1]-P9[1])**2+(P1[2]-P9[2])**2)**0.5
mod10=((P1[0]-P10[0])**2+(P1[1]-P10[1])**2+(P1[2]-P10[2])**2)**0.5
MODULO1.append(mod12); MODULO1.append(mod13); MODULO1.append(mod14)
MODULO1.append(mod15); MODULO1.append(mod16); MODULO1.append(mod17)
MODULO1.append(mod18); MODULO1.append(mod19); MODULO1.append(mod10)

min_modulo1=min(MODULO1)
pos1=MODULO1.index(min_modulo1)

# Dejando fijo el P2
MODULO2=[]
mod23=((P2[0]-P3[0])**2+(P2[1]-P3[1])**2+(P2[2]-P3[2])**2)**0.5
mod24=((P2[0]-P4[0])**2+(P2[1]-P4[1])**2+(P2[2]-P4[2])**2)**0.5
mod25=((P2[0]-P5[0])**2+(P2[1]-P5[1])**2+(P2[2]-P5[2])**2)**0.5
mod26=((P2[0]-P6[0])**2+(P2[1]-P6[1])**2+(P2[2]-P6[2])**2)**0.5
mod27=((P2[0]-P7[0])**2+(P2[1]-P7[1])**2+(P2[2]-P7[2])**2)**0.5
mod28=((P2[0]-P8[0])**2+(P2[1]-P8[1])**2+(P2[2]-P8[2])**2)**0.5
mod29=((P2[0]-P9[0])**2+(P2[1]-P9[1])**2+(P2[2]-P9[2])**2)**0.5
mod20=((P2[0]-P10[0])**2+(P2[1]-P10[1])**2+(P2[2]-P10[2])**2)**0.5
MODULO2.append(mod23); MODULO2.append(mod24)
MODULO2.append(mod25); MODULO2.append(mod26); MODULO2.append(mod27)
MODULO2.append(mod28); MODULO2.append(mod29); MODULO2.append(mod20)

min_modulo2=min(MODULO2)
pos2=MODULO2.index(min_modulo2)

# Dejando fijo el P3
MODULO3=[]
mod34=((P3[0]-P4[0])**2+(P3[1]-P4[1])**2+(P3[2]-P4[2])**2)**0.5
mod35=((P3[0]-P5[0])**2+(P3[1]-P5[1])**2+(P3[2]-P5[2])**2)**0.5
mod36=((P3[0]-P6[0])**2+(P3[1]-P6[1])**2+(P3[2]-P6[2])**2)**0.5
mod37=((P3[0]-P7[0])**2+(P3[1]-P7[1])**2+(P3[2]-P7[2])**2)**0.5
mod38=((P3[0]-P8[0])**2+(P3[1]-P8[1])**2+(P3[2]-P8[2])**2)**0.5
mod39=((P3[0]-P9[0])**2+(P3[1]-P9[1])**2+(P3[2]-P9[2])**2)**0.5
mod30=((P3[0]-P10[0])**2+(P3[1]-P10[1])**2+(P3[2]-P10[2])**2)**0.5

MODULO3.append(mod34); MODULO3.append(mod35); MODULO3.append(mod36)
MODULO3.append(mod37); MODULO3.append(mod38); MODULO3.append(mod39)
MODULO3.append(mod30)

min_modulo3=min(MODULO3)
pos3=MODULO3.index(min_modulo3)

# Dejando fijo el P4
MODULO4=[]
mod45=((P4[0]-P5[0])**2+(P4[1]-P5[1])**2+(P4[2]-P5[2])**2)**0.5
mod46=((P4[0]-P6[0])**2+(P4[1]-P6[1])**2+(P4[2]-P6[2])**2)**0.5
mod47=((P4[0]-P7[0])**2+(P4[1]-P7[1])**2+(P4[2]-P7[2])**2)**0.5
mod48=((P4[0]-P8[0])**2+(P4[1]-P8[1])**2+(P4[2]-P8[2])**2)**0.5
mod49=((P4[0]-P9[0])**2+(P4[1]-P9[1])**2+(P4[2]-P9[2])**2)**0.5
mod40=((P4[0]-P10[0])**2+(P4[1]-P10[1])**2+(P4[2]-P10[2])**2)**0.5

MODULO4.append(mod45); MODULO4.append(mod46); MODULO4.append(mod47)
MODULO4.append(mod48); MODULO4.append(mod49); MODULO4.append(mod40)

min_modulo4=min(MODULO4)
pos4=MODULO4.index(min_modulo4)

# Dejando fijo el P5
MODULO5=[]
mod56=((P5[0]-P6[0])**2+(P5[1]-P6[1])**2+(P5[2]-P6[2])**2)**0.5
mod57=((P5[0]-P7[0])**2+(P5[1]-P7[1])**2+(P5[2]-P7[2])**2)**0.5
mod58=((P5[0]-P8[0])**2+(P5[1]-P8[1])**2+(P5[2]-P8[2])**2)**0.5
mod59=((P5[0]-P9[0])**2+(P5[1]-P9[1])**2+(P5[2]-P9[2])**2)**0.5
mod50=((P5[0]-P10[0])**2+(P5[1]-P10[1])**2+(P5[2]-P10[2])**2)**0.5

MODULO5.append(mod56); MODULO5.append(mod57); MODULO5.append(mod58)
MODULO5.append(mod59); MODULO5.append(mod50)

min_modulo5=min(MODULO5)
pos5=MODULO5.index(min_modulo5)

# Dejando fijo el P6
MODULO6=[]
mod67=((P6[0]-P7[0])**2+(P6[1]-P7[1])**2+(P6[2]-P7[2])**2)**0.5
mod68=((P6[0]-P8[0])**2+(P6[1]-P8[1])**2+(P6[2]-P8[2])**2)**0.5
mod69=((P6[0]-P9[0])**2+(P6[1]-P9[1])**2+(P6[2]-P9[2])**2)**0.5
mod60=((P6[0]-P10[0])**2+(P6[1]-P10[1])**2+(P6[2]-P10[2])**2)**0.5

MODULO6.append(mod67); MODULO6.append(mod68); MODULO6.append(mod69)
MODULO6.append(mod60)

min_modulo6=min(MODULO6)
pos6=MODULO6.index(min_modulo6)

# Dejando fijo el P7
MODULO7=[]
mod78=((P7[0]-P8[0])**2+(P7[1]-P8[1])**2+(P7[2]-P8[2])**2)**0.5
mod79=((P7[0]-P9[0])**2+(P7[1]-P9[1])**2+(P7[2]-P9[2])**2)**0.5
mod70=((P7[0]-P10[0])**2+(P7[1]-P10[1])**2+(P7[2]-P10[2])**2)**0.5

MODULO7.append(mod78); MODULO7.append(mod79); MODULO7.append(mod70)
min_modulo7=min(MODULO7)
pos7=MODULO7.index(min_modulo7)

# Dejando fijo el P8
MODULO8=[]
mod89=((P8[0]-P9[0])**2+(P8[1]-P9[1])**2+(P8[2]-P9[2])**2)**0.5
mod80=((P8[0]-P10[0])**2+(P8[1]-P10[1])**2+(P8[2]-P10[2])**2)**0.5

MODULO8.append(mod89); MODULO8.append(mod80)
min_modulo8=min(MODULO8)
pos8=MODULO8.index(min_modulo8)

# Dejando fijo el P9
MODULO9=[]
mod90=((P9[0]-P10[0])**2+(P9[1]-P10[1])**2+(P9[2]-P10[2])**2)**0.5

MODULO9.append(mod90)
min_modulo9=min(MODULO9)
pos9=MODULO9.index(min_modulo9)


pos.append(P1); pos.append(P2); pos.append(P3); pos.append(P4)
min_mod.append(min_modulo1); min_mod.append(min_modulo2); min_mod.append(min_modulo3)
min_mod.append(min_modulo4); min_mod.append(min_modulo5); min_mod.append(min_modulo6)
min_mod.append(min_modulo7); min_mod.append(min_modulo8); min_mod.append(min_modulo9)

min_final=min(min_mod) #Distancia más corta comparando todos los puntos
min_final_pos=min_mod.index(min_final) # Posición en vector de modulos minimos

# Identificación de los puntos (manualmente se verifico que MODULOi fue)
pos_vec_min=min_final_pos+1

if pos_vec_min==4: 
 if MODULO4[0]==min_final:
    parCercano = "P4-P5" 
 elif MODULO4[1]==min_final:
    parCercano = "P4-P6" 
 elif MODULO4[2]==min_final:
    parCercano = "P4-P7"
elif MODULO4[3]==min_final:
    parCercano = "P4-P8"
elif MODULO4[4]==min_final:
    parCercano = "P4-P9"
elif MODULO4[5]==min_final:
    parCercano = "P4-P10"
    
print('----Par de puntos más cercano-----',parCercano)


#----------------------------------------------------------------------------

# Cree las siguientes listas utilizando el ciclo while: 

# lista1 = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]

print
cont2=0
lista1=[]
num=1
num2=-1
while True:
   lista1.append(num)
   lista1.append(num2)
   cont2+=1
   if cont2==13:
    break

# lista2 = [100, -1, 99, -1, 98, -1, 97, -1, 96, -1, ... 3, -1, 2, -1, 1, -1]

lista2=[]
num=100
num2=-1
lista2.append(num)
lista2.append(num2)

while True:
    num+=-1
    lista2.append(num)
    lista2.append(num2)
    if num==1:
        break

# lista3 = [2, 4, 5, 6, 8, 10,12, 14,15, 16,18, 20, 22, 24, 25 ... 592, 594, 595 ,596 ,598, 600]

lista3=[]
num=2
num2=4
lista=[]
lista3.append(num)
lista.append(num2)
while True: 
    num2+=10
    lista.append(num2)

    if num2==604:
        break

cont=-1
cont2=0

while True:
    num+=2
    lista3.append(num)
    
    if num==lista[cont2]:
        lista3.append(num+1)
        cont2+=1
    elif num==600:
        break


listaDeListas=[]
listaDeListas.append(lista1)
listaDeListas.append(lista2)
listaDeListas.append(lista3)

print('-----Lista de listas----',listaDeListas)

# Después de lograr los listados, almacenelos de la siguiente manera:
# listaDeListas = [lista1, lista2, lista3]

# -----------------------------------------------------------------------------------

MP=[1.0,1.1,2.3,1.1]
MG=[3.1,3.1,1.2,3.0]
JN=[5.0,4.0,2.5,5.0]
AL=[3.1,1.0,2.6,1.0]
CS=[3.1,4.0,1.1,3.0]
MR=[5.0,5.0,5.0,3.9]
EQ=[3.4,4.0,2.6,3.2]
JQ=[2.0,2.2,2.1,4.2]
ML=[3.7,4.1,4.7,4.0]
AG=[4.1,4.7,4.4,5.0]
CR=[5.0,5.0,1.0,3.2]
MV=[5.0,4.2,2.1,5.0]
ER=[3.2,4.1,2.2,3.3]

notas=range(0,6,1)
p_MP=[]
p_MG=[]
p_JN=[]
p_AL=[]
p_CS=[]
p_MR=[]
p_EQ=[]
p_JQ=[]
p_ML=[]
p_AG=[]
p_CR=[]
p_MV=[]
p_ER=[]
Mnota=[]
promedios=[]
end=[]
peornota=[]
cont=0
for i in notas:
    p1=MP[0]*0.1+MP[1]*0.2+MP[2]*0.15+MP[3]*0.20+i*0.35
    p2=MG[0]*0.1+MG[1]*0.2+MG[2]*0.15+MG[3]*0.20+i*0.35
    p3=JN[0]*0.1+JN[1]*0.2+JN[2]*0.15+JN[3]*0.20+i*0.35
    p4=AL[0]*0.1+AL[1]*0.2+AL[2]*0.15+AL[3]*0.20+i*0.35
    p5=CS[0]*0.1+CS[1]*0.2+CS[2]*0.15+CS[3]*0.20+i*0.35
    p6=MR[0]*0.1+MR[1]*0.2+MR[2]*0.15+MR[3]*0.20+i*0.35
    p7=EQ[0]*0.1+EQ[1]*0.2+EQ[2]*0.15+EQ[3]*0.20+i*0.35
    p8=JQ[0]*0.1+JQ[1]*0.2+JQ[2]*0.15+JQ[3]*0.20+i*0.35
    p9=ML[0]*0.1+ML[1]*0.2+ML[2]*0.15+ML[3]*0.20+i*0.35
    p10=AG[0]*0.1+AG[1]*0.2+AG[2]*0.15+AG[3]*0.20+i*0.35
    p11=CR[0]*0.1+CR[1]*0.2+CR[2]*0.15+CR[3]*0.20+i*0.35
    p12=MV[0]*0.1+MV[1]*0.2+MV[2]*0.15+MV[3]*0.20+i*0.35
    p13=ER[0]*0.1+ER[1]*0.2+ER[2]*0.15+ER[3]*0.20+i*0.35

    p_MP.append(p1)
    p_MG.append(p2)
    p_JN.append(p3)
    p_AL.append(p4)
    p_CS.append(p5)
    p_MR.append(p6)
    p_EQ.append(p7)
    p_JQ.append(p8)
    p_ML.append(p9)
    p_AG.append(p10)
    p_CR.append(p11)
    p_MV.append(p12)
    p_ER.append(p13)

Cantidad_con_posibilidades=0

for i in range(0,6,1):
    while p_MP[i]>3:
        cont+=1
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_MG[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_JN[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_AL[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_CS[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1
        
cont=0
for i in range(0,6,1):
    while p_MR[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_EQ[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1


cont=0
for i in range(0,6,1):
    while p_JQ[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_ML[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_AG[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_CR[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_MV[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1

cont=0
for i in range(0,6,1):
    while p_ER[i]>3 and i==5:
        cont+=1
        break
    if cont!=0:
        Cantidad_con_posibilidades+=1


if p_MP[5]<3:
    peornota.append(p_MP[5])
elif p_MP[0]>=3: 
    Mnota.append(p_MP)


if p_MG[5]<3:
    peornota.append(p_MG[5])
elif  p_MG[0]>=3:
    Mnota.append(p_MG[0])


if p_JN[5]<3:
    peornota.append(p_JN[5])
elif p_JN[0]>=3:
    Mnota.append(p_JN[0])


if p_AL[5]<3:
    peornota.append(p_AL[5])
elif  p_AL[0]>=3:
    Mnota.append(p_AL[0])
    

if p_CS[5]<3:
    peornota.append(p_CS[5])
elif  p_CS[0]>=3:
    Mnota.append(p_CS[0])

    
if p_MR[5]<3:
    peornota.append(p_MR[5])
elif  p_MR[0]>=3:
    Mnota.append(p_MR[0])
  
if p_EQ[5]<3:
    peornota.append(p_EQ[5])
elif  p_EQ[0]>=3:
    Mnota.append(p_EQ[0])

   
if p_JQ[5]<3:
    peornota.append(p_JQ[5])
if  p_JQ[0]>=3:
    Mnota.append(p_JQ[0])

  
if p_ML[5]<3:
    peornota.append(p_ML[5])
if  p_ML[0]>=3:
    Mnota.append(p_ML[0])


if p_AG[5]<3:
    peornota.append(p_AG[5])
elif  p_AG[0]>=3:
    Mnota.append(p_AG[0])


if p_CR[5]<3:
    peornota.append(p_CR[5])
elif  p_CR[0]>=3:
    Mnota.append(p_CR[0])
 

if p_MV[5]<3:
    peornota.append(p_MV[5])
elif  p_MV[0]>=3:
    Mnota.append(p_MV[0])
  
if p_ER[5]<3:
    peornota.append(p_ER[5])
elif  p_ER[0]>=3:
    Mnota.append(p_ER[0])

Cantidad_que_pierden=len(peornota)
Cantidad_que_ganan=len(Mnota)

estudiantes=[]
estudiantes.append(Cantidad_que_pierden)
estudiantes.append(Cantidad_que_ganan)
estudiantes.append(Cantidad_con_posibilidades)

print('-----estudiantes-----',estudiantes)

# -------------------------------------------------------------


# IDA
J=[1,1,1,1,0]
C=[1,0,1,0,1]
JO=[1,0,1,1,0]
M=[1,1,1,0,0]
E=[1,0,0,1,1]
A=[1,0,1,0,0]

cuota_personal=15000/6
C_J=0
C_C=0
C_JO=0
C_M=0
C_E=0
C_A=0

C_J1=0
C_C1=0
C_JO1=0
C_M1=0
C_E1=0
C_A1=0

for i in J:
    if i==1:
        C_J+=cuota_personal

for i in C:
    if i==1:
        C_C+=cuota_personal

for i in JO:
    if i==1:
        C_JO+=cuota_personal

for i in M:
    if i==1:
        C_M+=cuota_personal

for i in E:
    if i==1:
        C_E+=cuota_personal

for i in A:
    if i==1:
        C_A+=cuota_personal

# REGRESO

J1=[1,1,1,0,0]
C1=[1,0,0,0,0]
JO1=[1,0,1,1,0]
M1=[0,0,1,0,0]
E1=[0,0,0,1,0]
A1=[1,0,1,0,0]

for i in J1:
    if i==1:
        C_J1+=cuota_personal

for i in C1:
    if i==1:
        C_C1+=cuota_personal

for i in JO1:
    if i==1:
        C_JO1+=cuota_personal

for i in M1:
    if i==1:
        C_M1+=cuota_personal

for i in E1:
    if i==1:
        C_E1+=cuota_personal

for i in A1:
    if i==1:
        C_A1+=cuota_personal
        
J_F=C_J+C_J1+10000/6
C_F=C_C+C_C1+10000/6
JO_F=C_JO+C_JO1+10000/6
M_F=C_M+C_M1+10000/6
E_F=C_E+C_E1+10000/6
A_F=C_A+C_A1+10000/6

diccionarioPagos={'JUAN':J_F,'CAMILA':C_F,'JOSE':JO_F,'MARIA':M_F,'ESTEBAN':E_F,'ANGIE':A_F}
print('--------pagos-------',diccionarioPagos)


#-------------------------------------------------------------------------------

E001=[20,22,30,2,40,20,3]
E002=[31,14,32,15,13,20,11]
E010=[24,32,40,9,12,50,13]
E020=[42,12,33,24,22,32,23]
E021=[51,21,25,10,19,14,2]
E022=[22,31,51,21,35,15,11]
E023=[21,36,22,32,39,32,15]
E024=[22,33,41,21,43,31,36]
pagos=[]
pagos1=[]

P_E001=1200000+1200000*0.1+1200000*0.05+E001[0]*(50000)*0.05+E001[1]*70000*0.04+E001[2]*40000*0.06+E001[3]*25000*0.07+E001[4]*35000*0.05+E001[5]*80000*0.03+E001[6]*95000*0.02
P_E002=1200000+1200000*0.1+1200000*0.05+E002[0]*(50000)*0.05+E002[1]*70000*0.04+E002[2]*40000*0.06+E002[3]*25000*0.07+E002[4]*35000*0.05+E002[5]*80000*0.03+E002[6]*95000*0.02
P_E010=1200000+1200000*0.1+1200000*0.05+E010[0]*(50000)*0.05+E010[1]*70000*0.04+E010[2]*40000*0.06+E010[3]*25000*0.07+E010[4]*35000*0.05+E010[5]*80000*0.03+E010[6]*95000*0.02
P_E020=1200000+1200000*0.1+1200000*0.05+E020[0]*(50000)*0.05+E020[1]*70000*0.04+E020[2]*40000*0.06+E020[3]*25000*0.07+E020[4]*35000*0.05+E020[5]*80000*0.03+E020[6]*95000*0.02
P_E021=1200000+1200000*0.1+1200000*0.05+E021[0]*(50000)*0.05+E021[1]*70000*0.04+E021[2]*40000*0.06+E021[3]*25000*0.07+E021[4]*35000*0.05+E021[5]*80000*0.03+E021[6]*95000*0.02
P_E022=1200000+1200000*0.1+1200000*0.05+E022[0]*(50000)*0.05+E022[1]*70000*0.04+E022[2]*40000*0.06+E022[3]*25000*0.07+E022[4]*35000*0.05+E022[5]*80000*0.03+E022[6]*95000*0.02
P_E023=1200000+1200000*0.1+1200000*0.05+E023[0]*(50000)*0.05+E023[1]*70000*0.04+E023[2]*40000*0.06+E023[3]*25000*0.07+E023[4]*35000*0.05+E023[5]*80000*0.03+E023[6]*95000*0.02
P_E024=1200000+1200000*0.1+1200000*0.05+E024[0]*(50000)*0.05+E024[1]*70000*0.04+E024[2]*40000*0.06+E024[3]*25000*0.07+E024[4]*35000*0.05+E024[5]*80000*0.03+E024[6]*95000*0.02

pagos.append(P_E001); pagos.append(P_E002)
pagos.append(P_E010); pagos.append(P_E020)
pagos.append(P_E021); pagos.append(P_E022)
pagos.append(P_E023); pagos.append(P_E024)

pagos1.append(P_E001); pagos1.append(P_E002)
pagos1.append(P_E010); pagos1.append(P_E020)
pagos1.append(P_E021); pagos1.append(P_E022)
pagos1.append(P_E023); pagos1.append(P_E024)

pago_max1=max(pagos1)
pos_1=pagos1.index(pago_max1)
pagos1.remove(pago_max1)


pago_max2=max(pagos1)
pos_2=pagos1.index(pago_max2)
pagos1.remove(pago_max2)

pago_max3=max(pagos1)
pos_3=pagos1.index(pago_max3)

codigosAltosSalarios=[]
#Primer empleado

if pago_max1==pagos[0] or pago_max2==pagos[0] or pago_max3==pagos[0]:
    codigosAltosSalarios.append('E001')
    
if pago_max1==pagos[1] or pago_max2==pagos[1] or pago_max3==pagos[1]:
    codigosAltosSalarios.append('E002')

if pago_max1==pagos[2] or pago_max2==pagos[2] or pago_max3==pagos[2]:
    codigosAltosSalarios.append('E010')

if pago_max1==pagos[3] or pago_max2==pagos[3] or pago_max3==pagos[3]:
    codigosAltosSalarios.append('E020')

if pago_max1==pagos[4] or pago_max2==pagos[4] or pago_max3==pagos[4]:
    codigosAltosSalarios.append('E021')

if pago_max1==pagos[5] or pago_max2==pagos[5] or pago_max3==pagos[5]:
    codigosAltosSalarios.append('E022')

if pago_max1==pagos[6] or pago_max2==pagos[6] or pago_max3==pagos[6]:
    codigosAltosSalarios.append('E023')

if pago_max1==pagos[7] or pago_max2==pagos[6] or pago_max3==pagos[6]:
    codigosAltosSalarios.append('E024')


print('----codigosAltosSalarios----',codigosAltosSalarios)
