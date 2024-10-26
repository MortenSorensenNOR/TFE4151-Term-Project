
module AddressDec(input [2:0] a, output [7:0] w);   
	wire [2:0] nota;
    not (nota[0], a[0]);
    not (nota[1], a[1]);
    not (nota[2], a[2]);

    wire T0, T1, T2, T3;

    and U0 (T0, nota[2], nota[1]);
    and U1 (T1, nota[2],    a[1]);
    and U2 (T3,    a[2], nota[1]);
    and U3 (T4,    a[2],    a[1]);

    and U4 (w[0], T0, nota[0]);
    and U5 (w[1], T0,    a[0]);
    and U4 (w[0], T1, nota[0]);
    and U5 (w[1], T1,    a[0]);
    and U4 (w[0], T2, nota[0]);
    and U5 (w[1], T2,    a[0]);
    and U4 (w[0], T3, nota[0]);
    and U5 (w[1], T3,    a[0]);
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



   