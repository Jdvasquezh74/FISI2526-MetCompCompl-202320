# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:44:34 2023

@author: jd.vasquezh
"""
from minerales import Mineral
import numpy as np
import matplotlib.pyplot as plt

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
            temperaturas.append(float(temperatura))
            volumenes.append(float(volumen))
        archivo.close()
        self.lista_temperatura = np.array(temperaturas)
        self.lista_volumen = np.array(volumenes)
    
    def dVdT(self,t,h):
        if t+h < np.size(self.lista_volumen):
            return (self.lista_volumen[t+h] - self.lista_volumen[t])/(self.lista_temperatura[t+h] - self.lista_temperatura[t])
        else:
            return (self.lista_volumen[t] - self.lista_volumen[t-h])/(self.lista_temperatura[t] - self.lista_temperatura[t-h])
    
    def calcular_coeficiente_expansion_termica(self):
        coeficiente_expansion_termica = []
        for i in range(np.size(self.lista_temperatura)):
            coeficiente_expansion_termica.append((1/self.lista_volumen[i])*self.dVdT(i,1))
        fig = plt.figure(figsize=(10,8))
        plt.plot(self.lista_volumen,coeficiente_expansion_termica, figure=fig)
        plt.title(r"$\alpha$"+"(T) vs. V(T) " + self.nombre, figure=fig)
        plt.xlabel("Volumen (cc)", figure=fig)
        plt.ylabel("Coeficiente de expasión térmica", figure=fig)
        return coeficiente_expansion_termica[0], fig

        
        
        
        