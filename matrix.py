import random
import operator
import sys
import unittest

class MatrixError(Exception):
    """ An exception class for Matrix """
    pass

class Matrix(object):
    """ A simple Python Matrix class with
    basic operations and operator overloading """
    
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
        
    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return rep
    
    def reset(self):
        """ Reset the matrix data """
        self.rows = [[] for x in range(self.m)]

    def getRank(self):
        return (self.m, self.n)

    def __eq__(self, mat):
        """ Test equality """

        return (mat.rows == self.rows)
        
    def __add__(self, mat):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getRank() != mat.getRank():
            raise MatrixError, "Trying to add matrixes of varying rank!"

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        """ Subtract a matrix from this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getRank() != mat.getRank():
            raise MatrixError, "Trying to add matrixes of varying rank!"

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [item[0]-item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        """ Multiple a matrix with this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        matm, matn = mat.getRank()
        
        if (self.n != matm):
            raise MatrixError, "Matrices cannot be multipled!"
        
        mat_t = mat.getTranspose()
        mulmat = Matrix(self.m, matn)
        
        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], mat_t[y])])

        return mulmat

    def __iadd__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Calls __add__
        tempmat = self + mat
        self.rows = tempmat.rows[:]
        return self

    def __isub__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Calls __sub__
        tempmat = self - mat
        self.rows = tempmat.rows[:]     
        return self

    def __imul__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Possibly not a proper operation
        # since this changes the current matrix
        # rank as well...
        
        # Calls __mul__
        tempmat = self * mat
        self.rows = tempmat.rows[:]
        self.m, self.n = tempmat.getRank()
        return self

    def save(self, filename):
        open(filename, 'w').write(str(self))
        
