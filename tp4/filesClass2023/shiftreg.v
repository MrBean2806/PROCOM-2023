
module shiftreg
#(
    parameter  NB_LEDS = 4
)
(
    output [NB_LEDS - 1 : 0]    o_led  ,
    input                       i_valid,
    input                       i_reset,
    input                       clock
);
    

    // Vars
    reg [NB_LEDS - 1 : 0] shiftregister;

    // OP1 For
    // integer ptr;

    always @(posedge clock) begin
        if(i_reset) begin
            shiftregister <= {{NB_LEDS-1{1'b0}},1'b1};//4'b0001;
        end
        else if (i_valid) begin
            
            // //////////////////////////////////
            // // OP1 FOR
            // for(ptr=0;ptr<NB_LEDS-1;ptr=ptr+1) begin
            //     shiftregister[ptr+1] <= shiftregister[ptr];
            // end
            // shiftregister[0] <= shiftregister[NB_LEDS-1];
            // //////////////////////////////////

            // shiftregister <= shiftregister << 1;
            // shiftregister[0] <= shiftregister[NB_LEDS-1];

            shiftregister <= {shiftregister[NB_LEDS-2:0],shiftregister[NB_LEDS-1]};            
        end
        else begin
            shiftregister <= shiftregister;
        end
        
    end

    assign o_led = shiftregister;

endmodule