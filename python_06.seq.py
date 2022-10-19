#!usr/bin/env python3
genes={}
seq_read=open("Python_06.seq.txt","r")
for line in seq_read:
  line=line.rstrip()
  gene_id,seq=line.split()
  genes[gene_id]=seq
print(genes)


