`define N_LEDS 4
`define NB_SEL 2
`define NB_COUNT 11
`define NB_SW 4

`timescale 1ns/100ps

module tb_shiftleds();

    parameter N_LEDS   = `N_LEDS   ;
    parameter NB_SEL   = `NB_SEL   ;
    parameter NB_COUNT = `NB_COUNT ;
    parameter NB_SW    = `NB_SW    ;

	wire [N_LEDS - 1 : 0] o_led    ;
	wire [N_LEDS - 1 : 0] o_led_r  ;
	wire [N_LEDS - 1 : 0] o_led_b  ;
	wire [N_LEDS - 1 : 0] o_led_g  ;
	reg  [NB_SW  - 1 : 0] i_btn    ; 
	reg  [NB_SW  - 1 : 0] i_sw     ;
	reg                   i_reset  ;
	reg                   clock    ;
 

	always #5 clock = ~clock;
    initial begin
     
        clock = 0;
		i_reset = 1'b0;
		i_btn = 4'b0010;    //rojo
		i_sw = 4'b0001;     //R0
	
		#30 i_reset = 1'b1;       $display("%6d: Libero el reset", $time);
            i_btn[1] = 1'b0;       //suelto el boton
        #40 i_btn[0] = 1'b1;    $display("%6d: Cambio a Modo Flash", $time);
        #20 i_btn[0] = 1'b0;
        #40 i_btn[0] = 1'b1;    $display("%6d: Cambio a Modo SR2", $time);
        #20 i_btn[0] = 1'b0;    
        #80 i_sw[3] = 1'b1;     $display("%6d: Cambio direccion de shift", $time);
        #150;
      
    $finish;
	end
    
   top
   #(
     .N_LEDS   (N_LEDS)  ,
     .NB_SEL   (NB_SEL)  ,
     .NB_COUNT (NB_COUNT),
     .NB_SW    (NB_SW)
     )
 u_top
   (
    .o_led     (o_led)    ,
    .o_led_r   (o_led_r)  ,
    .o_led_b   (o_led_b)  ,
    .o_led_g   (o_led_g)  ,
    .i_btn     (i_btn)    ,
    .i_sw      (i_sw)     ,
    .i_reset   (i_reset)  ,
    .clock     (clock)
    );
 

endmodule