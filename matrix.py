#Splits the matrix [string] into
#an integer list
import math


def spliter(matrix):
    new_matrix = matrix.split(',')
    if math.sqrt(len(new_matrix)) is not int:
        return False, []
    else:
        return True, new_matrix

# def Gaussian_Inverse(matrix):