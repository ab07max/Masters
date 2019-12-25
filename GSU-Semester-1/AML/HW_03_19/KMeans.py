from copy import deepcopy
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

'''
Approach for K-Means Algorithm is as follows:
1. Read either MDS Data or PCA data 
2. Modify the code as commented
3. Given the data set, set the number of clusters and assign some random values as centroids.
4. for each data point in the data set, classify the data point as their association with a 
    cluster based on the euclidean distance between the data point and centroid
5. After the clusters are formed, calculate the new centroid by evaluating the mean of values of
    cluster points. And repeat the process until the difference between successive centroids is minimum
'''


def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


def findCentroids(X, n):
    # X coordinates of random centroids
    # the centroids are chosen randomly and they're given values
    # range from 0 to maxvalue of set - 20 for MDS Data set
    # and from 0 to maxvalue of set - 6 for PCA Data set
    C_x = np.random.randint(0, np.max(X) - 20, size=n)

    # Y coordinates of random centroids
    C_y = np.random.randint(0, np.max(X) - 20, size=n)
    C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
    plt.scatter(f1, f2, c='#050505', s=7)
    plt.scatter(C_x, C_y, marker='*', s=200, c='g')
    return C


def clusteredPlot(C, Data):
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    fig, ax = plt.subplots()
    for i in range(k):
        points = np.array([Data[j] for j in range(len(Data)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
    ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')
    plt.show()


# Driver Code
if __name__ == '__main__':

    # read data from the csv file
    # the data of Multi-dimensional scaling is in MDSData.csv
    # the data of Principal component Analysis is in PCAData.csv
    data = pd.read_csv('MDSData.csv')
    f1 = data['X-Values'].values
    f2 = data['Y-Values'].values
    X = np.array(list(zip(f1, f2)))

    # Number of clusters = 3 (Let's say)
    k = 2
    centroids = findCentroids(X, k)

    # To store the value of centroids when it updates
    C_old = np.zeros(centroids.shape)

    clusters = np.zeros(len(X))
    # Error func. - Distance between new centroids and old centroids
    error = dist(centroids, C_old, None)
    # Loop will run till the error becomes zero
    while error != 0:
        # Assigning each value to its closest cluster
        for i in range(len(X)):
            distances = dist(X[i], centroids)
            cluster = np.argmin(distances)
            clusters[i] = cluster
        # Storing the old centroid values
        C_old = deepcopy(centroids)
        # Finding the new centroids by taking the average value
        for i in range(k):
            points = [X[j] for j in range(len(X)) if clusters[j] == i]
            centroids[i] = np.mean(points, axis=0)
        error = dist(centroids, C_old, None)
    clusteredPlot(centroids, X)
