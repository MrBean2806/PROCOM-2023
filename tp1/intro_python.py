#!/usr/bin/env python
# coding: utf-8

# # Comentarios

# In[1]:


# Primeros comandos de Python
# Comentarios de una sola linea
"""
Comentarios multilinea
Comentarios multilinea
"""


# # Importando librerías

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# # Asignaciones basicas

# In[3]:


d_num  = 5
d_flt  = 5.
d_str  = 'texto'
d_numv = [0,1,2,3]
d_strv = ['Sol','Luna','Tierra']


# # Imprimir en pantalla

# In[4]:


print('#'*20)
print('#############################################')
print('Este numero es: ',d_num)
print(d_str)
print('Lista: ',d_numv,'\t','Un dato: ',d_numv[0])
print('Lista: ',d_strv,'\t','Un dato: ',d_strv[2])
print('El valor d_strv: %s'%d_strv[0])
print('El valor d_strv: %.2f'%(12.5555))
print('El valor d_strv: {:.2f}'.format(12.5555))
print('El valor d_strv: {}'.format(12.5555))
print('#############################################')


# # Operaciones

# In[5]:


print('#############################################')
suma     = 3 + d_num;    print('Sum:',suma)
resta    = suma - 15;    print('Res:',resta)
prod     = suma * resta; print('Pro:',prod)
div      = 6/2;          print('Div:',div,'\tTipo:',type(div))
div_e    = 6//2;         print('Div entera:',div_e,'\tTipo:',type(div_e))
modulo   = 8 % 3;        print('Mod:',modulo)
strv     = 'day'*2;      print(strv)        # Se repite la palabra
lists    = d_numv * 3;   print(lists)       # Se repite la lista
print('#############################################')


# # Condicional y métodos de generación de strings

# In[6]:


print ('#############################################')
ptr = 0
if(ptr==0):
    print ("Este numero es %d"%ptr)
elif(ptr==1):
    print ("Este numero es %d"%ptr + " no esperado")
elif(ptr>20 and ptr<=30):
    print ('>>>>>>>: ',ptr )
else:
    print ('El valor es %d %s'%(ptr,"no esperado"))
print ('#############################################')


# # Iterativo

# In[7]:


print ('#############################################')
for ptr in range(8):
    print (ptr,end=' ')
print()
print ('#############################################')
print ('#############################################')
for ptr in d_strv:
    print (ptr,end=' ')
print()
print ('#############################################')


# # Operaciones con vectores (np.ndarray)

# In[8]:


print('#############################################')
t_array = np.array([0,1,2,3]);                   print(t_array)
t_array = np.arange(0,5,2);                      print(t_array) 
t_array = np.arange(0,5)*3;                      print(t_array)
t_array = np.arange(0,5)//3;                     print(t_array)
t_array = np.arange(0,5)/3;                      print(t_array)
t_array = np.arange(0,5)*np.arange(0,5);         print(t_array)
t_array = np.dot(np.arange(0,5),np.arange(0,5)); print(t_array)

t_matrix = np.dot(np.matrix([[0, 1, 2, 3],[0, 1, 2, 3]]),
                  np.matrix([[0, 1], [2, 3],[0, 1], [2, 3]])); print(t_matrix)
print(type(t_matrix))
print('#############################################')


# # Seleccion en vectores

# In[9]:


print ('#############################################')
t0     = np.arange(0,5);                        print (t0)

t0[0]  = 25;                                    print (t0)                          
t0[len(t0)-1] = 100;                                    print (t0)
t0[-1] = 45;                                    print (t0)                          
t0[:]  = 1;                                     print (t0)
t0[0:2]= 3;                                     print (t0)
t0[3:5]= 2;                                     print (t0)
t0[0:6]= 5;                                     print (t0)

t0     = np.arange(0,5);                        print (t0)
c0= t0>2;                                       print (c0)
t1 = t0[c0];                                    print (t1)
t2 = t0[t0<=2];                                 print (t2)

print (len(t0),'\n',np.size(t0),'\n',np.size(t_matrix))
print (t_matrix)
print (np.shape(t_matrix))
print ('#############################################')


# # Matrices

# In[10]:


print ('#############################################')
t1         = np.zeros((1,5)); print (t1)
print(type(t1))
t1         = np.ones((3,5)) ; print (t1)
t1         = np.zeros((5,5)); print (t1)

t1[:,3]    = 1;               print (t1)
t1[0:5:2,:2]  = 2;            print (t1)
t1         = t1 + 5;          print (t1)
t1         = t1 - 5;          print (t1)
t1         = t1 * 5;          print (t1)
t1         = t1 / 5;          print (t1)
t2         = t1 * t1;         print (t2)
t2         = np.dot(t1, t1);  print (t2)
r,c=np.shape(t1);             print (r,c)
print ('#############################################')


# # Iterativo

# In[11]:


print ('#############################################')
t_vec = np.arange(0.,25.1,1.)
print (t_vec)
for ptr in range(len(t_vec)-1,-1,-1):
    print (t_vec[ptr])
print ('#############################################')


# ## Ejemplo

# In[12]:


print('#############################################')
count = 0
lista = []
for ptr in t_vec[0:5]:
    print (ptr)
    count += 1
    t_vec[count]=ptr+2
    lista.append(ptr+2)
print("Vec>> ",t_vec[1:6])
print("List>> ",lista)
print('#############################################')


# ## Iterativo

# In[13]:


print('#############################################')
ptr = 0
o_data = 0
while(ptr < len(t_vec)):
    o_data += t_vec[ptr]
    ptr    += 1
print(o_data)
print('#############################################')


# # Igualdad en float

# In[14]:


a=2/3.1
b=0.2/0.31
print (a==b)


# In[15]:


print(a)
print(b)


# In[16]:


print('{:.22f}'.format(a))
print('{:.22f}'.format(b))


# In[17]:


def are_equal(n1,n2):
    return abs(n1-n2)<0.0000001

print(are_equal(a,b))


# In[18]:


import math
print(math.isclose(a, b, abs_tol=0.0000001))


# # Definicion de funciones

# In[19]:


def producto(a,b):
    c = a * b
    return c

c = producto(2,2)
print (c)


# ## Pasaje de argumentos mutables e inmutables

# In[20]:


def funcion(val):
    val=4
    print(val)
    return

x=10
funcion(x)
print(x)


# In[21]:


def funcion2 (lista):
    lista.append(40)
    #lista[0] = 8
    #lista = [8]
    #print(lista)
    return

x=[10,20,30]
funcion2(x)
print(x)


# In[22]:


def funcion3 (vector):
    vector[0] = 8
    #vector = np.array([8])
    #print(vector)
    return

x=np.array([10,20,30])
funcion3(x)
print(x)


# # Shallow copy - Deep copy

# In[23]:


colores1 = ["rojo", "azul"]
colores2 = colores1
print(colores1)
print(colores2)


# In[24]:


colores2[0]="amarillo"
print(colores1)
print(colores2)


# In[25]:


colores1 = ["rojo", "azul"]
colores2 = colores1

colores2=["amarillo","verde"]
print(colores1)
print(colores2)


# In[26]:


colores1 = ["rojo", "azul"]
colores2 = colores1[:]

colores2[0]="amarillo"
print(colores1)
print(colores2)


# In[27]:


colores1 = ["rojo", "azul"]
colores2 = colores1.copy()

colores2[0]="amarillo"
print(colores1)
print(colores2)


# In[28]:


#Con vectores

numeros1 = np.arange(0,4)
numeros2 = numeros1
numeros2[0:2] = 33
print(numeros1)
print(numeros2)

numeros1 = np.arange(0,4)
numeros2 = numeros1.copy() #deep copy
numeros2[0:2] = 33
print(numeros1)
print(numeros2)


# # Importando módulos

# In[29]:


import sys
print(sys.path)


# In[30]:


import hola
hola.decirHola("Juan")
#from hola import decirHola
#decirHola("Juan")


# # Entrada de datos

# In[31]:


a = input('Ingrese Opcion')
print (a)


# # String Split

# In[32]:


text = 'Hola a todos'

# Splits at space
print(text.split())

word = 'Hola, a, todos'

# Splits at ','
print(word.split(','))

word = 'Hola:a:todos'

# Splitting at ':'
print(word.split(':'))

word = 'CatBatSatFatOr'

# Splitting at t
print(word.split('t'))


# # String Join

# In[34]:


# Joining with empty separator
list1 = ['Hola', 'a', 'todos']
print(" ".join(list1))

# Joining with string
list1 = " join "
print("$".join(list1))


# In[ ]:




