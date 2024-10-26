`timescale 1ns/1ps

module tb_memory_unit ();
    localparam unsigned CLOCK_PERIOD_HALF = 5;

    reg clk;
    reg op;
    reg select;
    reg [2:0] addr;

    reg [7:0] r_data_in;
    wire [7:0] w_data_out;
	
    memory_unit memory_unit_inst (
        .clk(clk),
        .op(op),
        .select(select),
		.addr(addr),
        .data_in(r_data_in),
        .data_out(w_data_out)
    );

    // Generate clock
    initial begin
        clk = 0;
        forever begin
            clk = ~clk;
            #CLOCK_PERIOD_HALF;
        end
    end

    // Generate data sigals
    initial begin
        op = 0; select = 0; addr = '0; r_data_in = '0;

        #40 select = 1; op = 1; addr = 1; r_data_in = 8'b01001001;
        #20 select = 1; op = 0; addr = 1; r_data_in = '0;
        #10 select = 1; op = 1; addr = 0; r_data_in = 8'b11001100;
        #20 select = 1; op = 1; addr = 7; r_data_in = 8'b00110011;
        #10 select = 1; op = 0; addr = 0; r_data_in = '0;
        #10 select = 1; op = 0; addr = 7; r_data_in = '0;
		
		#20 $finish;
    end

endmodule