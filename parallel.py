from mpi4py import MPI as mpi
import numpy as np


def join(matrix):
    result_vector = []
    for line in matrix:
        for value in line:
            result_vector.append(value)
    return result_vector


def doSumVectors(vector1, vector2):
    result_sum = 0
    if len(vector1) != len(vector2):
        print('@@@@@@@@@@@@@@@@@@@@@')
    else:
        for i in range(0, len(vector1)):
            result_sum = result_sum + vector1[i]*vector2[i]
        return result_sum

def doProductVectorsMatrix(vectors, mat):
    product_vector = []
    if len(vectors) is not len(mat[0]):
        print("Le Nombre de Colone de la premiere matrice doit etre egale au nombre de ligne de la deuxieme matrice.")
    else:
        for line in mat:
            sum_vector = doSumVectors(vectors, line)
            product_vector.append(sum_vector)
        return product_vector


def productMatrixMatrix(m1, m2):
    product_matrix = []
    if len(m1[0]) is not len(m2[0]):
        print("Veuillez entrez les matrices de meme taille")
    else:
        for line in m1:
            product_VM = doProductVectorsMatrix(line, m2)
            product_matrix.append(product_VM)
        return product_matrix

def parallelProductMatrix(m1, m2):
    comm = mpi.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    number_of_sub_matrix = len(m1) // size
    m1_ = None
    m2_ = None

    if rank == 0:
        m1_ = np.array(m1)
        m2_ = np.array(m2)
    
    # decoupage de la matrice1 et transmission au different processeur
    recv_buf = np.empty([number_of_sub_matrix, len(m1[0])], dtype=int)
    comm.Scatterv(m1_, recv_buf, root=0)
    print("Processeur:", rank, ", Sous_Vecteur:", recv_buf)
    print('\n')

    # Difjoin de la deuxieme matrice a tout les processeurs
    if rank != 0:
        m2_ = np.empty([len(m2)], dtype=int)
    if rank == 0:
        comm.send(m2_, dest = 1)
    elif rank == 1:
        m2_ = comm.recv(source=0)
    #comm.Bcast(m2_, root=0)
    print('Processeur:', rank, ", Matrice: ", m2_) 

    m1_ = productMatrixMatrix(recv_buf, m2_)
    print('Processeur:', rank, ', result :', m1_)

    recvbuf_ = None
    if rank == 0:
        recvbuf_ = np.empty([1, len(m1_)], dtype=int)

    res = comm.gather(m1_, root=0)

    if rank == 0:
        print('Processeur :', rank, ', Result :', res)
        result_vector = join(res)
        print(result_vector)

# def product_matrix_vectors(matrix, vectors):
#     product_vector = []
#     if len(vectors) is not len(matrix[0]):
#         print("Le Nombre de Colone de la premiere matrice doit etre egale au nombre de ligne de la deuxieme matrice.")
#     else:
#         for line in matrix:
#             sum_vestor = doSumVectors(line, vectors)
#             product_vector.append(sum_vector)
#         return product_vector        