
RecMario = (
(-0.5, -1.98),
(0.1, -1.98),
(0.1, -2.055),
(-0.5, -2.055)
)
MarioCambiosSilueta = (
#Izq, derecha y arriba
(-1,5,1),
(0,1,1),
(0,1,1),
(0,0,1),
(0,0,1),
(1,0,1),
(0,-1,1),
(-1,-1,1),
(-1,1,1),
(17,2,0),
(-18,1,1),
(0,0,1),
(0,0,1),
(0,0,1),
(1,-1,1),
(1,0,1),
(0,-1,1),
(1,-1,1),
(0,-1,1),
(1,-1,1),
(1,0,1),
(0,2,1),
(-4,1,1),
(-1,1,1),
(-1,1,1),
(0,1,1),
(0,1,1),
(0,0,1),
(-1,-1,1),
(0,-1,1),
(1,-1,1),
(1,0,1),
(1,2,1),
(0,1,1),
(1,0,1),
(1,-1,1),
(0,-2,1),
(1,-1,1),
(1,0,1),
(1,-1,1),
(1,-1,1),
(2,-1,1)
)

MarioCambiosRelleno = (
[
(2,-5)
],
[
(1,-5), (11,-1)
],
[
(1,-13),(3,-8),(8,-6),(11,-1)
],
[
(1,-14),(2,-7),(9,-6),(11,-3),(13,-1)
],
[
(1,-10),(6,-6),(11,-4),(12,-1)
],
[
(5,-8),(9,-1)
],
[
(1,-10),(4,-7)
],
[
(8,-1)
],
[
(1,-10),(7,-1)
],
[

]
)


ColoresMario = (
[
0
],
[
1,0
],
[
1,2,1,1
],
[
1,2,1,1,2
],
[
1,2,1,2
],
[
1,1
],
[
1,2
],
[
3
],
[
4,3
],
[

]
)


PaletaMario = (
#Suela
(213,182,64,255),
#Zapato1
(159,95,46,255),
#Zapato2
(195,116,59,255),
#RopaAzul
(52,65,240,255),
#Guante1
(221,221,221,255),
#Guante2
(254,254,254,255),
#Boton1
(229,191,100,255),
#Boton2
(253,223,101,255),
#RopaRoja
(212,7,7,255),
#Bigote1
(109,64,31,255),
#Bigote2
(159,95,47,255),
#Piel1
(229,215,188,255),
#Piel2
(254,239,208,255),
#Cabello1
(159,95,48,255),
#Cabello2
(189,116,61,255)
)


def Formar():
    Rectangulos = list()
    RectangulosRelleno = list()
    Rec = globals()['RecMario']
    Rellenos = globals()['MarioCambiosRelleno']
    Cambios = globals()['MarioCambiosSilueta']
    Rectangulos.append(Rec)
    i = 0
    for cambio in Cambios:
        Rec = (
        (Rec[0][0]+0.075*cambio[0],Rec[0][1]+0.075*cambio[2]),
        (Rec[1][0]+0.075*cambio[1],Rec[1][1]+0.075*cambio[2]),
        (Rec[2][0]+0.075*cambio[1],Rec[2][1]+0.075*cambio[2]),
        (Rec[3][0]+0.075*cambio[0],Rec[3][1]+0.075*cambio[2])
        )

        if(i<len(Rellenos)):
            rellenosAux = list()
            for relleno in Rellenos[i]:
                RecAux = Rec
                RecAux = (
                (RecAux[0][0]+0.075* relleno[0], RecAux[0][1]),
                (RecAux[1][0]+0.075* relleno[1], RecAux[1][1]),
                (RecAux[2][0]+0.075* relleno[1], RecAux[2][1]),
                (RecAux[3][0]+0.075* relleno[0], RecAux[3][1])
                )
                rellenosAux.append(RecAux)
            RectangulosRelleno.append(rellenosAux)
        i+=1
        Rectangulos.append(Rec)
    print(RectangulosRelleno)
    return (Rectangulos,RectangulosRelleno,  ColoresMario, PaletaMario)
