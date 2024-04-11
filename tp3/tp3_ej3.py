import serial

def armarTrama(device, data):
    #genero cada palabra de la trama como un string, y los guardo en una lista 
    cabecera = 4*['0']
    cabecera [0] = "101"  
    
    if(len(data) < 2**4-1):                     #trama corta (4 bits)
        cabecera[0] += '0'                      # L/S = 0
        cabecera[0] += format(len(data), '04b')     #agrego el tamaño del dato en bin (4 bits)
    elif(len(data) < 2**16-1):                  #trama larga (16 bits)
        cabecera[0] += '1'                      # L/S = 1
        cabecera[0] += '0000'                   # S.size = 0
        aux = format(len(data), '016b')
        cabecera[1] = aux[0:8]                  #L.size (L)
        cabecera[2] = aux[8:16]                 #L.size (H)
    cabecera[3] = format(int(device), '08b')    #Device
    fin = "010" + cabecera[0][3:8]              #Final de trama

    #convierto los strings de cada campo en un arreglo de bytes para enviarlo por puerto serie
    aux = []
    for ptr in range(len(cabecera)):
        aux.append(int(cabecera[ptr],2))    #arreglo de la representacion entera de los bytes de la cabecera
    trama = bytearray(aux)                  #genero un arreglo de bytes con esos enteros
    trama += bytearray(data, 'utf-8')       #campo data
    trama += bytearray([int(fin,2)])        #campo final de la trama
    return trama 

def desarmarTrama(trama_raw):
    #Recibo la trama como un arreglo de bytes y la convierto en un arreglo de strings para extraer los campos
    trama = []                              #arreglo de strings con los campos de la trama
    data = ''
    for ptr in range(len(trama_raw)):
        if(ptr >= 0 and ptr < 4):           #primeros 4 campos de la trama
            trama.append(format(trama_raw[ptr], '08b'))
        elif(ptr == len(trama_raw)-1):      #final trama
            trama.append(format(trama_raw[-1], '08b'))
        else:                               #data
            trama.append(chr(trama_raw[ptr]))

    #Extraigo los valores de cada campo
    if int(trama[0],2) & 0b00010000:       #trama larga
        #Convierte los caracteres de la trama que contienen L. size (H y L) en un numero de 8 bits de nuevo, los concatena como strings y los convierte a entero para obtener el valor final
        size = int(trama[1] + trama[2], 2)
    else:                                  #trama corta
        size = int(trama[0][4:9], 2)
    device = int(trama[3],2)    
    for ptr in range(size):
        data += trama[4+ptr]
        
    if(verificarTrama(trama) == True):
        return [device, data]
    else:
        return [None, None]

def verificarTrama(trama):     #trama -> arreglo de strings con los campos de la trama
    tramaValida = True
    #La trama será inválida si el primer campo no comienza con '101',
    #o si el último campo no es igual al primero pero comenzando con '010'
    inicio = trama[0]
    fin = trama[-1]
    
    if(inicio[0:3] != '101'):
        tramaValida = False
    elif(fin != '010' + inicio[3:8]):
        tramaValida = False
    
    return tramaValida

ser = serial.serial_for_url('loop://', timeout=1)

ser.isOpen()
ser.timeout=None
ser.flushInput()
ser.flushOutput()
device = "0"    

while True:
    print('> Ingrese un comando:')
    #validación de comando
    while True:
        data = input(">> ")     #comando a enviar
        if(data == 'Calculadora' or data == 'Graficar' or data == 'exit'):
            break
        print("> Comando inválido. Ingreselo nuevamente")
    
    trama_tx = armarTrama(device=device, data=data)    
    ser.write(trama_tx)         #transmito trama como bytearray
    # print("Trama enviada = ", trama_tx)

    #recepcion del comando
    trama_rx = bytearray(1) #esto le agrega un byte al principio al arreglo
    while ser.inWaiting() > 0:
        trama_rx += ser.read(1)
    # print("Trama recibida = ", trama_rx)

    device, data = desarmarTrama(trama_rx[1:])
    # print("device = ", device)    
    # print("data = ", data)  
        
    if(data == 'Calculadora'):
        with open("calculadora.py") as f:
            exec(f.read())
    elif(data == 'Graficar'):
        with open("grafico.py") as f:
            exec(f.read())
    elif(data == 'exit'):
        if ser.isOpen():
            ser.close()
        break
    else: print("Error en la trama recibida")
