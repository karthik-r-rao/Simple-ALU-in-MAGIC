# Simple-ALU-in-MAGIC
A primitive 8-bit ALU implemented in MAGIC and simulated using the switch-level simulator IRSIM. 

The ALU can perform the following functions:
* Addition
* Subtraction
* Bitwise Ops- AND, XOR, OR

The command files for the simulation on IRSIM are generated automatically using **generateTest.py** and verified for correctness by **checkALU.py**. 

Set a parameter $ITERATIONS in **testALU.sh** before running it. This controls the number of times the command files are generated and the ALU's outputs are tested. Increase this parameter for more extensive testing. Decrease it if you are satisfactory with the coverage. 
