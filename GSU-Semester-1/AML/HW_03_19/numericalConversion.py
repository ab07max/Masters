import numpy as np
from Bio import SeqIO

# Read the DNA Sequences from .fas file
fasta_sequences = SeqIO.parse(open('HW4.fas'), 'fasta')

# create a list of sequences
seqList = []
for fasta in fasta_sequences:
    seqList.append(fasta.seq)

# create a matrix for length of each DNA String - 264 for total number of sequences - 120
freqMatrix = np.zeros((len(seqList), 264))

# for every sequence assign a numerical value to the primary units G, A, C, T
for sequence, i in zip(seqList, range(len(seqList))):
    for ch, j in zip(sequence, range(len(sequence))):
        if ch == 'G':
            freqMatrix[i][j] = 1
        if ch == 'A':
            freqMatrix[i][j] = 2
        if ch == 'C':
            freqMatrix[i][j] = 3
        if ch == 'T':
            freqMatrix[i][j] = 4

print(freqMatrix)
