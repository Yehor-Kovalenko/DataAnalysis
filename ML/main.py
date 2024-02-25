import csv

from KMeans_Alg import KMeans
from KNN_Alg import KNN

# read csv
with open('data_train.csv', newline='') as csvfile:
    data_train = list(csv.reader(csvfile))
with open('data_test.csv', newline='') as csvfile:
    data_test = list(csv.reader(csvfile))
with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

########           K-MEANS               ###########################################
k = 3
kmeans = KMeans(data, k)
arr = kmeans.fit()

kmeans.draw_scatter(arr[0], 0, 1, 'Długość działki kielicha [cm]', 'Szerokość działki kielicha [cm]')
kmeans.draw_scatter(arr[0], 0, 2, 'Długość działki kielicha [cm]', 'Długość płatka [cm]')
kmeans.draw_scatter(arr[0], 0, 3, 'Długość działki kielicha [cm]', 'Szerokość płatka [cm]')
kmeans.draw_scatter(arr[0], 1, 2, 'Szerokość działki kielicha [cm]', 'Długość płatka [cm]')
kmeans.draw_scatter(arr[0], 1, 3, 'Szerokość działki kielicha [cm]', 'Szerokość płatka [cm]')
kmeans.draw_scatter(arr[0], 2, 3, 'Długość płatka [cm]', 'Szerokość płatka [cm]')

iterations = []
wcss = []

for i in range(2, 11):
    kmeans = KMeans(data, i)
    array_info = kmeans.fit()
    iterations.append(array_info[1])
    wcss.append(kmeans.wcss(array_info[0]))
kmeans.draw_lin(iterations, 'Liczba iteracji')
kmeans.draw_lin(wcss, 'Wartość WCSS')


knn = KNN(data_train, data_test)
KNN.kNN(knn)
