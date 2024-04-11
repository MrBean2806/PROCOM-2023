// Shift Leds

`define N_LEDS 4
`define NB_SEL 2
`define NB_COUNT 32
`define NB_SW 4

module shiftleds
  #(
    parameter N_LEDS    = `N_LEDS    ,
    parameter NB_SEL    = `NB_SEL    ,
    parameter NB_COUNT  = `NB_COUNT  ,
    parameter NB_SW     = `NB_SW
    )
   (
    output [N_LEDS - 1 : 0] o_led   ,
    output [N_LEDS - 1 : 0] o_led_b ,
    output [N_LEDS - 1 : 0] o_led_g ,
    input [NB_SW   - 1 : 0] i_sw    ,
    input                   i_reset ,
    input                   clock
    );

   // Localparam
   localparam R0       = (2**(NB_COUNT-10))-1 ;
   localparam R1       = (2**(NB_COUNT-9))-1  ;
   localparam R2       = (2**(NB_COUNT-8))-1  ;
   localparam R3       = (2**(NB_COUNT-7))-1  ;

   localparam SEL0     = `NB_SEL'h0           ;
   localparam SEL1     = `NB_SEL'h1           ;
   localparam SEL2     = `NB_SEL'h2           ;
   localparam SEL3     = `NB_SEL'h3           ;

   // Vars
   wire [NB_COUNT - 1 : 0] ref_limit ;
   reg [NB_COUNT  - 1 : 0] counter   ;
   reg [N_LEDS    - 1 : 0] shiftreg  ;
   wire                    reset     ;
   
   wire [NB_SW-1:0] sw_from_vio;
   wire reset_from_vio;
   wire sel_mux;
   wire [NB_SW-1:0] sw_w;


   assign sw_w = (sel_mux) ? sw_from_vio : i_sw;
   assign reset = (sel_mux) ? ~reset_from_vio : ~i_reset;
   assign ref_limit = (i_sw[(NB_SW-1)-1 -: NB_SEL]==SEL0) ? R0 :
                      (i_sw[(NB_SW-1)-1 -: NB_SEL]==SEL1) ? R1 :
                      (i_sw[(NB_SW-1)-1 -: NB_SEL]==SEL2) ? R2 : R3;

   always@(posedge clock or posedge reset) begin
      if(reset) begin
         counter  <= {NB_COUNT{1'b0}};
         shiftreg <= {{N_LEDS-1{1'b0}},{1'b1}};
      end
      else if(i_sw[0]) begin
         if(counter>=ref_limit) begin
            counter  <= {NB_COUNT{1'b0}};
            shiftreg <= {shiftreg[N_LEDS-2 -: N_LEDS-1],shiftreg[N_LEDS-1]};
      end
         else begin
            counter  <= counter + {{NB_COUNT-1{1'b0}},{1'b1}};
            shiftreg <= shiftreg;
         end
      end
      else begin
         counter  <= counter;
         shiftreg <= shiftreg;
      end // else: !if(i_sw[0])
   end // always@ (posedge clock or posedge reset)

   assign o_led   = shiftreg;
   assign o_led_b = (i_sw[3]==1'b0) ? shiftreg : {N_LEDS{1'b0}};
   assign o_led_g = (i_sw[3]==1'b1) ? shiftreg : {N_LEDS{1'b0}};
   
    ila
    u_ila
   (.clk_0(clock),
    .probe0_0(o_led),
    .probe1_0(o_led_b),
    .probe2_0(o_led_g));

    vio
    u_vio
   (.clk_0(clock),
    .probe_in0_0(o_led),
    .probe_in1_0(o_led_b),
    .probe_in2_0(o_led_g),
    .probe_out0_0(sel_mux),
    .probe_out1_0(reset_from_vio),
    .probe_out2_0(sw_from_vio));

endmodule // shiftleds
