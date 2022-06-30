import random
from clases.movimientos import movimiento_general,tipo_movimiento,movimiento_especifico
from clases.escenarios import Escenario
from clases.superheroes import superheroe, tipo_superheroe
from clases.organizaciones import organizacion

def main():

    firstNames = {"A":"Captain", "B":"Turbo", "C":"Galactic", "D":"The", "E":"Aqua", "F":"Fire",
    "G":"Iron", "H":"Super", "I":"Green", "J":"Phantom", "K":"Dark", "L":"Ghost", "M":"Professor",
    "N":"Atomic", "O":"Rock", "P":"Omega", "Q":"Rocket", "R":"Shadow", "S":"Agent", "T":"Silver",
    "U":"Wild", "V":"Wolf", "W":"Ultra", "X":"Wonder", "Y":"Doctor", "Z":"Star"}

    lastNames = {"A":"X", "B":"Shield", "C":"Machine", "D":"Justice", "E":"Beast", "F":"Wing",
    "G":"Arrow", "H":"Skull","I":"Blade", "J":"Bolt", "K":"Cobra", "L":"Blaze",
    "M":"Soldier", "N":"Strike", "O":"Falcon", "P":"Fang", "Q":"King", "R":"Surfer",
    "S":"Bot", "T":"Guard", "U":"Thing", "V":"Claw", "W":"Brain", "X":"Master", "Y":"Power", "Z":"Storm"}

    organizaciones=["A - Force", "Avengers", "Mercs for Money", "League of Realms", "Strange Academy", "X-Men"]

    print()
    print("!!!COMENZEMOS¡¡¡")
    print()

    #ELEGIR ESCENARIO
    x=input("Elige un escenario: torre_stark, santo_santuario, colegio_xavier: ")
    x=x.lower()
    escenario=Escenario.de_nombre(x)
    print()
    #CREAR LISTA SUPERHEROES
    nombres=list(firstNames.values())
    apellidos=list(lastNames.values())
    tipos=["humano","no_humano"]
    list_sup=[]

    for i in range(len(nombres)):
        nombre=nombres[i]
        apellido=apellidos[i]
        alias=nombre+""+apellido
        s=tipos[random.randint(0,1)]
        tipo=tipo_superheroe.de_nombre(s)
        sup=superheroe(i+1,alias,alias,tipo,escenario)
        list_sup.append(sup)

    list_costes=[]
    for i in list_sup:
        list_costes.append(i.get_coste())

    #CREAR ORGANIZACIONES
    r=len(list_sup)
    l=len(organizaciones)
    c=r/l
    #a=26, b=6, c=4.33 por tanto van a sobrar superheroes(en este caso habrá 3 superheroes por organizacion y sobraran 8)
    org_sup=[]
    print()
    print("<<< FORMACION DE LAS ORGANIZACIONES >>>")
    print()
    for i in range(len(organizaciones)):
        nombre=organizaciones[i]
        org=organizacion(nombre,[])
        print(f'Elige superheroes para la organizacion: {nombre}')
        print()
        while len(org.superheroes)<3:
            for j in range(len(list_sup)):
                print(f'{j} - {list_sup[j].__str__()}')
            x=int(input())
            org.set_superheroes(list_sup[x])
            list_sup.remove(list_sup[x])
        else:
            org_sup.append(org)
