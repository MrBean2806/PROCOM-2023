//modulo shiftreg modificado
module shiftreg
#(
    parameter  NB_LEDS = 4
)
(
    output [NB_LEDS - 1 : 0]    o_led  ,
    input                       i_reset,
    input                       i_enable,
    input                       i_shift_dir,
    input                       clock
);
    // Vars
    reg [NB_LEDS - 1 : 0] shiftregister;

    always @(posedge clock or negedge i_reset) begin
        if(!i_reset) begin
            shiftregister <= {{NB_LEDS-1{1'b0}},1'b1};  //4'b0001;
        end
        else if (i_enable) begin
            if(i_shift_dir)     //desplazamiento hacia la izquierda
                shiftregister <= {shiftregister[NB_LEDS-2:0],shiftregister[NB_LEDS-1]};            
            else                //desplazamiento hacia la derecha
                shiftregister <= {shiftregister[0],shiftregister[NB_LEDS-1:1]};            
        end
        else begin
            shiftregister <= shiftregister;
        end
    end

    assign o_led = shiftregister;

endmodule