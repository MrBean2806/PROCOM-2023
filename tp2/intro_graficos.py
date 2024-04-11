#!/usr/bin/env python
# coding: utf-8

# # Graficos

# In[ ]:


# Grafica en la misma pagina, sino abre una ventana con qt5
#get_ipython().run_line_magic('matplotlib', 'inline')
#%matplotlib qt5


# ## Importamos librerias

# In[ ]:


import numpy as np
import matplotlib.pyplot as pl

#define las dimensiones de las figuras por defecto (en pulgadas)
pl.rcParams['figure.figsize']= [16.0,10.0]


# ## Grafico Simple

# In[ ]:


## Graficos usando matplotlib.pyplot
phase0 = 0.
phase1 = np.pi/2.
f0     = 2.
f1     = 2.
f2     = 4.

t  = np.arange(0.,f0,0.01)
y0 = np.sin(2.*np.pi*f0*t + phase0)
y1 = np.sin(2.*np.pi*f1*t + phase1)
y2 = np.cos(2.*np.pi*f2*t + phase0)

pl.figure(10)
pl.plot(t,y0,linewidth=1.0,label='Phase: %1.2f'%phase0)
pl.plot(t,y1,'o-',linewidth=1.0,label='Phase: %1.2f'%phase1)
pl.plot(t,y2,'x-r',linewidth=1.0,label='Phase: %1.2f'%phase0)
pl.stem(t,y2,label='Phase: %1.2f'%phase0)
#pl.axvline(x=1,color='k')
#pl.axvline(x=1.5,color='k')
#pl.axhline(y=0,color='k')
pl.ylabel('Amplitud')
pl.xlabel('Tiempo')
pl.title('Seno-Coseno')
pl.legend()
pl.grid()
pl.show()


# ## Histogramas

# In[ ]:


Nsymb   = 10000
symbols = np.random.uniform(-1,1,Nsymb)
#symbols = 2*(np.random.uniform(-1,1,Nsymb)>0.0)-1

pl.figure()
pl.hist(symbols,20,label='Symbols')
pl.legend()
pl.xlim(-1.5,1.5)
#pl.ylim(0,10000)
pl.grid()
#pl.show()


# In[ ]:


mu, sigma = 0, 0.1
samples   = np.random.normal(mu, sigma, 30000)

pl.figure()
count, bins, ignored = pl.hist(samples, 100, density=True)

pl.plot(bins, 1/(sigma * np.sqrt(2. * np.pi)) * 
         np.exp( - (bins - mu)**2 / (2. * sigma**2) ),
         linewidth=2, color='r')
pl.grid()
#pl.show()


# ## Scatter

# In[ ]:


mu, sigma = 0, 0.1
x   = np.random.normal(mu, sigma, 1000)
y   = np.random.normal(mu, sigma, 1000)
pl.figure(figsize=[8,8])
pl.scatter(x,y)
pl.xlim(-0.5,0.5)
pl.ylim(-0.5,0.5)
pl.grid()
#pl.show()


# ## Histograma 2D

# In[ ]:


from matplotlib.colors import LogNorm

mu, sigma = 0, 0.1
x   = np.random.normal(mu, sigma, 30000)
y   = np.random.normal(mu, sigma, 30000)

pl.figure(figsize=[10,8])
pl.hist2d(x, y, bins=100, norm=LogNorm())
pl.colorbar()
pl.xlim(-0.5,0.5)
pl.ylim(-0.5,0.5)
pl.grid()
#pl.show()


# ## Multiples Graficos

# In[ ]:


pl.figure(figsize=[14,14])
pl.subplot(3,3,(1,3))
pl.plot(t,y0,'.-',linewidth=2.0,label='Phase: %1.2f'%phase0)
pl.ylabel('Amplitud')
pl.xlabel('Tiempo')
pl.legend()
pl.grid()

pl.subplot(3,3,(4,7))
pl.plot(t,y1,'rx-',linewidth=1.0,label='Phase: %1.2f'%phase1)
pl.ylabel('Amplitud')
pl.xlabel('Tiempo')
pl.legend()
pl.grid()

pl.subplot(3,3,5)
pl.stem(t,y2,'y',markerfmt='C1o')
pl.plot(t,y2,'g',linewidth=1.0,label='Phase: %1.2f'%phase0)
pl.ylabel('Amplitud')
pl.xlabel('Tiempo')
pl.xlim(0,0.5)
pl.legend()
pl.grid()

pl.subplot(3,3,6)
pl.plot(t,y1,'.',linewidth=1.0,label='Phase: %1.2f'%phase1)
pl.ylabel('Amplitud')
pl.xlabel('Tiempo')
pl.legend()
pl.grid()

pl.subplot(3,3,(8,9))
pl.plot(t,y1,'m+-',linewidth=1.0,label='Phase: %1.2f'%phase1)
pl.ylabel('Amplitud')
pl.xlabel('Tiempo')
pl.legend()
pl.grid()
pl.title('Sin')

## Guardando figuras en archivos
# pl.savefig('grafica.eps')
# pl.savefig('grafica.pdf')
# pl.savefig('grafica.png')

#pl.show()


# ## Graficando datos desde un archivo

# In[ ]:


datos = np.fromfile('sine.log',sep=',')
pl.figure(figsize=[10,8])
pl.plot(datos)
pl.grid()
#pl.show()


# ## Control de graficos (solo en interprete no interactivo)

# In[ ]:

pl.show(block=False)
input('Press Enter to Continue')
pl.close()


# # In[ ]:


# def plotfigs(data,figNew=True,show=False):
#     if figNew==True:
#         pl.figure()

#     pl.plot(np.arange(0,len(data)),data,label='color')
#     pl.grid(True)

#     if show==True:
#         pl.show()

# plotfigs(y0)
# plotfigs(y1,figNew=False)
# plotfigs(y2,show=True)

