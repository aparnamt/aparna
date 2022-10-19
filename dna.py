#! usr/bin/env python3
nt_count={}
dna='ATGCGCTAGCTACGCTAHATCGCTCGATCGC'
unique=set(dna)
print("unique nt:",unique)
for nt in unique:
  count=dna.count(nt)
  nt_count[nt]=count
print("nt count:",nt_count)


