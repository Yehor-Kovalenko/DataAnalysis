import random

import matplotlib.pyplot as plt
import numpy as np


class KMeans:

    def __init__(self, data, k):
        self.k = k
        self.data = data
        self.centroids = []

    def draw_lin(self, dane, label):
        x = list(range(2, len(dane) + 2))
        plt.scatter(x, dane, label=f'{label}', color='darkblue')
        plt.plot(x, dane, linestyle='-', color='darkblue', marker='o')
        plt.xlabel('k')
        plt.ylabel(f'{label}')
        plt.grid(True)
        plt.show()

    def draw_scatter(self, clusters, cecha1, cecha2, cecha1_nazwa, cecha2_nazwa):
        colours = ['b', 'g', 'y']
        centr_x = [float(cent[cecha1]) for cent in self.centroids]
        centr_y = [float(cent[cecha2]) for cent in self.centroids]
        for i, cluster in enumerate(clusters):
            x = [float(point[cecha1]) for point in cluster]
            y = [float(point[cecha2]) for point in cluster]
            plt.scatter(x, y, color=colours[i])
            plt.plot(centr_x[i], centr_y[i], '+', markersize=12, color="red")
        plt.xlabel(f'{cecha1_nazwa}')
        plt.ylabel(f'{cecha2_nazwa}')
        plt.grid(True)
        plt.show()

    def fit(self):
        prev_centroids = [[] for _ in range(self.k)]
        for i in range(self.k):
            self.centroids.append(random.choice(self.data))
        does_not_stop = True
        iterations = 0

        while self.centroids != prev_centroids:
            clusters = [[] for _ in range(self.k)]
            iterations = iterations + 1
            for j, point in enumerate(self.data):
                distances = []
                for centroid in self.centroids:
                    distance = 0
                    distance += self._distance_to_centroid(point, centroid)
                    distances.append(distance)
                min_distance_id = np.argmin(distances)
                clusters[min_distance_id].append(point)
            prev_centroids = self.centroids
            self.centroids = [self._mean(cluster) for cluster in clusters]
            for i, centroid in enumerate(self.centroids):
                if np.isnan(centroid).any():  # Catch any np.nans, resulting from a centroid having no points
                    self.centroids[i] = prev_centroids[i]
        return [clusters, iterations]

    def _mean(self, cluster):  # cluster is list of points with unknown amount of coordinates
        coordinates = list(zip(*cluster)) #transpose list
        summary=[0 for _ in range(len(coordinates))]
        for i in range(len(coordinates)):
            coordinates[i] = [float(element) for element in coordinates[i]]
            summary[i] += sum(coordinates[i])
        answer=[]
        for mean in summary:
            answer.append(mean / len(coordinates[0]))
        return answer

    def _distance_to_centroid(self, point, centroid):
        distance = 0
        for j in range(len(centroid) - 1):
            distance += abs(float(point[j]) - float(centroid[j])) ** 2
        return np.sqrt(distance)

    def wcss(self, clusters):
        summary = 0
        i = 0
        for cluster in clusters:
            for point in cluster:
                summary += self._distance_to_centroid(point, self.centroids[i]) ** 2
            i += 1
        return summary


