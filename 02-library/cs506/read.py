def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    import numpy as np
    file = open(csv_file_path)
    matrix = np.loadtxt(file, delimeter=',')
    return matrix

    #raise NotImplementedError()

#matrix = read_csv('Matrix.csv', decode='utf-8')

import csv
rows = []
with open("Matrix.csv", 'r) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
