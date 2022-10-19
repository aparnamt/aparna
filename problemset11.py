#!usr/ bin/ env python3
#define 
sequence='GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCT'
gene_name='dna1'
species_name='Setaria tundra'
def at_content(sequence):
  length=len(sequence)
  a_count=sequence.count('A')
  t_count=sequence.count('T')
  at_content=(a_count+t_count)/length
  return at_content
print(at_content(sequence))
