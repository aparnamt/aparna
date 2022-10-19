#!usr/bin/env python3
import re
string='''>gi|170746|gb|M12277.1|WHTH4091 Wheat histone H4 TH091 gene, complete cds
AGCACCCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACGTCGCATCTCCACCGTCTCGCGGATCG
ACCCAGCGAAGTCCCTCCCGCCCCCAAAGTCCCCCAAATCTTGCAGTTCCCTCCTAAATCCTCCCCATAT
AAACCAACCCCCCGCCCTCAGATCCCTAATCCCATCGCAAGCATCAGACTCCCTCCAAAGCAGGCAGCAG
CTCCTCTTCTTCCTAATCACACTATCTCGGAGAGGAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGG
GGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCC
GGCGATCCGGAGGCTGGCCAGGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGC
GGCGTCCTCAAGATCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCA
AAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCTTCGGAGG
CTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTGATCTGTGCTGTCGTAGATGAGATTTACTG
ATTTGGCGTGCGCCGGTTGTATTCTGTCATGGGGTTCAGTGGGCTGTGTAATACCTTGCTCTGTACTTCT
GTTCAATGCAATCACTTCTATTCTGGi
>gi|603555|emb|X83548.1| H.sapiens gene for histone H4
TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGG
AAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAA
GATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCCTTTTCCATTT
TTTCCTGAAGTCGTGGGCAGGGCGCAAGGTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTT
CCCAATCAGGTCCGATTTATTACTATATAAAGTACTGCTGCGAGGCTTGCCGTGTTGCATTTTGTTTAGT
ACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCAAA
GTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGTGGAGGCGTTA
AGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTAATCCG
CGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTC
AAGCGCCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAG
GCCCTTCTCAGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAAC
ACTTAAACGTATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGT
GCCCCTTTCAGCATTACTTAGTGGTTAAA'''
pattern=r"^>\w+\S+\s?.*"
patfind=re.findall(pattern,string)
print(patfind)
