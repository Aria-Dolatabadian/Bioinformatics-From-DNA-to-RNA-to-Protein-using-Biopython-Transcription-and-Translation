from Bio.Seq import Seq
from Bio.SeqUtils import GC
sequence = Seq('ATACGCGAAAAAAAAAACGGATATA')
print(sequence)
#non overlapping count
print(sequence.count('ATA'))
# overlapping count
print(sequence.count_overlap('ATA'))
#GC content
print(GC(sequence))
#Transcription  DNA to RNA
# 1:reverse_complement
coding_dna =Seq('ATGGCCATTGTAATGGGCCGCTGAAGGGTGCCCGATAG')
template_dna =coding_dna.reverse_complement()
print(template_dna)
#2 Transcription
messenger_rna=coding_dna.transcribe()
print(messenger_rna)
#The Seq object also include a back transcription method for going from mRNA  to the cosing strand of the DNA
coding_dna=messenger_rna.back_transcribe()
print(coding_dna)
#Translation RNA to protein
print(messenger_rna.translate())
# we can also translate directly from the coding strand of the DNA
print(coding_dna.translate())
