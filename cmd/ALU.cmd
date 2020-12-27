logfile logfiles/ALU0.txt
stepsize 50
h vdd
l vss
vector A A7 A6 A5 A4 A3 A2 A1 A0
vector B B7 B6 B5 B4 B3 B2 B1 B0
vector SUM sum7 sum6 sum5 sum4 sum3 sum2 sum1 sum0
vector AND and7 and6 and5 and4 and3 and2 and1 and0
vector OR or7 or6 or5 or4 or3 or2 or1 or0
vector XOR xor7 xor6 xor5 xor4 xor3 xor2 xor1 xor0
vector ALUFN select1 select0
vector ALU_OUT ALU_OUT7 ALU_OUT6 ALU_OUT5 ALU_OUT4 ALU_OUT3 ALU_OUT2 ALU_OUT1 ALU_OUT0
vector in A7 A6 A5 A4 A3 A2 A1 A0 B7 B6 B5 B4 B3 B2 B1 B0 select1 select0 MODE
w in ALU_OUT COUT
setvector in 1101011010110011100
s
setvector in 0101111010000001101
s
setvector in 0010101100111100011
s
setvector in 1100100110010110011
s
setvector in 0100101101100101001
s
setvector in 1010000110111011111
s
setvector in 1110011110110000101
s
setvector in 0011011011110110100
s
setvector in 1010101011111010011
s
setvector in 0001101010011100000
s
analyzer ALUFN MODE A B COUT ALU_OUT 
logfile