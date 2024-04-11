import numpy as np

def iterativo(step, iter, op):
    resultado = 0
    if(op == 'c'):
        resultado = 1   #elemento neutro para la multiplicacion
    for i in range(iter):
        if(op == 'a'):
           resultado = resultado + step    
        if(op == 'b'):
            resultado = resultado - step    
        if(op == 'c'):
            resultado = resultado * step    
    return resultado

def ingresoMatrices():
    while True:
        print("Ingrese los elementos de cada fila separados por espacios, y las filas separadas por ';' ")
        m1 = input("Ingrese los elementos la primera matriz\n")
        m1 = np.matrix(m1)
        m2 = input("Ingrese los elementos la segunda matriz\n")
        m2 = np.matrix(m2)

        cols_m1 = np.shape(m1)[1]
        filas_m2 = np.shape(m2)[0]
        if(filas_m2 == cols_m1):
            break
        print("Tamaño de matrices incompatible")
    
    return m1, m2 


while True:
    while True:
        print("Seleccionar operación deseada")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Iterativo")
        print("  a) Sumar")
        print("  b) Restar")
        print("  c) Multiplicar")
        print("6. Producto punto")

        opcion = input("Ingrese la opción\n")
        if(int(opcion[0]) > 0 and int(opcion[0]) < 7):
            break
        print("Opción inválida")
    
    if(opcion == '6'):
        op1, op2 = ingresoMatrices()
    else:
        if(opcion[0] == '5'):
            operandos = input("Ingrese el paso y el numero de veces que se repetirá separados por un espacio\n")
        else:
            operandos = input("Ingrese los 2 operandos separados por un espacio\n")
        
        operandos = operandos.split()
        op1 = int(operandos[0])
        op2 = int(operandos[1])
            
    
# print(op1, op2)

    match opcion[0]:
        case '1': 
            resultado = op1 + op2
        case '2': 
            resultado = op1 - op2
        case '3': 
            resultado = op1 * op2
        case '4': 
            resultado = op1 / op2
        case '5': 
            resultado = iterativo(op1, op2, opcion[1])
        case '6': 
            resultado = np.dot(op1, op2)
        case _:
            resultado = None

    if(resultado is not None):
        print("El resultado es:\n",resultado)
    opcion = input("Desea continuar? [s/n]\n")
    if(opcion == 'n'):
        break
     