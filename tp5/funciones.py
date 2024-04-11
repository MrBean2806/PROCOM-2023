import numpy as np
import matplotlib.pyplot as plt
from tool._fixedInt import *

def rcosine(beta, Tbaud, oversampling, Nbauds, intWidth, fractWidth, roundMode, Norm=False):
    """ Respuesta al impulso del pulso de caida cosenoidal """
    t_vect = np.arange(-0.5*Nbauds*Tbaud, 0.5*Nbauds*Tbaud, 
                       float(Tbaud)/oversampling)

    y_vect = []
    for t in t_vect:
        y_vect.append(np.sinc(t/Tbaud)*(np.cos(np.pi*beta*t/Tbaud)/
                                        (1-(4.0*beta*beta*t*t/
                                            (Tbaud*Tbaud)))))

    y_vect = np.array(y_vect)
    if(fractWidth != -1):
        temp_array = arrayFixedInt(intWidth, fractWidth, y_vect, signedMode='S', roundMode=roundMode, saturateMode='saturate')
        for i in range(len(temp_array)):
            y_vect[i] = temp_array[i].fValue

    if(Norm):
        return (t_vect, y_vect/np.sqrt(np.sum(y_vect**2)))
        #return (t_vect, y_vect/y_vect.sum())
    else:
        return (t_vect,y_vect)


def resp_freq(filt, Ts, Nfreqs):
    # """Computo de la respuesta en frecuencia de cualquier filtro FIR"""
    H = [] # Lista de salida de la magnitud
    A = [] # Lista de salida de la fase
    filt_len = len(filt)

    #### Genero el vector de frecuencias
    freqs = np.matrix(np.linspace(0,1.0/(2.0*Ts),Nfreqs))
    #### Calculo cuantas muestras necesito para 20 ciclo de
    #### la mas baja frec diferente de cero
    Lseq = 20.0/(freqs[0,1]*Ts)

    #### Genero el vector tiempo
    t = np.matrix(np.arange(0,Lseq))*Ts

    #### Genero la matriz de 2pifTn
    Omega = 2.0j*np.pi*(t.transpose()*freqs)

    #### Valuacion de la exponencial compleja en todo el
    #### rango de frecuencias
    fin = np.exp(Omega)

    #### Suma de convolucion con cada una de las exponenciales complejas
    for i in range(0,np.size(fin,1)):
        fout = np.convolve(np.squeeze(np.array(fin[:,i].transpose())),filt)
        mfout = abs(fout[filt_len:len(fout)-filt_len])
        afout = np.angle(fout[filt_len:len(fout)-filt_len])
        H.append(mfout.sum()/len(mfout))
        A.append(afout.sum()/len(afout))

    return [H,A,list(np.squeeze(np.array(freqs)))]


def eyediagram(data, n, offset, period):
    span     = 2*n
    segments = int(len(data)/span)
    xmax     = (n-1)*period
    xmin     = -(n-1)*period
    x        = list(np.arange(-n,n,)*period)
    xoff     = offset

    plt.figure()
    for i in range(0,segments-1):
        plt.plot(x, data[(i*span+xoff):((i+1)*span+xoff)],'b')       
    plt.grid(True)
    plt.xlim(xmin, xmax)
    plt.show()
    
    
def graficar_RtaImpulso(t,rc0,rc1,rc2):
    plt.plot(t,rc0,'ro-',linewidth=2.0,label=r'$\beta=0.0$')
    plt.plot(t,rc1,'gs-',linewidth=2.0,label=r'$\beta=0.5$')
    plt.plot(t,rc2,'k^-',linewidth=2.0,label=r'$\beta=1.0$')
    plt.legend()
    plt.grid(True)
    plt.xlabel('Muestras')
    plt.ylabel('Magnitud')
    plt.title('Respuesta al impulso del pulso de caida cosenoidal')
    
    
def graficar_RtaFreq(H0,H1,H2,A0,A1,A2,F0,F1,F2,T,Ts):
    plt.semilogx(F0, 20*np.log10(H0),'r', linewidth=2.0, label=r'$\beta=0.0$')
    plt.semilogx(F1, 20*np.log10(H1),'g', linewidth=2.0, label=r'$\beta=0.5$')
    plt.semilogx(F2, 20*np.log10(H2),'k', linewidth=2.0, label=r'$\beta=1.0$')

    plt.axvline(x=(1./Ts)/2.,color='k',linewidth=2.0)
    plt.axvline(x=(1./T)/2.,color='k',linewidth=2.0)
    plt.axhline(y=20*np.log10(0.5),color='k',linewidth=2.0)
    plt.legend(loc=3)
    plt.grid(True)
    plt.xlim(F2[1],F2[len(F2)-1])
    plt.xlabel('Frequencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.title('Respuesta en frecuencia del pulso de caida cosenoidal')


def graficar_ConvSimb(symb_out0I, symb_out1I, symb_out2I, zsymbI, beta):
    plt.plot(symb_out0I,'r-',linewidth=2.0,label=r'$\beta=%2.2f$'%beta[0])
    plt.plot(symb_out1I,'g-',linewidth=2.0,label=r'$\beta=%2.2f$'%beta[1])
    plt.plot(symb_out2I,'k-',linewidth=2.0,label=r'$\beta=%2.2f$'%beta[2])
    plt.plot(zsymbI,'o', label='Simbolos')
    plt.xlim(1000,1250)
    plt.grid(True)
    plt.legend()
    plt.xlabel('Muestras')
    plt.ylabel('Magnitud')
    plt.title('Convolución Simbolos I')

    # plt.subplot(2,2,4)
    # plt.plot(symb_out0Q,'r-',linewidth=2.0,label=r'$\beta=%2.2f$'%beta[0])
    # plt.plot(symb_out1Q,'g-',linewidth=2.0,label=r'$\beta=%2.2f$'%beta[1])
    # plt.plot(symb_out2Q,'k-',linewidth=2.0,label=r'$\beta=%2.2f$'%beta[2])
    # # plt.plot(zsymbQ,'o')
    # plt.xlim(1000,1250)
    # plt.grid(True)
    # plt.legend()
    # plt.xlabel('Muestras')
    # plt.ylabel('Magnitud')
    # plt.title('Convolución Simbolos Q')


def graficar_Simb(Nsymb, symbolsI, symbolsQ, zsymbI, zsymbQ):
    label = 'Simbolos: %d' % Nsymb
    plt.figure(figsize=[10,6])
    plt.subplot(2,2,1)
    plt.hist(symbolsI,label=label)
    plt.legend()
    plt.xlabel('Simbolos')
    plt.ylabel('Repeticiones')
    plt.title('Simbolos I')
    plt.subplot(2,2,2)
    plt.hist(symbolsQ,label=label)
    plt.legend()
    plt.xlabel('Simbolos')
    plt.ylabel('Repeticiones')
    plt.title('Simbolos Q')
    plt.subplot(2,2,3)
    plt.stem(zsymbI,'o')
    plt.xlim(1000,1250)
    plt.grid(True)
    plt.title('Upsampling de los símbolos')
    plt.subplot(2,2,4)
    plt.stem(zsymbQ,'o')
    plt.xlim(1000,1250)
    plt.grid(True)
    
    
def graficar_diagOjo(os, Nbauds, beta, symb):
    offset_eye = 6
    span     = 2*os
    data = symb[100:len(symb)-100]
    segments = int(len(data)/span)
    xmax     = (os-1)*Nbauds
    xmin     = -(os-1)*Nbauds
    x        = list(np.arange(-os,os,)*Nbauds)

    plt.title('Rolloff = %.2f'%beta)
    for i in range(0,segments-1):
    	plt.plot(x, data[(i*span+offset_eye):((i+1)*span+offset_eye)],'b')       
    plt.grid(True)
    plt.xlim(xmin, xmax)



def graficar_constelacion(os, offset_eye, symb_I, symb_Q, fmt):
    plt.plot(symb_I[100+offset_eye:len(symb_I)-(100-offset_eye):int(os)],
             symb_Q[100+offset_eye:len(symb_Q)-(100-offset_eye):int(os)],
                 fmt, linewidth=2.0)
    plt.xlim((-2, 2))
    plt.ylim((-2, 2))
    plt.grid(True)
    plt.xlabel('Real')
    plt.ylabel('Imag')

