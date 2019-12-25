import numericalConversion
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd


# function to visualize the scattering of pairwise hamming distances between sequence 1 and sequence 2
def scatterPlotVisualizer(XCoords, YCoords):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(XCoords, YCoords, c="blue")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("PCA")
    plt.show()
    return


def writePCADataToCSV(csvData):
    with open('PCAData.csv', 'w') as writeFile:
        writeFile.write("X-Values" + "," + "Y-Values")
        writeFile.write("\n")
        for entries in csvData:
            writeFile.write("" + str(entries[0]) + "," + str(entries[1]) + "")
            writeFile.write("\n")
    writeFile.close()


if __name__ == '__main__':
    originalMatrix = numericalConversion.freqMatrix
    # to calculate the eigen values and eigen vectors
    covar_matrix = PCA(n_components=2)

    # We perform data preprocessing using StandardScaler()
    originalMatrix = StandardScaler().fit_transform(originalMatrix)
    principalComponents = covar_matrix.fit_transform(originalMatrix)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['principal component 1', 'principal component 2'])

    x = principalComponents[:, 0]
    y = principalComponents[:, 1]

    # performing the visualization
    scatterPlotVisualizer(x, y)

    # write MDS Data to CSV file
    writePCADataToCSV(principalComponents)
