import numpy as np
import matplotlib.pyplot as pl

def figPlot(x, y, row, col, joinVec, xlim, ylim, xlabel, ylabel, params, label, typeGraf, numplot=1, show=True):
    pl.figure(figsize=[14,7], num = numplot)
    
    Nplots = len(x)     #la cantidad de plots es la cantidad de vectores que se reciben para graficar
    
    for plot in range(Nplots):
        pl.subplot(row,col,joinVec[plot])   
        if(typeGraf[plot] == 'plot'):
            pl.plot(x[plot], y[plot], params[plot], r'$\beta=0.1$')
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
            
    pl.legend()
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



