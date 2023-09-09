import matplotlib.pyplot as plt
from expansiontermicamineral import ExpansionTermicaMineral
from lista_minerales import minerales

olivina = minerales[14]
grafito = minerales[0]

olivinaETM = ExpansionTermicaMineral(olivina.nombre, olivina.dureza, olivina.lustre,
                                     olivina.rompimiento_por_fractura, olivina.color, olivina.composicion,
                                     olivina.sistema_cristalino, olivina.specific_gravity, "olivine_angel_2017.csv")
coeficiente_expansion, fig = olivinaETM.calcular_coeficiente_expansion_termica()
print("\n"+"="*35+"\nCálculo de Coeficiente de expansión del Olivino\n"+"="*35)
print("\nSe ha calculado el coeficiente de expansión del olivino a una temperatura de",olivinaETM.lista_temperatura[0],"°C.")
print("\u03B1"+"("+str(olivinaETM.lista_temperatura[0])+"°C) = "+str(coeficiente_expansion)+".")

plt.savefig("Coeficiente_Expansion_Olivina.png",figure=fig)

grafitoETM = ExpansionTermicaMineral(grafito.nombre, grafito.dureza, grafito.lustre,
                                     grafito.rompimiento_por_fractura, grafito.color, grafito.composicion,
                                     grafito.sistema_cristalino, grafito.specific_gravity, "graphite_mceligot_2016.csv")
coeficiente_expansion, fig = grafitoETM.calcular_coeficiente_expansion_termica()
print("\n"+"="*35+"\nCálculo de Coeficiente de expansión del Grafito\n"+"="*35)
print("\nSe ha calculado el coeficiente de expansión del grafito a una temperatura de",grafitoETM.lista_temperatura[0],"°C.")
print("\u03B1"+"("+str(grafitoETM.lista_temperatura[0])+"°C) = "+str(coeficiente_expansion)+".")

plt.savefig("Coeficiente_Expansion_Grafito.png",figure=fig)