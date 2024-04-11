#include <stdio.h>
#include <string.h>
#include "xparameters.h"
#include "xil_cache.h"
#include "xgpio.h"
#include "platform.h"
#include "xuartlite.h"
#include "microblaze_sleep.h"

#define PORT_IN	 		XPAR_AXI_GPIO_0_DEVICE_ID //XPAR_GPIO_0_DEVICE_ID
#define PORT_OUT 		XPAR_AXI_GPIO_0_DEVICE_ID //XPAR_GPIO_0_DEVICE_ID

//Device_ID Operaciones
#define def_SOFT_RST            0
#define def_ENABLE_MODULES      1
#define def_LOG_RUN             2
#define def_LOG_READ            3

XGpio GpioOutput;
XGpio GpioParameter;
XGpio GpioInput;
u32 GPO_Value;
u32 GPO_Param;
XUartLite uart_module;

//Funcion para recibir 1 byte bloqueante
//XUartLite_RecvByte((&uart_module)->RegBaseAddress)

int main()
{
	init_platform();
	int Status;
	XUartLite_Initialize(&uart_module, 0);

	GPO_Value=0x00000000;
	GPO_Param=0x00000000;
	unsigned char cabecera[4];

	Status=XGpio_Initialize(&GpioInput, PORT_IN);
	if(Status!=XST_SUCCESS){
        return XST_FAILURE;
    }
	Status=XGpio_Initialize(&GpioOutput, PORT_OUT);
	if(Status!=XST_SUCCESS){
		return XST_FAILURE;
	}
	XGpio_SetDataDirection(&GpioOutput, 1, 0x00000000);
	XGpio_SetDataDirection(&GpioInput, 1, 0xFFFFFFFF);

	u32 value;
	int datos = 0;
	unsigned char estado_sw = 0;
	unsigned char trama[2];	//16 bits

	while(1){
    read(stdin, trama, 2);
    datos = 0;
    datos = (trama[0] << 8) | trama[1];
    /* unsigned char datos_rec[3]; */
    /* short int i; */
    /* for(i=0;i<3;i++){ */
    /*   datos_rec[i]=XUartLite_RecvByte((&uart_module)->RegBaseAddress); */
    /* } */
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// ACA es donde se escribe toda la funcionalidad
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    //El bit 13 indica si hay que leer los sw o activar los leds
    if ((datos & 0xE000) != 0xA000)	//El inicio de la trama no es el correcto
          continue;
    if((datos&(0x1000))>>12){
    	estado_sw = 0;
    	XGpio_DiscreteWrite(&GpioOutput,1, (u32) 0x00000000);
    	value	  = XGpio_DiscreteRead(&GpioInput, 1);
    	estado_sw = (char)(value&(0x0000000F));	//leo los 4 LSB
    	estado_sw |= 0xA0;

    	while(XUartLite_IsSending(&uart_module)){}
    	XUartLite_Send(&uart_module, &(estado_sw),1);

    }else{	//prendo leds
    	XGpio_DiscreteWrite(&GpioOutput,1, (u32) datos & 0xFFF);	//Me quedo con los primeros 12 bits de la trama
    }

//    XGpio_DiscreteWrite(&GpioOutput,1, (u32) datos & 0xFFF);	//Me quedo con los primeros 12 bits de la trama



//		   switch(cabecera[0]){
//           case '0':
//               XGpio_DiscreteWrite(&GpioOutput,1, (u32) 0x00000249);
//               break;
//           case '1':
//               XGpio_DiscreteWrite(&GpioOutput,1, (u32) 0x00000492);
//               break;
//           case '2':
//               XGpio_DiscreteWrite(&GpioOutput,1, (u32) 0x00000924);
//               break;
//           case '3':
//               XGpio_DiscreteWrite(&GpioOutput,1, (u32) 0x00000000);
//               value = XGpio_DiscreteRead(&GpioInput, 1);
//               datos=(char)(value&(0x0000000F));
//               while(XUartLite_IsSending(&uart_module)){}
//               XUartLite_Send(&uart_module, &(datos),1);
//               break;
//		   }
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// FIN de toda la funcionalidad
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        }
	
	cleanup_platform();
	return 0;
}
