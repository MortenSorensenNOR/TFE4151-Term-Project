module bitCell(
	input rw,   // readWrite operation variables
	input wordLine,   // wordLine, indicating that the word this bit is part of should be written to
	input i, 		  // the bit of the input-word that should be written to this cell
	input bitCarry,   // the output from the same bit in the words above this one
	output bitOut,	  // output from this bit to the bitline
	
	//ONLY INCLUDE NEXT LINE IF TESTING
	output [1:0] Q       // Exposing the Q and Q inverse (flip-flop state)
);														

	wire [1:0] readWrite;																	  	
	and U1 (readWrite[0], ~rw, wordLine);	//read
	and U2 (readWrite[1],  rw, wordLine);   //write
	
	// defining some wires
	wire [1:0] temp;  // wires between and and crosslinked nands
	wire [1:0] temp2;  // wires between and and crosslinked nands	
	
	//UNCOMMENT NEXT LINE WHEN NOT TESTING
	//wire [1:0] Q;     // Q and Q inverse
	
	// assigning the wires				   
	and U3 (temp[0], readWrite[1],  i);  
	and U4 (temp[1], readWrite[1], ~i);  
									
																  
	nor U5 (Q[0], temp[0], Q[1]);
	nor U6 (Q[1], temp[1], Q[0]);
	
	// defining and assigning wires for the bitLine
	wire bitLineTemp;								 
	and U7 (bitLineTemp, Q[1], readWrite[0]);
													
	or U8 (bitOut, bitCarry, bitLineTemp);
	
endmodule 		 








module bitCellTestbench();
    reg rw;               // Read/Write control signal
    reg wordLine;         // Wordline signal
    reg i;                // Input bit to write to the bit cell
    reg bitCarry;         // Bit carry from above
    wire bitOut;          // Output bit from the bit cell
    wire [1:0] Q;         // Flip-flop state (Q and Q inverse)
    
    // Instantiate the bitCell module
    bitCell uut (
        .rw(rw),
        .wordLine(wordLine),
        .i(i),
        .bitCarry(bitCarry),
        .bitOut(bitOut),
        .Q(Q)   // Capture the flip-flop state
    );
    
    // Test sequence
    initial begin
        // Initialize variables
        $monitor("Time = %0d, rw = %b, wordLine = %b, i = %b, bitCarry = %b, bitOut = %b, Q = %b", 
                 $time, rw, wordLine, i, bitCarry, bitOut, Q);

        // Test case 1: Write operation (rw = 1, wordLine = 1)	
        $display(" ");
        $display("Test case 1: Write operation (rw = 1, wordLine = 1, i = 1)");
        rw = 1; wordLine = 1; i = 1; bitCarry = 0; #10;
        						  
        $display(" ");
        $display("Test case 2: Write operation (rw = 1, wordLine = 1, i = 0)  (og så tilbake til 1)");
        rw = 1; wordLine = 1; i = 0; bitCarry = 0; #10;				
        rw = 1; wordLine = 1; i = 1; bitCarry = 0; #10;

        // Test case 3: Read operation (rw = 0, wordLine = 1) 
        $display(" ");
        $display("Test case 3: Read operation (rw = 0, wordLine = 1, i = 0)");
        rw = 0; wordLine = 1; i = 0; bitCarry = 0; #10;
			  
        $display(" ");
        $display("Test case 4: Read operation (rw = 0, wordLine = 1, i = 1)");
        rw = 0; wordLine = 1; i = 1; bitCarry = 0; #10;

        // Test case 5: Wordline disabled (wordLine = 0, should not affect bitOut)
        $display(" ");
        $display("Test case 5: Wordline disabled (wordLine = 0)  (set to 0 with wordline, and then try to change back w/o wordline)");	
        rw = 1; wordLine = 1; i = 0; bitCarry = 0; #10;	
        rw = 1; wordLine = 0; i = 1; bitCarry = 0; #10;
        													  
        $display(" ");
        $display("Test case 6: Wordline disabled (wordLine = 0) (set to 1, and try to read w/o wordline)");	 
        rw = 1; wordLine = 1; i = 1; bitCarry = 0; #10;	
        rw = 0; wordLine = 0; i = 0; bitCarry = 0; #10;

        // Test case 7: Carry bit logic			 
        $display(" ");
        $display("Test case 7: Carry bit logic, bitCarry = 1 (try to read without wordline, with either valuable in Q)");
        rw = 0; wordLine = 0; i = 0; bitCarry = 1; #10;	
        rw = 1; wordLine = 1; i = 0; bitCarry = 0; #10;		   
        rw = 0; wordLine = 0; i = 0; bitCarry = 1; #10;	
													   

        // End of the test
        $finish;
    end
endmodule