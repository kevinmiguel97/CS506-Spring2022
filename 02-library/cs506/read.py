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




