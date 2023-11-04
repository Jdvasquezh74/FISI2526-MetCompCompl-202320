import numpy as np

#Algoritmo de multiplicación de matrices

def multiplicacion_matricial(A,B):
    filasA = np.shape(A)[0]
    columnasA = np.shape(A)[1]
    filasB = np.shape(B)[0]
    columnasB = np.shape(B)[1]
    if columnasA !=  filasB:
        print("Las matrices a multiplicar son:")
        print("A\n", A)
        print("B\n", B)
        print("Esta multiplicación es imposible!")
        print("El número de columnas de la matriz A y el número de filas de la matriz B debe ser igual!") 
    else:
        print("Las matrices a multiplicar son:")
        print("A\n", A)
        print("B\n", B)
        C = np.zeros((filasA, columnasB))
        for i in range(filasA):
            for j in range((columnasB)):
                for k in range(columnasA):
                    C[i][j] = C[i][j] + A[i][k]*B[k][j]
        print("La matriz resultante de la multiplicación matricial es:")
        print("C\n",C)

#Punto 1 - Parte 1
#Literal a
print("Punto 1 - Parte 1\n")
print("Literal a\n")
A = np.array([[5, -4, -2],[5, -5, 4],[2, 5, -4],[-5, 4, 3],[3, -4, -3]])
B = np.array([[5],[-2],[-3]])
multiplicacion_matricial(A,B)
input("Presione 'Enter' para continuar.")

#Literal b
print("\nLiteral b\n")
A = np.array([[0,-1,-1,3],[5,-5,-2,2],[1,0,4,5]])
B = np.array([[0,-3],[-2,-1],[3,-3]])
multiplicacion_matricial(A,B)
input("Presione 'Enter' para continuar.")

#Literal c
print("\nLiteral c\n")
A = np.array([[2,-5,5,1],[5,2,-7,-6],[-6,-1,7,-4],[5,4,1,-5]])
B = np.array([[0,4,-7,1,-6],[-1,-6,-5,1,1],[2,-1,-6,5,-5],[-3,-6,6,3,5]])
multiplicacion_matricial(A,B)
input("Presione 'Enter' para continuar.")

#Punto 1 - Parte 2
print("\nPunto 1 - Parte 2\n")
print("Ahora vamos a comprobar que la multiplicación matricial no es conmutativa")
A = np.array([[1,2],[3,4]])
B = np.array([[10,9],[8,7]])
print("\nMultiplicación A.B")
multiplicacion_matricial(A,B)
input("Presione 'Enter' para continuar.")
print("\nMultiplicación B.A")
multiplicacion_matricial(B,A)
input("Presione 'Enter' para continuar.")
print("Como se observa, son las mismas matrices y solo hemos invertido el orden, pero el resultado no es igual!")
print("De lo anterior, la multiplicación matricial NO es una operación conmutativa.")