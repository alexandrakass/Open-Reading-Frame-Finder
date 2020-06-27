from Bio import SeqIO
import os
import Finder
os.getcwd()
os.chdir('C:/Users/alexa/OneDrive/Coursera/Python for Genomic Data Science')


# TODO: Loop through a FASTA file and store each identifier in a value and the sequence in a key
my_seq = Finder.parse_fasta("test.fasta")
Finder.quickView(my_seq)
print("Number of identifiers = ", len(my_seq))
# Get each identifier and sequence and store them in a dict
seq_dict = {}
for i, record in enumerate(my_seq):
    seq_dict[record.id] = record.seq.lower()


# TODO: Get open reading frames for each identifier in each frame and store them in respective dict
frameOne = {}; frameTwo = {}; frameThree = {};
frameList = [frameOne, frameTwo, frameThree]; orfs = [];


for key, value in seq_dict.items():
    start_Codons = Finder.has_start_codon(str(value))
    stop_Codons = Finder.has_stop_codon(str(value))
    orfs = Finder.find_orf(start_Codons, stop_Codons, 1)
    frameOne[key] = (orfs)

print(frameOne)

'''
for i, frame in range(len(frameList)):
    for key, value in seq_dict.items():
        start_Codons = Finder.has_start_codon(str(value))
        stop_Codons = Finder.has_stop_codon(str(value))
        orfList = Finder.find_orf(start_Codons, stop_Codons, i)

    frame[key] = orfList

print(frameList)
'''


