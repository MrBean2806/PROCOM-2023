import numpy as np
import matplotlib.pyplot as plt
from tool._fixedInt import *
from funciones import *
## Parametros generales
T     = 1.0/1.0e9 # Periodo de baudio
Nsymb = 1000          # Numero de simbolos
os    = 8
## Parametros de la respuesta en frecuencia
Nfreqs = 256          # Cantidad de frecuencias

## Parametros del filtro de caida cosenoidal
beta   = [0.0,0.5,0.99] # Roll-Off
Nbauds = 16     # Cantidad de baudios del filtro
## Parametros funcionales
Ts = T/os              # Frecuencia de muestreo

quantization = ['puntoFlotante', 'S(8,7) round','S(8,7) trunc',
                'S(6,4) round', 'S(6,4) trunc', 'S(3,2) round', 'S(3,2) trunc']

# Generacion de simbolos I/Q
symbolsI = 2*(np.random.uniform(-1,1,Nsymb)>0.0)-1;
symbolsQ = 2*(np.random.uniform(-1,1,Nsymb)>0.0)-1;
# Upsampling de los simbolos
zsymbI = np.zeros(os*Nsymb);    zsymbI[1:len(zsymbI):int(os)]=symbolsI
zsymbQ = np.zeros(os*Nsymb);    zsymbQ[1:len(zsymbQ):int(os)]=symbolsQ

graficar_Simb(Nsymb, symbolsI, symbolsQ, zsymbI, zsymbQ)

#Generacion de graficas para cada tipo de cuantizacion
for q in range(len(quantization)):
    if(quantization[q]!='puntoFlotante'): 
        intWidth = int(quantization[q][2])
        fractWidth = int(quantization[q][4])
        roundMode = quantization[q][7:]
    else:   intWidth=fractWidth=roundMode=-1
    print(quantization[q])

    
    # Calculo de tres pulsos con diferente roll-off
    (t,rc0) = rcosine(beta[0],T,os,Nbauds,intWidth,fractWidth,roundMode)
    (t,rc1) = rcosine(beta[1],T,os,Nbauds,intWidth,fractWidth,roundMode)
    (t,rc2) = rcosine(beta[2],T,os,Nbauds,intWidth,fractWidth,roundMode)
    # Calculo respuesta en frec para los tres pulsos
    [H0,A0,F0] = resp_freq(rc0, Ts, Nfreqs)
    [H1,A1,F1] = resp_freq(rc1, Ts, Nfreqs)
    [H2,A2,F2] = resp_freq(rc2, Ts, Nfreqs)
    #Convolucion de los filtros con los simbolos
    symb_out0I = np.convolve(rc0,zsymbI,'same'); symb_out0Q = np.convolve(rc0,zsymbQ,'same')
    symb_out1I = np.convolve(rc1,zsymbI,'same'); symb_out1Q = np.convolve(rc1,zsymbQ,'same')
    symb_out2I = np.convolve(rc2,zsymbI,'same'); symb_out2Q = np.convolve(rc2,zsymbQ,'same')
    ## GENERACION DE GRAFICAS
    plt.figure(figsize=[12,7])
    plt.suptitle('Cuantizacion %s'%quantization[q])
    plt.subplot(2,2,1)
    graficar_RtaImpulso(t,rc0,rc1,rc2)
    plt.subplot(2,2,2)
    graficar_RtaFreq(H0,H1,H2,A0,A1,A2,F0,F1,F2,T,Ts)
    plt.subplot(2,2,(3,4))
    graficar_ConvSimb(symb_out0I, symb_out1I, symb_out2I, zsymbI, beta)
    
    plt.figure(figsize=[8,8])
    plt.suptitle('Cuantizacion %s'%quantization[q])
    plt.subplot(2,3,1)
    graficar_diagOjo(os, Nbauds, beta[0], symb_out0I)
    plt.subplot(2,3,2)
    graficar_diagOjo(os, Nbauds, beta[1], symb_out1I)
    plt.subplot(2,3,3)
    graficar_diagOjo(os, Nbauds, beta[2], symb_out2I)
    
    offset_eye=6
    plt.subplot(2,3,4)
    graficar_constelacion(os, offset_eye-1, symb_out0I, symb_out0Q, 'r.')
    graficar_constelacion(os, offset_eye+1, symb_out0I, symb_out0Q, 'r.')
    graficar_constelacion(os, offset_eye, symb_out0I, symb_out0Q, 'b.')
    plt.subplot(2,3,5)
    graficar_constelacion(os, offset_eye-1, symb_out1I, symb_out1Q, 'r.')
    graficar_constelacion(os, offset_eye+1, symb_out1I, symb_out1Q, 'r.')
    graficar_constelacion(os, offset_eye, symb_out1I, symb_out1Q, 'b.')
    plt.subplot(2,3,6)
    graficar_constelacion(os, offset_eye-1, symb_out2I, symb_out2Q, 'r.')
    graficar_constelacion(os, offset_eye+1, symb_out2I, symb_out2Q, 'r.')
    graficar_constelacion(os, offset_eye, symb_out2I, symb_out2Q, 'b.')
 
plt.show()
