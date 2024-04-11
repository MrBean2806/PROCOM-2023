import time
import serial

ser = serial.serial_for_url('loop://', timeout=1)

ser.isOpen()
ser.timeout=None
ser.flushInput()
ser.flushOutput()


print('Ingrese un comando:\n')
while True:
    while True:
        data = input(">> ")     #comando a enviar
        if(data == '1' or data == '2' or data == 'exit'):
            break
        print("Comando inválido. Ingreselo nuevamente")
    #envio del comando
    for ptr in range(len(data)):
        ser.write(data[ptr].encode())

    #recepcion del comando
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1).decode()
    # print(out)
    if(out == '1'):
        with open("calculadora.py") as f:
            exec(f.read())
    elif(out == '2'):
        with open("grafico.py") as f:
            exec(f.read())
    elif(out == 'exit'):
        if ser.isOpen():
            ser.close()
        break
        
    if out != '':
        print("<< " + out)
