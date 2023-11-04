import numpy as np

#Algoritmo de eliminación Gaussiana
def eliminacion_gaussiana(A):
    dim = np.shape(A)[0]
    vec = np.zeros((dim))
    #Se lleva la matriz a su forma escalonada
    for j in range(dim + 1):
        for i in range(dim):
            if i > j:
                factor = A[i][j]/A[j][j]
                for k in range(dim + 1):
                    A[i][k] = A[i][k] - factor*A[j][k]
    #Se obtiene la solución obteniendo la forma escalonada reducida
    #La solución se almacena en un vector con la cantidad de incógnitas
    for i in np.arange(dim-1,-1,-1):
        suma = 0
        for j in np.arange(i,dim,1):
            suma += A[i][j]*vec[j]
        vec[i] = (A[i][dim]-suma)/A[i][i]
    return vec

#Punto 2
#Literal a
print("Punto 2")
print("Literal a")
print("El problema a resolver tiene su representación matricial como sigue:")
A = np.array([[3,1,-1,2],[1,-2,1,0],[4,-1,1,3]]).astype(np.float64)
print(A)
vec = eliminacion_gaussiana(A)
print("Las 3 fuerzas son F1 =",round(vec[0],4), "N, F2 = ",round(vec[1],4),"N y F3 =", round(vec[2],4), "N.")
input("Presione 'Enter' para continuar.")

#Literal b
print("\nLiteral b")
print("El problema a resolver tiene su representación matricial como sigue:")
A = np.array([[1,1,1,0],[0,-8,10,0],[4,-8,0,6]]).astype(np.float64)
print(A)
vec = eliminacion_gaussiana(A)
print("Las 3 corrientes son Ia =",round(vec[0],4), "A, Ib =",round(vec[1],4),"A e Ic =", round(vec[2],4), "A.")
