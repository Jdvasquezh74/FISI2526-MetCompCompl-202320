# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

class Mineral:
    
    def __init__(self, nombre: str, dureza: float, lustre: str, 
                 rompimiento_por_fractura: bool, color: str, composicion: str, sistema_cristalino: str, specific_gravity: float):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color 
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino 
        self.specific_gravity = specific_gravity
        
    def es_silicato(self)->bool:
        return "Si" in self.composicion and "O" in self.composicion
    
    def calcular_densidad(self)->float:
        return self.specific_gravity*1000
    
    def mostrar_color(self)->None:
        value = self.color
        value = value.lstrip('#')
        lv = len(value)
        value = tuple(int(value[i:i + lv // 3], 16)/255 for i in range(0, lv, lv // 3))
        plt.imshow([[value]])
    
    def mostrar_info_consola(self)->None:
        print("Nombre: " + self.nombre + "\n")
        print("Dureza:", self.dureza)
        print("Tipo de rompimiento:", self.rompimiento_por_fractura)
        print("Sistema de organización de átomos:", self.sistema_cristalino)
        print()
        