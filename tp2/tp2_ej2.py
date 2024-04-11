import numpy as np
import matplotlib.pyplot as pl

def figPlot(x, y, row, col, joinVec, numplot, show, typeGraf, xlim, ylim, xlabel, ylabel):
    pl.figure(figsize=[8,5], num = numplot)
    
    Nplots = len(x)     #la cantidad de plots es la cantidad de vectores que se reciben para graficar
     
    for plot in range(Nplots):
        pl.subplot(row,col,joinVec[plot])   
        if(typeGraf[plot] == 'plot'):
            pl.plot(x[plot], y[plot])
        elif(typeGraf[plot] == 'stem'):
            pl.stem(x[plot], y[plot])
        pl.xlim(xlim[plot])
        pl.ylim(ylim[plot])
        
        #chequear si el subplot está en el margen inferior o izquierdo
        k = np.arange(0,row)
        margen_izq = col*k+1   #1er vector columna (margen izquierdo) 
        if(joinVec[plot][0] in margen_izq):
            pl.ylabel(ylabel[plot])
        
        #si el primer elemento de joinVec esta en la ultima fila, el grafico es del margen inferior
        if(joinVec[plot][0] > col*(row-1)):
            pl.xlabel(xlabel[plot])
            
    if(show):
        pl.show()

def validarSubgrafico(lugares_ocupados, row, col, joinVec):
    #condiciones para agregar un subgrafico:
    cond1 = True   #Que no estén ya ocupados los lugares elegidos 
    cond2 = True   #Que los lugares a ocupar sean todos de la misma fila (solo agrupación horizontal)
    while True:
        print( np.reshape(np.arange(1,row*col+1), (row, col)))
        opcion = input("  Indices de los bloques que ocupa el subgráfico en la cuadrícula (i_first, i_last): ").split(',')
        if(len(opcion) == 1):   #si se ingresa la ubicacion con un solo indice
            ubic_plot = np.arange(int(opcion[0])-1,int(opcion[0]))
        else:                   #se ingresa la ubicacion como una tupla ( , )
            ubic_plot = np.arange( int(opcion[0])-1, int(opcion[1]) )  #vector con la ubicacion del subgrafico en la grilla
        
        #Chequear que los lugares a ocupar sean todos de la misma fila
        k = np.arange(1,row+1)
        lim_derecho = col*k-1
        for i in range(len(ubic_plot)):
            #si encuentro un elemento en el borde del grafico (lim_derecho) y no es el ultimo, me estoy sobrepasando de fila
            if(ubic_plot[i] in lim_derecho and i != len(ubic_plot)-1 ):   
                print("  Error. El subgrafico se excede en espacio")
                cond2 = False
                
        #Chequear que no estén ocupados todos los lugares
        if(True in lugares_ocupados[ubic_plot[0] : ubic_plot[-1]+1]):   #no hay ningun lugar ocupado en los elegidos
            print("  Error. Uno de los lugares elegido está ocupado")
            cond1 = False
        if(cond1 and cond2):
            lugares_ocupados[ubic_plot[0] : ubic_plot[-1] + 1] = True
            joinVec.append( (ubic_plot[0] + 1 , ubic_plot[-1] + 1) )
            break       
        cond1 = cond2 = True

def graficar():
    Npts = 1000    #cantidad de puntos por grafico
    y = []  #lista de vectores
    x = []
    ylim = []
    xlim = []
    xlabel = []
    ylabel = []
    typeGraf = []
    joinVec = []
    
    numplot = int(input("Número de figura: "))
    opcion = input("Cantidad de filas y columnas para distribuir los gráficos (fila, col): ").split(',')
    row, col = int(opcion[0]), int(opcion[1])
    lugares_ocupados = np.full(row*col, False)   #True = lugar ocupado, False = lugar libre
    plot = 0

    while False in lugares_ocupados[:]:     #seguir agregando subgraficos mientras haya lugar
        print("Subgrafico %d:"%(plot+1))
        #validación de coherencia entre cantidad de subplots y su distribucion
        validarSubgrafico(lugares_ocupados, row, col, joinVec)
        
        dist = input("  Distribución de datos [Normal/Uniforme]: ")
        #ajustar amplitud vertical segun los limites y
        if(dist.lower() == "normal" or dist.lower() == "n"):    #Ingresar mu y sigma
            opcion = input("    Valores de (mu, sigma) = ").split(',')
            mu, sigma =  float(opcion[0]), float(opcion[1])
            y.append(np.random.normal(mu, sigma, Npts))
        if(dist.lower() == "uniforme" or dist.lower() == "u"):  
            opcion = input("    Límites para el rango (inf, sup) = ").split(',')
            inf, sup = float(opcion[0]), float(opcion[1])
            y.append(np.random.uniform(inf,sup,Npts))
        if(dist.lower() == "d"):  #grafico default para testeo
            y.append(np.random.uniform(0,1,Npts))
            xlabel.append("Tiempo")
            xlim.append([0,5])
            rango = abs(xlim[plot][1]-xlim[plot][0])
            x.append( np.arange(xlim[plot][0], xlim[plot][1], rango/Npts) )
            ylabel.append("Amplitud")
            ylim.append([-0.5,1.5])
            typeGraf.append("plot")
        else:
            xlabel.append(input("  Etiqueta para el eje X: "))
            lim = input("    Límites eje X (inferior, superior): ").split(',')
            xlim.append( [float(lim[0]), float(lim[1])] )
            
            rango = abs(xlim[plot][1]-xlim[plot][0])
            x.append( np.arange(xlim[plot][0], xlim[plot][1], rango/Npts) )   #asigno 1000 puntos a la función entre los limites inferior y superior
            
            ylabel.append( input("  Etiqueta para el eje Y: ") )
            lim = input("    Límites eje Y (inferior, superior): ").split(',')
            ylim.append( [float(lim[0]), float(lim[1])] )
            
            opcion = input(  "Tipo de gráfico [Plot/Stem]: ")
            if(opcion.lower() == "plot" or opcion.lower() == "p"): 
                typeGraf.append("plot")
            elif(opcion.lower() == "stem" or opcion.lower() == "s"): 
                typeGraf.append("stem")
                
        plot += 1   
        if(input("Desea agregar otro grafico? [s/n] ").lower() == "n"):
            break
    
    if(False not in lugares_ocupados[:]):
        print("No entran más subgráficos con la configuración actual")
              
    if(input("Mostrar gráficos? [s/n]: ").lower() == "s"):
        show = True
        
    figPlot(x, y, row=row, col=col, joinVec=joinVec, numplot=numplot, show=show, xlim=xlim, ylim=ylim, typeGraf=typeGraf, xlabel=xlabel, ylabel=ylabel)

graficar()

