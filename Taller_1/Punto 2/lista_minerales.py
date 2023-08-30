# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:30:13 2023

@author: jd.vasquezh
"""
from minerales import Mineral

print("Se van a almacenar la información de los minerales en objetos de la clase Mineral.\n")
archivo = open("./minerales.txt", "r", encoding="utf8")
minerales = []
for linea in archivo.readlines():
    linea = linea[:-1]
    linea = linea.split("\t")
    if linea[0] != "nombre":
        mineral_i = Mineral(linea[0], float(linea[1]), linea[5], bool(linea[2]), linea[3], linea[4], linea[7], float(linea[6]))
        minerales.append(mineral_i)
archivo.close()
print("Se han almacenado los datos de la lista en", len(minerales),"objetos de la clase Mineral.\n")

print("="*35+"\nCálculo de minerales silicatos\n"+"="*35)
print("Se va a calcular el número de minerales silicatos de la lista de minerales.\n")
silicatos = 0
for mineral in minerales:
    if mineral.es_silicato():
        silicatos += 1
print("Se han encontrado",silicatos,"silicatos en la lista de minerales.\n")

print("="*35+"\nCálculo de densidad promedio de minerales\n"+"="*35)
print("Se va a calcular la densidad promedio de los minerales en la lista.\n")
densidad_total = 0
for mineral in minerales:
    densidad_total += mineral.calcular_densidad()
densidad_promedio = round(densidad_total/len(minerales),2)
print("Se ha calculado la densidad promedio en",densidad_promedio,"kg/m^3.")