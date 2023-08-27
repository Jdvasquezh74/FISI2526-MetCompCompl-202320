# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


#Punto 1.3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

def datos_archivo(ruta:str)->list:

    lista = []

    archivo = open(ruta, "r",encoding="utf-8")
    leer = False



    while True:
        linea = archivo.readline()
        if(leer == True):
            if(("SPECS:" not in linea) and ("- type:" not in linea) and (linea != "")):
                linea = " ".join(linea.split())
                linea = linea.split(" ")
                tupla = (float(linea[0]), float(linea[1]))
                lista.append(tupla)
            else:
                break
        if("data: |" in linea):
            leer = True
    return lista

#Punto 1.4

def refraccion_esp()->None:
    datos_kapton = datos_archivo("Plásticos Comerciales/Kapton.yml")
    datos_noa1348 = datos_archivo("Adhesivos Ópticos/NOA1348.yml")

    kapton_l = []
    kapton_n = []
    noa_l = []
    noa_n = []

    for i in datos_kapton:
        kapton_l.append(i[0])
        kapton_n.append(i[1])
    for j in datos_noa1348:
        noa_l.append(j[0])
        noa_n.append(j[1])

    plt.figure(dpi=200)
    plt.plot(kapton_l, kapton_n)
    plt.title("Kapton, Promedio: {}, Desviación Estandar: {}".format(round(np.mean(kapton_n),2), round(np.std(kapton_n),2)))
    plt.xlabel("Longitud de onda")
    plt.ylabel("Indice de refracción")
    plt.grid()
    plt.show()

    plt.figure(dpi=200)
    plt.plot(noa_l, noa_n)
    plt.title("NOA1348, Promedio: {}, Desviación Estandar: {}".format(round(np.mean(noa_n),2), round(np.std(noa_n),2)))
    plt.xlabel("Longitud de onda")
    plt.ylabel("Indice de refracción")
    plt.grid()
    plt.show()


#Punto 1.5

def grafica_refraccion(datos_ruta:str)->None:

    datos = open(datos_ruta, 'r', encoding="utf-8")

    linea = datos.readline()

    while linea != "":
        linea = datos.readline()
        linea = linea.split(",")
        categoria = linea[0]
        material = linea[2]

        ruta_material = "{}/{}.yml".format(categoria, material)
        datos_material = datos_archivo(ruta_material)

        material_l = []
        material_n = []

        for i in datos_material:
            material_l.append(i[0])
            material_n.append(i[1])
        
        plt.figure(dpi=200)
        plt.plot(material_l, material_n)
        plt.title("{}, Promedio: {}, Desviación Estandar: {}".format(material, round(np.mean(material_n),2), round(np.std(material_n),2)))
        plt.xlabel("Longitud de onda")
        plt.ylabel("Indice de refracción")
        plt.grid()
        plt.savefig("{}/{}.png".format(categoria, material))

grafica_refraccion("indices_refraccion.csv")







