import os

class Arquitecturas(str): ...
class Capa(str): ...

os.system("cls")

arquitecturas_estandar_de_red: dict[ Arquitecturas, list[Capa]] = {
    "TCP/IP" : [
        "Capa de acesso a la red",
        "capa de internet", 
        "Capa de transporte",
        "Capa de aplicación"
    ],

    "OSI" : [
        "Capa de enlace de datos",
        "capa de red",
        "Capa de transporte",
        "Capa de sesión",
        " Capa de presentación",
        "Capa de aplicación"
    ]
}

print("las arquitecturas estandares de red son: ")
for arquitectura in arquitecturas_estandar_de_red.keys():
    print(arquitectura)


for arquitectura in arquitecturas_estandar_de_red.keys():
    print(f"\nLas capas de la arquitectura {arquitectura} son: ")
    for capa in arquitecturas_estandar_de_red[arquitectura]:
        print(capa)