#!/bin/bash
ITERATIONS=10
batch=0
while [ $batch -lt $ITERATIONS ]
do
	echo "Current batch is $batch..."
	python3 generateTest.py $batch 
	irsim scmos100.prm magic/ALU.sim -cmd/ALU${batch}.cmd
	echo "Batch $batch has finished execution. Check its log at logfiles/ALU${batch}.txt"
	echo "Verifying the ALU outputs..."
	python3 checkALU.py $batch
	batch=`expr $batch + 1`
done