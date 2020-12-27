# -*- coding: utf-8 -*-
"""
@author: karthikrao
"""

# script for testing the outputs of the ALU

import sys

batch = int(sys.argv[1])


def unsign2sign(num):
    if num>127:
        num-=256
    return num

def checkAND(opA, opB, aluout):
    expected = opA & opB
    if aluout==expected:
        return True
    return False

def checkADD(opA, opB, aluout, cout):
    expected = opA + opB
    # cout for overflow
    if aluout + 256*cout == expected:
        return True
    return False

def checkSUB(opA, opB, aluout, cout):
    # convert operands to signed decimal
    opA=unsign2sign(opA)
    opB=unsign2sign(opB)
    expected = opA-opB
    # take care of overflow
    if expected<-128 or expected>127:
        aluout-=256*cout
    else:
        aluout=unsign2sign(aluout)
    if aluout==expected:
        return True
    return False

def checkXOR(opA, opB, aluout):
    expected = opA ^ opB
    if aluout==expected:
        return True
    return False

def checkOR(opA, opB, aluout):
    expected = opA | opB
    if aluout==expected:
        return True
    return False

correct=0
testcases=0

f = open('logfiles/ALU' + str(batch) + '.txt', "r")
lines = f.readlines()
for i in range(0, len(lines), 2):
    ele = lines[i].split()
    
    # read data from file
    aluout = (int(ele[1][8:], 2))
    opA = (int(ele[2][3:11], 2))
    opB = (int(ele[2][11:19], 2))
    alufn = (int(ele[2][19:21], 2))
    mode = (int(ele[2][21], 2))
    cout = (int(ele[3][5], 2))
    
    if alufn==3:
        flag=checkAND(opA, opB, aluout)
    elif alufn==2:
        if mode:
            flag=checkSUB(opA, opB, aluout, cout)
        else:
            flag=checkADD(opA, opB, aluout, cout)
    elif alufn==1:
        flag=checkXOR(opA, opB, aluout)
    else:
        flag=checkOR(opA, opB, aluout)
        
    if flag:
        correct+=1
    else:
        print("The following inputs are causing unexpected behaviour-")
        print(f"\topA{opA}, opB:{opB}, alufn:{alufn}, mode:{mode}")
    testcases+=1
    
print(f"Number of test cases correct: {correct}/{testcases}\n")
f.close()