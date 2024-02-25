import matplotlib.pyplot as plt
import numpy as np


class KNN:
    def __init__(self, data_train, data_test):
        self.k = 0
        self.data_train = self.normalize(data_train)
        self.data_test = self.normalize(data_test)
        self.sets = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 2, 3]]
        self.str_sets = [["Długość działki kielicha", "Szerokość działki kielicha"],
                         ["Długość działki kielicha", "Długość płatka"],
                         ["Długość działki kielicha", "Szerokość płatka"],
                         ["Szerokość działki kielicha", "Długość płatka"],
                         ["Szerokość działki kielicha", "Szerokość płatka"],
                         ["Długość płatka", "Szerokość płatka"],
                         ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]]

    def normalize(self, arr):
        normalized = arr
        for i in range(4):
            max_value = self.find_max(arr, i)
            for j in range(0, len(arr)):
                normalized[j][i] = float(arr[j][i]) / max_value
        return normalized

    def find_max(self, arr, param):
        tmp = []
        for i in range(len(arr)):
            tmp.append(float(arr[i][param]))
        return max(tmp)

    def sort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    tmp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = tmp
        return arr

    def qualifier(self, p0, p1, p2):
        if p0 > p1 and p0 > p2:
            return 0
        elif p1 > p0 and p1 > p2:
            return 1
        elif p2 > p0 and p2 > p1:
            return 2
        else:
            return 3

    def draw(self, shortest0, shortest1, shortest2):
        if shortest0 <= shortest1 and shortest0 <= shortest2:
            return 0
        elif shortest1 <= shortest0 and shortest1 <= shortest2:
            return 1
        else:
            return 2

    def guess_type(self, sorted_distances):
        p0 = p1 = p2 = 0
        shortest0 = shortest1 = shortest2 = 0
        for i in range(self.k):
            if (sorted_distances[i][1] == '0'):
                p0 = p0 + 1
                shortest0 = min(shortest0, float(sorted_distances[i][0]))
            elif (sorted_distances[i][1] == '1'):
                p1 = p1 + 1
                shortest1 = min(shortest1, float(sorted_distances[i][0]))
            else:
                p2 = p2 + 1
                shortest2 = min(shortest2, float(sorted_distances[i][0]))
        if self.qualifier(p0, p1, p2) != 3:
            return self.qualifier(p0, p1, p2)
        else:
            return self.draw(shortest0, shortest1, shortest2)


    def classification(self, test_point, set_number):
        distances = []
        for k in range(len(self.data_train)):
            distance = 0
            for i in self.sets[set_number]:
                distance = distance + ((float(test_point[i]) - float(self.data_train[k][i])) ** 2)
            distances.append([np.sqrt(distance), self.data_train[k][4]])
        return self.guess_type(self.sort(distances))

    def matrix(self, arr):
        for i, j in enumerate(arr):
            if i % 3 == 0:
                print('    setosa', j)
            elif i % 3 == 1:
                print('versicolor', j)
            else:
                print(' virginica', j)

    def mistake_matrix(self, arr, original_type, checked_type):
        arr[original_type][checked_type] += 1
        return arr

    def plots(self, values, set_number):
        counted_neighbours = list(range(1, 16))
        title = "Badane cechy: "
        if len(self.str_sets[set_number]) == 4:
            title = "Badane cechy: Wszystkie"
        else:
            for i in range(len(self.str_sets[set_number])):
                title = title + self.str_sets[set_number][i]
                if i < (len(self.str_sets[set_number]) - 1):
                    title = title + ", "
        plt.ylim(0, 110)
        plt.bar(counted_neighbours, values, color='darkblue')
        plt.xticks(counted_neighbours)
        plt.xlabel('k sąsiadów')
        plt.ylabel('Wartości [%]')
        plt.title(title)
        plt.show()

    def kNN(self):
        for j in range(len(self.sets)):
            values = []
            print("\n\n\nSet of characteristics:", self.sets[j])
            for k in range(1, 16):
                self.k = k
                result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                counter = 0

                for i in range(len(self.data_test)):
                    real_type = int(self.data_test[i][4])
                    guessed_type = self.classification(self.data_test[i], j)
                    result = self.mistake_matrix(result, real_type, guessed_type)
                for i in range(3):
                    counter = counter + result[i][i]
                values.append(float((counter * 100) / len(self.data_test)))

            max_value_id = np.argmax(values) + 1
            result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            counter = 0
            print('k nearest neighbors: ' + str(max_value_id))
            print("           se, ve, vi")
            for i in range(len(self.data_test)):
                real_type = int(self.data_test[i][4])
                guessed_type = self.classification(self.data_test[i], j)
                result = self.mistake_matrix(result, real_type, guessed_type)
            self.matrix(result)
            self.plots(values, j)
