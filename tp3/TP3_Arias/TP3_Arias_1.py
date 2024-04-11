import time
import serial
import matplotlib.pyplot as pl
import numpy as np


# Script calculadora
def calculadora(eleccion):
    match eleccion:
        case 1:
            a, b = ingreso_numeros()
            return a + b
        case 2:
            a, b = ingreso_numeros()
            return a - b
        case 3:
            a, b = ingreso_numeros()
            return a * b
        case 4:
            a, b = ingreso_numeros()
            if b != 0:
                return a/b
            else:
                return None
        case 5:
            return iterativo()
        case 6:
            return producto_punto()


# Ingresa desde el teclado y verifica si es float
def input_float():
    flotante = 0
    is_float = False
    while not is_float:
        try:
            flotante = float(input())
            is_float = True
        except ValueError:
            print('No es un número')
    return flotante


# ingreso números
def ingreso_numeros():
    is_float = False
    nro1 = 0
    nro2 = 0
    while not is_float:
        try:
            nro1 = float(input('Seleccione el primer número: '))
            is_float = True
        except ValueError:
            print('No es un número')

    is_float = False
    while not is_float:
        try:
            nro2 = float(input('Seleccione el segundo número: '))
            is_float = True
        except ValueError:
            print('No es un número')
    return nro1, nro2


# menu
def opcion():
    variable_eleccion = 'x'
    while variable_eleccion not in range(1, 7):
        variable_eleccion = int(input('''Calculadora:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Iterativo
6. Producto punto
    Respuesta: '''))
    return variable_eleccion


def producto_punto():
    eleccion_producto = 'x'
    while eleccion_producto not in ['v', 'm']:
        eleccion_producto = input('Seleccione \'V\' para vectores o \'M\' para matrices: ').lower()
    if eleccion_producto == 'v':
        return producto_punto_vectores()
    else:
        return producto_punto_matrices()


def producto_punto_vectores():
    coinciden_dimensiones = False
    largo_1 = 'x'
    largo_2 = 'x'
    while not coinciden_dimensiones:
        print('Primer vector:')
        while not largo_1.isdigit():
            largo_1 = input('\tSeleccione el largo del vector: ')
        largo_1 = int(largo_1)

        print('Segundo vector:')
        while not largo_2.isdigit():
            largo_2 = input('\tSeleccione el largo del vector: ')
        largo_2 = int(largo_2)

        if largo_1 == largo_2 > 0:
            coinciden_dimensiones = True
        else:
            largo_1 = 'x'
            largo_2 = 'x'
            print('\nLos largos deben coincidir y ser de un valor entero mayor a 0.\n')

    print('Primer vector:')
    vector_1 = []
    for x in range(0, largo_1):
        print(f'Seleccione el elemento [{x+1}]:')
        vector_1.append(input_float())
    vector_1 = np.array(vector_1)

    print('\nSegundo vector:')
    vector_2 = []
    for x in range(0, largo_1):
        print(f'Seleccione el elemento [{x+1}]:')
        vector_2.append(input_float())
    vector_2 = np.array(vector_2)

    print(vector_1)
    print(vector_2)
    return np.dot(vector_1, vector_2)


def producto_punto_matrices():
    coinciden_dimensiones = False
    filas_1 = 'x'
    columnas_1 = 'x'
    filas_2 = 'x'
    columnas_2 = 'x'
    while not coinciden_dimensiones:
        print('Primer arreglo:')
        while not filas_1.isdigit():
            filas_1 = input('\tSeleccione la cantidad de filas: ')
        while not columnas_1.isdigit():
            columnas_1 = input('\tSeleccione la cantidad de columnas: ')
        filas_1 = int(filas_1)
        columnas_1 = int(columnas_1)

        print('\nSegundo arreglo:')
        while not filas_2.isdigit():
            filas_2 = input('\tSeleccione la cantidad de filas: ')
        while not columnas_2.isdigit():
            columnas_2 = input('\tSeleccione la cantidad de columnas: ')
        filas_2 = int(filas_2)
        columnas_2 = int(columnas_2)

        if filas_1 == columnas_2 > 0 and filas_2 == columnas_1 > 0:
            coinciden_dimensiones = True
        else:
            filas_1 = 'x'
            columnas_1 = 'x'
            filas_2 = 'x'
            columnas_2 = 'x'
            print('\nLas dimensiones deben coincidir y ser de un valor entero mayor a 0.\n')

    print('Primer arreglo:')
    matriz_1 = np.empty([filas_1, columnas_1])
    for fil in range(0, filas_1):
        for col in range(0, columnas_1):
            print(f'Seleccione el elemento fila[{fil+1}] columna[{col+1}]:')
            matriz_1[fil, col] = input_float()

    print('Segundo arreglo:')
    matriz_2 = np.empty([filas_2, columnas_2])
    for fil in range(0, filas_2):
        for col in range(0, columnas_2):
            print(f'Seleccione el elemento fila[{fil+1}] columna[{col+1}]:')
            matriz_2[fil, col] = input_float()

    print(matriz_1)
    print(matriz_2)
    return np.dot(matriz_1, matriz_2)


def iterativo():
    inciso = 'x'
    step = 'x'
    iterar = 'x'
    while inciso not in ['a', 'b', 'c']:
        inciso = input('''Seleccione la manera de iterar:
    a) Sumar
    b) Restar
    c) Multiplicar
            Respuesta: ''')
    while not step.isdigit():
        step = input('Seleccione el paso: ')
    while not iterar.isdigit():
        iterar = input('Seleccione el número de veces a iterar: ')
    step = int(step)
    iterar = int(iterar)
    match inciso:
        case 'a':
            resultado = 0
            for x in range(0, iterar):
                resultado += step
            return resultado
        case 'b':
            resultado = 0
            for x in range(0, iterar):
                resultado -= step
            return resultado
        case 'c':
            resultado = 1
            for x in range(0, iterar):
                resultado *= step
            return resultado

def script_calculadora():
    salir = False
    print('Bienvenido a la calculadora\n')
    while not salir:
        print(f'El resultado es {calculadora(opcion())}')
        respuesta_continuar = 'x'
        while respuesta_continuar not in ['s', 'n']:
            respuesta_continuar = input('\nPara continuar presione "S", sino presione "N": ').lower()
        if respuesta_continuar == 'n':
            salir = True

    print('\n' + 20*'*' + '\nGracias por usar la calculadora\n' + 20*'*')

# Script graficos
def figPlot(x, y, row, col, joinVec, numplot, typeGraf, xlim, ylim, xlabel, ylabel, show=False):
    pl.figure(numplot)
    for i in range(0, len(joinVec)):
        # Verifico si el num para agrupar es solo un número o una tupla
        if len(joinVec[i]) == 1:
            pl.subplot(row, col, joinVec[i][0])
        else:
            pl.subplot(row, col, joinVec[i])

        # 'p' -> plot. 's' -> stem.
        if typeGraf[i] == 'p':
            pl.plot(x[i], y[i])
        elif typeGraf[i] == 's':
            pl.stem(x[i], y[i])

        # Verifico si el subgráfico está a la izquierda
        if (joinVec[i][0]-1)%col == 0:
            pl.ylabel(ylabel[i])

        # Verifico si el subgráfico está abajo
        if len(joinVec[i]) == 1:
            if joinVec[i][0] > ((row-1)*col):
                pl.xlabel(xlabel[i])
        else:
            if joinVec[i][1] > ((row-1)*col):
                pl.xlabel(xlabel[i])
        
        #pl.legend()
        
        pl.xlim(xlim[i][0], xlim[i][1])
        pl.ylim(ylim[i][0], ylim[i][1])
        pl.grid()

    if show:
        pl.show()



def graficar():
    numplot = 'x'
    while not numplot.isdigit():
        numplot = input('Indique el número del gráfico: ')
    numplot = int(numplot)

    numGraphs = 0
    while numGraphs <= 0:
        numGraphs = int(input('Ingrese la cantidad de subgráficos que quiere realizar: '))
    
    # Estilo y tipo de gráfico
    styleGraphs = []
    typeGraf = []
    # Límites
    xlim = []
    ylim = []
    # Vectores x e y
    x = []
    y = []
    # Labels
    xlabel = []
    ylabel = []
    for i in range(0, numGraphs):
        # Estilo y tipo de gráfico
        aux = 'x'
        while aux not in ['l', 'n', 'u',] or len(aux)>1:
            aux = input(f'''Seleccione el tipo de distribución, gráfico {i+1}:
                l: Laplace.
                n: Normal.
                u: Uniforme.
                    Elección: ''').lower()
        styleGraphs.append(aux)

        aux = 'x'
        while aux not in ['p', 's'] or len(aux)>1:
            aux = input(f'''Seleccione el tipo de gráfico, gráfico {i+1}:
                p: Plot.
                s: Stem.
                    Elección: ''').lower()
        typeGraf.append(aux)


        # Límites
        lim_correct = False
        lim_aux = []
        while not lim_correct:
            print(f'\nLímites del eje x, subgráfico {i+1}:')
            aux1 = float(input('Ingrese el límite inferior: '))
            aux2 = float(input('Ingrese el límite superior: '))
            if aux2 > aux1:
                lim_aux = [aux1, aux2]
                lim_correct = True
        xlim.append(lim_aux)

        aux_label = input(f'Ingrese el nombre para el eje x del subgráfico {i+1}: ')
        xlabel.append(aux_label)

        lim_correct = False
        lim_aux = []
        while not lim_correct:
            print(f'\nLímites del eje y, subgráfico {i+1}:')
            aux1 = float(input('Ingrese el límite inferior: '))
            aux2 = float(input('Ingrese el límite superior: '))
            if aux2 > aux1:
                lim_aux = [aux1, aux2]
                lim_correct = True
        ylim.append(lim_aux)


        aux_label = input(f'Ingrese el nombre para el eje y del subgráfico {i+1}:  ')
        ylabel.append(aux_label)

        # Asignación de vectores x e y según tipo de gráfico
        array_aux = np.arange(xlim[i][0],xlim[i][1],(xlim[i][1]-xlim[i][0])/50)
        x.append(array_aux)
        if styleGraphs[i] == 'l':
            mu = (xlim[i][1] + xlim[i][0])/2
            e_decay = 1
            array_aux = np.random.laplace(mu, e_decay, len(x[i]))
            y.append(array_aux)

        elif styleGraphs[i] == 'n':
            mu = (xlim[i][1] + xlim[i][0])/2
            sigma = 0.1
            array_aux = np.random.normal(mu, sigma, len(x[i]))
            y.append(array_aux)

        else:
            high_y = ylim[i][1]
            low_y = ylim[i][0]
            array_aux = np.random.uniform(low_y, (high_y+low_y)/2, len(x[i]))
            y.append(array_aux)

    row = 0
    col = 0
    while numGraphs > row*col:
        print(f'\nIngreso filas y columnas (tener en cuenta que se deben tener al menos {numGraphs} espacios.')
        row = int(input('Ingrese la cantidad de filas de subgráficos: '))
        col = int(input('Ingrese la cantidad de columnas de subgráficos: '))

    # spaceLeft representa la cantidad de espacios permitidos para un solo subgráfico.
    # Si este se supera, no entrarán los subgráficos restantes.
    spaceLeft = row*col - numGraphs + 1
    # rowGraphsUsed representa la cantidad de subgráficos o lugares utlizados en una misma fila.
    rowGraphsUsed = 0
    # graphSelect es la posición en la que estoy del gráfico.
    graphSelect = 1
    joinVec = []
    for i in range(0, numGraphs):
        print(f'\nSubgráfico número {i+1}:')

        # colSubLeft representa la cantidad de espacios que quedan en la fila para graficar
        colSubLeft = col - rowGraphsUsed

        # Elijo el menor entre colSubLeft o spaceLeft para establecer el límite
        if (colSubLeft < spaceLeft):
            colSubLim = colSubLeft
        else:
            colSubLim = spaceLeft
        colSub = 0
        while colSub > colSubLim or colSub <= 0:
            colSub = int(input(f'Elija columnas del subgráfico ({colSubLim} como máximo): '))


        # Creo variable auxiliar, para colocar en joinVec
        if colSub == 1:
            aux = (graphSelect, )
            joinVec.append(aux)
        else:
            aux = (graphSelect, graphSelect+(colSub-1))
            joinVec.append(aux)
            spaceLeft -= (colSub - 1)

        graphSelect += colSub

        rowGraphsUsed += colSub
        if rowGraphsUsed == col:
            rowGraphsUsed = 0

    show = 'x'
    while show not in ['s', 'n']:
        show = input('\nSi desea mostrar el gráfico, presione "S", sino "N": ').lower()
    show = True if (show == 's') else False

    figPlot(x, y, row, col, joinVec, numplot, typeGraf, xlim, ylim, xlabel, ylabel, show)



#############################################
# Nota:
# Comentar esta linea si se utiliza el puerto serie
# con la FPGA
ser = serial.serial_for_url('loop://', timeout=1)

#############################################
# Nota:
# Descomentar esta linea si se utiliza el puerto serie
# con la FPGA
#############################################
# ser = serial.Serial(
#     port     = '/dev/ttyUSB1',
#     baudrate = 9600,
#     parity   = serial.PARITY_NONE,
#     stopbits = serial.STOPBITS_ONE,
#     bytesize = serial.EIGHTBITS
# )

ser.isOpen()
ser.timeout=None
ser.flushInput()
ser.flushOutput()

while 1 :
    char_v = []
    data = input('''Ingrese un comando:
    1: Ejecuta el script calculadora.
    2: Ejecuta el script de gráficos.
    exit: Finaliza el programa.
        Respuesta:''')
    if data == 'exit':
        if ser.isOpen():
            ser.close()
        break
    else:
        ser.write(data.encode())
        #time.sleep(2)
        out = ''
        #print("Info: ",ser.inWaiting())
        while ser.inWaiting() > 0:
            read_data = ser.read(1)
            #print(read_data)
            out += read_data.decode()
            #print("Info: ",ser.inWaiting())
        if out != '':
            print(">> " + out)
            if out == '1':
                script_calculadora()
                break     
            elif out == '2':
                graficar()
                break
               
            ''' Se utiliza un break al final de cada llamada a las funciones para terminar el script.
            Es decir, este script simplemente funciona una sola vez que se ingresa un valor CORRECTO.
            Los valores correctos son "1", "2", y "exit", en caso contrario se vuelve a pedir un valor.
            Si se quisiera seguir ejecutando el código, aunque finalice el script calculadora o graficar,
            se debería quitar los "break" simplemente. De esta manera, solo se terminará el script con un 
            "exit".'''