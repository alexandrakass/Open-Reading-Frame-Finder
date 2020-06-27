# Open-Reading-Frame-Finder
This project was created to improve the algorithm for open reading frame finders

The goal is to create an improved version of previously written ORF algorithms that is more intuitive and easier for a user to understand. This project uses the psudo-code from https://iopscience.iop.org/article/10.1088/1742-6596/1341/9/092010/pdf to write an open reading frame (ORF) finder in python. The logic from this paper needed a bit of revising as section 3.3 didn't take into consideration checking if the start and stop codons were in the same reading frame. This code fixes that problem and outputs a list of dictionaries for each reading frame where the identifer is the key and a list of tuples is the value. The tuples hold the range where the reading frame index in the sequence starts and stops translation.


# Requirements to run this code -
 - IDE that can run python 3.5
 - SeqIO from the Bio Python library
 - FASTA file to test and run the code
 - The path of the directory where the FASTA files are stored
 
 
