//TP4 ej1
`define N_LEDS 4
`define NB_SEL 2
`define NB_COUNT 32
`define NB_SW 4

module top
#(
  parameter N_LEDS    = `N_LEDS    ,
  parameter NB_SEL    = `NB_SEL    ,
  parameter NB_COUNT  = `NB_COUNT  ,
  parameter NB_SW     = `NB_SW
  )
 (
  output [N_LEDS - 1 : 0] o_led   ,
  output [N_LEDS - 1 : 0] o_led_r ,
  output [N_LEDS - 1 : 0] o_led_b ,
  output [N_LEDS - 1 : 0] o_led_g ,
  input  [NB_SW  - 1 : 0] i_btn   , //ver parametro
  input  [NB_SW  - 1 : 0] i_sw    ,
  input                   i_reset ,
  input                   clock
  );

//PARAMETROS LOCALES
localparam R0 = (2**(NB_COUNT-10))-1 ;
localparam R1 = (2**(NB_COUNT-9))-1  ;
localparam R2 = (2**(NB_COUNT-8))-1  ;
localparam R3 = (2**(NB_COUNT-7))-1  ;

localparam SEL0 = `NB_SEL'h0;
localparam SEL1 = `NB_SEL'h1;
localparam SEL2 = `NB_SEL'h2;
localparam SEL3 = `NB_SEL'h3;

localparam COLOR_R = 3'b001;
localparam COLOR_G = 3'b010;
localparam COLOR_B = 3'b100;
localparam MODE_FS = 1'b0;
localparam MODE_SR = 1'b1;

//VARIABLES INTERNAS
reg [NB_COUNT-1 : 0] counter;
reg [2 : 0] color_sel;      // [B G R]
reg mode_sel;
wire shift_en;
wire [NB_COUNT-1 : 0] counter_limit;
wire [N_LEDS-1 : 0] o_led_from_SR;
wire [N_LEDS-1 : 0] o_led_from_Flash;
wire [N_LEDS-1 : 0] o_led_from_mux;

//ENCLAVAMIENTO BOTONES
reg [NB_SW - 1 : 0] i_btn_state;
reg [NB_SW - 1 : 0] i_btn_last_state;


    always @ (posedge clock or negedge i_reset) begin
        if(!i_reset) 
            i_btn_last_state <= {NB_SW{1'b0}};
        else 
            i_btn_last_state <= i_btn;
    end
        
    always @ (posedge clock or negedge i_reset) begin
        if(!i_reset)
            mode_sel <= MODE_SR;
        else if((i_btn[0] == 1'b1) && (i_btn_last_state[0] == 1'b0))
            mode_sel <= ~mode_sel;
    end

    always @ (posedge clock or negedge i_reset) begin
        if(!i_reset) 
            color_sel <= COLOR_R;
        else if((i_btn[1] == 1'b1) && (i_btn_last_state[1] == 1'b0))
            color_sel <= COLOR_R;
        else if((i_btn[2] == 1'b1) && (i_btn_last_state[2] == 1'b0))
            color_sel <= COLOR_G;
        else if((i_btn[3] == 1'b1) && (i_btn_last_state[3] == 1'b0))
            color_sel <= COLOR_B;
    end


//CONTADOR Y COMPARADOR
    always @ (posedge clock or negedge i_reset) begin
        if(!i_reset) begin
            counter <= {NB_COUNT{1'b0}};
        end
        else if(i_sw[0]) begin
            if(counter >= counter_limit)
                counter <= {NB_COUNT{1'b0}};
            else
                counter <= counter + {{NB_COUNT-1{1'b0}},{1'b1}};
        end
        else begin
            counter <= counter;
        end
    end
//SELECTOR DE RETARDO
    assign counter_limit =  (i_sw[(NB_SW-1)-1 -: NB_SEL]==SEL0) ? R0 :
                            (i_sw[(NB_SW-1)-1 -: NB_SEL]==SEL1) ? R1 :
                            (i_sw[(NB_SW-1)-1 -: NB_SEL]==SEL2) ? R2 : R3;
//SHIFT REGISTER Y FLASH
    assign shift_en = (counter >= counter_limit);
    
    shiftreg 
        #(.NB_LEDS (N_LEDS))
    u_shiftreg (
        .o_led(o_led_from_SR),
        .i_reset(i_reset),
        .i_enable(shift_en),
        .i_shift_dir(i_sw[3]),
        .clock(clock)
        );
    
    flash
        #(.NB_LEDS(N_LEDS))
    u_flash (
        .o_led(o_led_from_Flash),
        .i_reset(i_reset),
        .i_enable(shift_en),
        .clock(clock)
    );

    assign o_led_from_mux = (mode_sel) ? o_led_from_SR : o_led_from_Flash;

//SELECCION DEL COLOR DE SALIDA    
    assign o_led_r = (color_sel[0]) ? o_led_from_mux : {N_LEDS{1'b0}};
    assign o_led_g = (color_sel[1]) ? o_led_from_mux : {N_LEDS{1'b0}};
    assign o_led_b = (color_sel[2]) ? o_led_from_mux : {N_LEDS{1'b0}};
    assign o_led = {color_sel, mode_sel};


endmodule