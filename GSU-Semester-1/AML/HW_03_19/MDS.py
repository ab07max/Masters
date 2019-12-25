import numpy as np
from Bio import SeqIO
from matplotlib import pyplot as plt
from sklearn.manifold import MDS


# Function to calculate the pairwise hamming distance
def calcHammDist(sequence1, sequence2):
    distance = 0
    for index in range(len(sequence1)):
        if sequence1[index].__ne__(sequence2[index]):
            distance += 1
    return distance


# function to visualize the scattering of pairwise hamming distances between sequence 1 and sequence 2
def scatterPlotVisualizer(XCoords, YCoords):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # ax.scatter(XCoords[0:60], YCoords[0:60], c="red")
    # ax.scatter(XCoords[60:120], YCoords[60:120], c="blue")
    ax.scatter(XCoords, YCoords, c="red")
    ax.set_xlabel("Pairwise Hamming Distance - Sequence 1")
    ax.set_ylabel("Pairwise Hamming Distance - Sequence 2")
    ax.set_title("MDS")
    plt.show()
    return


def writeMDSDataToCSV(csvData):
    with open('MDSData.csv', 'w') as writeFile:
        writeFile.write("X-Values" + "," + "Y-Values")
        writeFile.write("\n")
        for entries in csvData:
            writeFile.write("" + str(entries[0]) + "," + str(entries[1]) + "")
            writeFile.write("\n")
    writeFile.close()


if __name__ == '__main__':
    seqList = []
    # parsing the fasta file and storing it in a variable
    fasta_sequences = SeqIO.parse(open('HW4.fas'), 'fasta')
    for fasta in fasta_sequences:
        seqList.append(fasta.seq)

    # initializing the hamming list of elements to zeros
    hammList = np.zeros((len(seqList), len(seqList)))

    # building the hamming distance matrix
    # the shape of this matrix is 120 X 120
    for i in range(len(seqList)):
        for j in range(len(seqList)):
            hammingDist = calcHammDist(seqList[i], seqList[j])
            hammList[i][j] = hammingDist

    # performing the  multi-dimensional scaling on the hamming distance matrix
    # n_components = 2 - scaling the dimensions to two
    # dissimilarity = 'precomputed' - means that we are specifying the mds that
    # dissimilarities is already computed in the form of pairwise hamming distances
    embedding = MDS(n_components=2, dissimilarity='precomputed')
    hamm_transformed = embedding.fit_transform(hammList)

    # forming the x-coordinates and y-coordinates
    x = hamm_transformed[:, 0]
    y = hamm_transformed[:, 1]

    # performing the visualization
    scatterPlotVisualizer(x, y)

    # write MDS Data to CSV file
    writeMDSDataToCSV(hamm_transformed)
