import time
import serial
import sys

# Remoto a local
# pscp -P 4466 user@fulgorip1.hopto.org:/home/user/work dda/<user>/<file> ./
# Local a remoto
# pscp -P 4466 ./<file> user@fulgorip1.hopto.org:/home/user/work dda/<user>/

portUSB = sys.argv[1]
if(portUSB == 'debug'):
    ser = serial.serial_for_url('loop://', timeout=1)
    ser.isOpen()
    ser.timeout=None
    ser.flushInput()
    ser.flushOutput()
    
else:
    ser = serial.Serial(
        port='/dev/ttyUSB{}'.format(int(portUSB)),	#Configurar con el puerto
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    ser.isOpen()
    ser.timeout=None
    print(ser.timeout)


print('Comandos:')
print('+ get -> Imprime el estado de los switch')
print('+ set led <n> <color> -> Modifica el estado de los leds')
print('     n = numero de led (1-4)')
print('     color = color del led [R,G,B] (0-1)')
print('+ exit -> Salir del programa\n')
print('Ingrese un comando:\r\n')

# TRAMA -> lista de strings
# [inicio R/W led1 led2 led3 led4]
# [ 101    x  RGB  RGB  RGB  RGB]  -> 16 bits
inicioTrama = '101'
rw = '0'    # 0 = Write, 1 = Read
trama = [inicioTrama, rw] + 4*['000'] 

while(1):
    
    inputData = input("<< ")	
    if str(inputData) == 'exit':
        ser.close()
        exit()
    elif(str(inputData) == 'get'):
        print ("Wait Input Data")
        
        #Envio trama con RW=1
        trama = inicioTrama + '1' + 12*'0'
        trama_tx = bytearray([ int(trama[0:8],2), int(trama[8:16],2) ]) 
        # print(trama_tx)
        ser.write(trama_tx)
        time.sleep(2)

        # Recepcion de la respuesta
        trama_rx = bytearray(1) 
        if ser.inWaiting() > 0:
            trama_rx = ser.read(1)
            
        trama_rx = ord(trama_rx)
        # print(trama_rx)

        print("Switches:")
        for i in range(4):
            print("SW" + str(i), end="")
            if((trama_rx & (0x8>>i))):
                print(" ON")
            else:
                print(" OFF")

    elif(str(inputData[0:6] == "set led")):
        led = int(inputData[8])
        rgb = inputData[10:]
        color = 0b000

        if (rgb.find('r') != -1): color |= 0b100 
        if (rgb.find('g') != -1): color |= 0b010 
        if (rgb.find('b') != -1): color |= 0b001
        if (rgb == 'off'): color = 0b000
        
        # lista con el color de cada led, la convierto a un solo string
        trama[led+1] = format(color,'03b')
        trama_str = ''. join(trama)
        print(trama_str)
        # conversion de la trama a enviar de string a bytearray
        trama_tx = bytearray([int(trama_str[0:8],2), int(trama_str[8:16],2) ]) 
        ser.write(trama_tx)
        time.sleep(1)
    else:
        print("Opcion invalida, intente de nuevo")
