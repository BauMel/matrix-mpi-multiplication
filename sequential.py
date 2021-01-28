import numpy as np

def simple_matrix_multiplication(m1,m2):
    # get number of column of first matrix
    # len1 = len(np.array(m1)[:,0])
    # get number of line of second matrix
    # len2 = len(np.array(m2)[0])
    if len(m1[0]) == len(m2):
    # init res matrix 
        res_matrix = np.zeros((len(m1), len(m2[0])))
        # iterate through rows of m1
        for i in range(len(m1)):
            # iterate through columns of m2
            for j in range(len(m2[0])):
                # iterate through rows of m2
                for k in range(len(m2)):
                    res_matrix[i][j] += m1[i][k] * m2[k][j]

        for r in res_matrix:
            print(r)

        return res_matrix
    else:
         print('Les matrices ne sont pas de tailles compatibles Aucun Résultat')   