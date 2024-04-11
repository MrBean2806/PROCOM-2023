module flash
#(
    parameter  NB_LEDS = 4
)
(
    output [NB_LEDS - 1 : 0]    o_led  ,
    input                       i_reset,
    input                       i_enable,
    input                       clock
);
    // Vars
    reg [NB_LEDS - 1 : 0] shiftregister;

    always @(posedge clock or negedge i_reset) begin
        if(!i_reset) begin
            shiftregister <= {NB_LEDS{1'b1}}; 
        end
        else if (i_enable) begin
            shiftregister <= ~shiftregister;            
        end
    end

    assign o_led = shiftregister;

endmodule