# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:44:34 2023

@author: jd.vasquezh
"""
from minerales import Mineral

class ExpansionTermicaMineral(Mineral):
    
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity, archivo_expansion_termica:str):
        
        Mineral.__init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity)
        
        self.archivo_expansion_termica = archivo_expansion_termica
        archivo = open("./"+self.archivo_expansion_termica, "r")
        temperaturas = []
        volumenes = []
        archivo.readline()
        for dato in archivo.readlines():
            temperatura, volumen = dato.split(",")
            temperaturas.append(temperatura)
            volumenes.append(volumen)
        archivo.close()
        self.lista_temperatura = temperaturas
        self.lista_volumen = volumenes
    
    def DerivadaCentral(f,x,h):
        d = 0.
        
        if h != 0:
            d = (f(x+h) - f(x-h))/(2*h)
            
        return d
        
        
        
        