#! usr/bin/env python3
genes={}
fasta_obj=open("Python_06.fasta","r")
for line in fasta_obj:
 line=line.rstrip()
 if '>' in line:
  genes[line]=''
  seq=line
 else:
  genes[seq] = genes[seq] + line
print(genes)








