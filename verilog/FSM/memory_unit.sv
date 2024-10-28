`timescale 1ns/1ps

module memory_unit (
    input wire clk,
    input wire op,
    input wire select,
    input wire [2:0] addr,

    input wire [7:0] data_in,
    output reg [7:0] data_out
);
    // FSM
    wire w_valid;
    wire w_rw;

    fsm fsm_inst (
        .clk(clk),
        .op(op),
        .select(select),
        .valid(w_valid),
        .rw(w_rw)
    );

    // Address Decoder
    wire [2:0] r_addr;
    wire [7:0] wordLine;

    // Register the input address
    d_flip_flop addr_register0 (
        .clk(clk),
        .D(addr[0]),
        .Q(r_addr[0]),
        .Qn()
    );

    d_flip_flop addr_register1 (
        .clk(clk),
        .D(addr[1]),
        .Q(r_addr[1]),
        .Qn()
    );

    d_flip_flop addr_register2 (
        .clk(clk),
        .D(addr[2]),
        .Q(r_addr[2]),
        .Qn()
    );

    AddressDec addr_dec_inst (
        .a(r_addr),
        .w(wordLine)
    );
    
    // TEMP MEMORY
    reg [7:0] memory_array[8];
    always_ff @(posedge clk) begin
        if (w_valid) begin
			case (wordLine)
				8'b00000001: begin
					if (w_rw) begin
		                memory_array[0] <= data_in;
						data_out <= '0;
		            end else begin
		                data_out <= memory_array[0];
		            end
				end
				
				8'b00000010: begin
					if (w_rw) begin
		                memory_array[1] <= data_in;
						data_out <= '0;
		            end else begin
		                data_out <= memory_array[1];
		            end
                end
                
                8'b00000100: begin
					if (w_rw) begin
		                memory_array[2] <= data_in;
		            	data_out <= '0;
					end else begin
		                data_out <= memory_array[2];
		            end
                end
                
                8'b00001000: begin
					if (w_rw) begin
		                memory_array[3] <= data_in;
		            	data_out <= '0;
					end else begin
		                data_out <= memory_array[3];
		            end
                end

                8'b00010000: begin
					if (w_rw) begin
		                memory_array[4] <= data_in;
		            	data_out <= '0;
					end else begin
		                data_out <= memory_array[4];
		            end
				end
				
				8'b00100000: begin
					if (w_rw) begin
		                memory_array[5] <= data_in;
		            	data_out <= '0;
					end else begin
		                data_out <= memory_array[5];
		            end
				end
				
				8'b01000000: begin
					if (w_rw) begin
		                memory_array[6] <= data_in;
		            	data_out <= '0;
					end else begin
		                data_out <= memory_array[6];
		            end
				end

				8'b10000000: begin
					if (w_rw) begin
		                memory_array[7] <= data_in;
		            	data_out <= '0;
					end else begin
		                data_out <= memory_array[7];
		            end
				end
				
				default: begin
					data_out <= '0;
				end
			endcase
        end else begin
			data_out <= '0;
		end
    end
endmodule