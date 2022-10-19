#! usr/bin/env python3
from Bio import SeqIO
count_seq=0
short_seq=0
first_line=True
for seq_record in SeqIO.parse("Python_08.fasta","fasta"):
  #short_seq=len(seq_record)
  if first_line==True:
     #short_seq=len(seq_record.seq)
     long_seq=len(seq_record.seq)
     first_line=False
 #   print('first line',short_seq)
 # print('ID',seq_record.id)
 # print('Sequence',seq_record.seq)
  #print(seq_record)  
#  print('Length',len(seq_record.seq))
  count_seq=count_seq+1
  #if short_seq <len(seq_record.seq):
   # short_seq=len(seq_record.seq)
   # print('short seq:',short_seq)
  #else:
   # short_seq=len(seq_record.seq)
#print(count_seq)
 # if long_seq>len(seq_record.seq)
  #   long_seq=len(seq_record.seq)
   #  print('longseq is',long_seq)
 # else:
  #     long_seq=len(seq_record.seq)
#length=len(seq_record)
#print('length is:',length)

avg_length=len(seq_record)/count_seq
#print(avg_length)


#print('shortest seq length',short_seq)
#print('long seq is:'long_seq)
g_count= seq.count(seq_record)
print(g_count)



