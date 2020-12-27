# -*- coding: utf-8 -*-
"""
@author: karthikrao
"""

# script for generating cmd files with IRSIM commands

import sys
import random

batch = int(sys.argv[1])

batch_size = 1000  # number of samples in each IRSIM simulation
cmdpath = 'cmd/'
logpath = 'logfiles/'
fname = cmdpath + "ALU" + str(batch) + ".cmd"
destName = logpath + 'ALU' + str(batch) + '.txt'
step = 50 # step size of IRSIM simulator
vdd = 'vdd'
vss = 'vss'
nodes_opA = ['A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1', 'A0']
nodes_opB = ['B7', 'B6', 'B5', 'B4', 'B3', 'B2', 'B1', 'B0']
nodes_sum = ['sum7', 'sum6', 'sum5', 'sum4', 'sum3', 'sum2', 'sum1', 'sum0']
nodes_and = ['and7', 'and6', 'and5', 'and4', 'and3', 'and2', 'and1', 'and0']
nodes_or = ['or7', 'or6', 'or5', 'or4', 'or3', 'or2', 'or1', 'or0']
nodes_xor = ['xor7', 'xor6', 'xor5', 'xor4', 'xor3', 'xor2', 'xor1', 'xor0']
nodes_alufn = ['select1', 'select0']
nodes_aluout = ['ALU_OUT7', 'ALU_OUT6', 'ALU_OUT5', 'ALU_OUT4', 'ALU_OUT3', 'ALU_OUT2', 'ALU_OUT1', 'ALU_OUT0']
nodes_in = nodes_opA + nodes_opB + nodes_alufn + ['MODE'] 
bit_length = len(nodes_in)

vector_opA = 'A'
vector_opB = 'B'
vector_sum = 'SUM'
vector_and = 'AND'
vector_or = 'OR'
vector_xor = 'XOR'
vector_alufn = 'ALUFN'
vector_aluout = 'ALU_OUT'
vector_cout = 'COUT'


f = open(fname, "w")
f.write(f'logfile {destName}\n')
f.write(f'stepsize {step}\n')
f.write(f'h {vdd}\n')
f.write(f'l {vss}\n')
f.write(f'vector {vector_opA}')
for node in nodes_opA:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_opB}')
for node in nodes_opB:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_sum}')
for node in nodes_sum:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_and}')
for node in nodes_and:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_or}')
for node in nodes_or:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_xor}')
for node in nodes_xor:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_alufn}')
for node in nodes_alufn:
    f.write(f' {node}')
f.write('\n')
f.write(f'vector {vector_aluout}')
for node in nodes_aluout:
    f.write(f' {node}')
f.write('\n')
f.write(f"vector in")
for node in nodes_in:
    f.write(f' {node}')
f.write('\n')
f.write(f"w in {vector_aluout} {vector_cout}\n")

for i in range(batch_size):
    x = random.randint(0, 2**bit_length) # generate a random 19 bit number
    f.write(f"setvector in {x:019b}\n")
    f.write('s\n')
f.write('logfile\n')
f.write('exit')
f.close()