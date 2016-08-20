# comutation
Data and code for paper: Comutation_rules

First run the python code in "\H3N2" or "\H1N1" or "fluB"
----- output: MutMatrix.txt 


Then use "MutMatrix.txt" as input and run matlab code 
---- output:  forARM_MutMatrix.csv


.csv ---> .dat (just need to remove the duplicate space)
And then run Association Rule Mining (ARM) at HPC "/home/hchen009/AssocRuleMining"
Command (e.g. supp=1000, conf=0.7):
./lcm Cf -a 0.7 forARM_MutMatrix.dat 1000 out_rules_1k_0-7_all.dat


------------------------------------------ for Visualization ------------------------------------------

Extract rules from the results of ARM (see below for example)
the rule "164 <= 137 193" will be changed to "164 137 193"
And run the matlab code again


.csv ---> .sif
Visualize the rules in Cytoscape
