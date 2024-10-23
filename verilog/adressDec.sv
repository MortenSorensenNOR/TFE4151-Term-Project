
module AddressDec(input [2:0] a, output [7:0] w);   

	wire [2:0] nota;
	
	assign nota = ~a;
	
	assign w[0] = nota[2] & nota[1] & nota[0];    
    assign w[1] = nota[2] & nota[1] &    a[0];
    assign w[2] = nota[2] &    a[1] & nota[0];
    assign w[3] = nota[2] &    a[1] &    a[0];           
    assign w[4] =    a[2] & nota[1] & nota[0];    
    assign w[5] =    a[2] & nota[1] &    a[0];
    assign w[6] =    a[2] &    a[1] & nota[0];
    assign w[7] =    a[2] &    a[1] &    a[0];
	
endmodule



module adressTestbench();

    reg [2:0] a;        // Input to the address decoder
    wire [7:0] w;       // Output from the address decoder
    
    // Instantiate the address decoder module
    AddressDec uut(
        .a(a),
        .w(w)
    );
    											  
    // Test all possible values of input a
    initial begin
        // Monitor the input and output values
        $monitor("Time = %0d, a = %b, w = %b", $time, a, w);

        // Apply test cases
        a = 3'b000; #10;
        a = 3'b001; #10;
        a = 3'b010; #10;
        a = 3'b011; #10;
        a = 3'b100; #10;
        a = 3'b101; #10;
        a = 3'b110; #10;
        a = 3'b111; #10;

        // Finish the simulation
        $finish;
    end

endmodule



   