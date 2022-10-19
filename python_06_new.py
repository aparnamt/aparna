#!usr/bin/env python3
fasta_obj=open("Python_06.seq.txt","r")
count=0
totalchara = 0
for line in fasta_obj:
  line=line.rstrip() 
  count=count+1
  totalchara = totalchara + len(line)
print(count)
print(totalchara)
#line_length=len(line)
#print(line_length)
avg_ll=totalchara/count
print(avg_ll)

 


 



