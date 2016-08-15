# Matrix and Vector classes ###################################################################
# Python v3.4.3
# ~~~~Created by David M Carter (2016)~~~~
#
############
#  MATRIX  #
############
#
#  A = Matrix(n,m)    Creates a Matrix object, A, of dimensions (n x m)
#                     All elements of a new Matrix object are initialized to 0
#
#  A[i,j]             Points to element A_(i,j)
#                     0 <= i <= (n-1)
#                     0 <= j <= (m-1)
#
#  A + e              Returns a Matrix object that is the sum of A and e
#                     (e must be one of {Matrix, int, float})
#
#  A - e              Returns a Matrix object that is the difference of A and e
#                     (e must be one of {Matrix, int, float})
#
#  A * e              Returns a Matrix object that is the product of A and e
#                     (e must be one of {Matrix, Vector, int, float})
#                     A.m() must equal e.n() in the Vector or Matrix case
#
#
#  MATRIX ATTRIBUTES:
#
#    A.n()              Returns the number of rows in Matrix A
#    A.m()              Returns the number of columns in Matrix A
#
#    A.getRow(i)        Returns a Vector object containing the elements of row i of A
#                       0 <= i <= (n-1)
#
#    A.getCol(j)        Returns a Vector object containing the elements of column j of A
#                       0 <= j <= (m-1)
#
#    A.isSquare()       (Boolean) check if a Matrix object A is a square matrix (n x n)
#
#    A.getDiag()        Returns a Vector object containing the main diagonal elements of A
#
#
#  MATRIX METHODS:
#
#    matsSameDim(A,B)   (Boolean) Check if Matrix objects A,B have the same dimensions
#
#    transpose(A)        Returns a Matrix object that is the transpose of A
#                        Vector transpose not supported (or needed)
#
#
###########
# VECTOR  #
###########
#
#  x = Vector(n)      Creates a Vector object, x, of dimension n
#                     All elements of a new Vector object are initialized to 0
#
#  x[i]               Returns element x_i
#                     0 <= i <= (n-1)
#
#  x + e              Returns a Vector object that is the sum of x and e
#                     (e must be one of {Vector, int, float})
#
#  x - e              Returns a Vector object that is the difference of x and e
#                     (e must be one of {Vector, int, float})
#
#  A * e              Returns a Vector object that is the product of x and e
#                     (e must be one of {int, float})
#
#  VECTOR ATTRIBUTES:
#
#    x.n()              Returns the dimension of Vector x (number of rows or columns)
#
#    x.l2Norm()         Returns the l2-norm of Vector object x
#
#    x.maxNorm()        Returns the l(inf)-norm (max norm) of Vector object x
#
#
#  VECTOR METHODS:
#
#    dotProduct(x,y)    Returns the dot product of Vectors x,y
#
#    vectsSameDim(x,y)  (Boolean) Check if Vector objects x,y have the same dimension
#
#######################
# ADDITIONAL METHODS  #
#######################
#
#  B = copy(A)        Returns a Matrix or Vector object with the elements from A copied over
#
###############################################################################################

import math

#(BOOLEAN) Check if two numbers are equal using a tolerance of 1e-16
def isEqual(a, b):
    tolerance = 1.0e-16
    return (abs (a-b) < tolerance)

def matsSameDim(matrixA, matrixB):
    if not (isinstance(matrixA, Matrix) and isinstance(matrixB, Matrix)):
        raise TypeError("(matsSameDim) must compare two Matrix objects")
    else:
        return ((matrixA.rows == matrixB.rows) and (matrixA.cols == matrixB.cols))

def vectsSameDim(vectorX, vectorY):
    if not (isinstance(vectorX, Vector) and isinstance(vectorY, Vector)):
        raise VectorError("(vectsSameDim) must compare two Vector objects")
    else:
        return (vectorX.cols == vectorY.cols)

def dotProduct(vectorX, vectorY):
    if not (isinstance(vectorX, Vector) and isinstance(vectorY, Vector)):
        raise TypeError("(dotProduct) must dot two Vector objects")
    elif not vectsSameDim(vectorX,vectorY):
        raise VectorError("(dotProduct) must dot Vectors of same dimension")
    else:
        s = 0
        for i in range(vectorX.n()):
            s += vectorX[i]*vectorY[i]
        return s

def transpose(matrix):
    if not isinstance(matrix, Matrix):
        raise MatrixError("(transpose) method only operates on Matrix objects")
    else:
        transpose = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                transpose.data[j][i] = matrix.data[i][j]
        return transpose

def copy (matOrVect):
    if isinstance(matOrVect, Matrix):
        copy = Matrix(matOrVect.n(), matOrVect.m())
        for i in range(matOrVect.n()):
            for j in range(matOrVect.m()):
                copy.data[i][j] = matOrVect.data[i][j]
        return copy
    elif isinstance(matOrVect, Vector):
        copy = Vector(matOrVect.n())
        for i in range(matOrVect.n()):
            copy.data[i] = matOrVect.data[i]
        return copy
    else:
        raise TypeError("(copy) method only operates on Matrix or Vector objects")


class Error(Exception):
    pass

class MatrixError(Error):
    def __init__(self, msg):
        self.msg = msg

class VectorError(Error):
    def __init__(self, msg):
        self.msg = msg
        

class Matrix():

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        if (self.rows < 1):
            raise MatrixError("(Matrix initialization) Rows must be >= 1")
        elif (self.cols < 1):
            raise MatrixError("(Matrix initialization) Columns must be >= 1")

        else:
            self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __setitem__(self, index, data):
        self.data[index[0]][index[1]] = data

    def __getitem__(self, index):
        return self.data[index[0]][index[1]]

    def __add__(matrix, matrixOrNumber):
        if (isinstance(matrix, Matrix) and isinstance(matrixOrNumber, Matrix)):
            if not (matsSameDim(matrix, matrixOrNumber)):
                raise MatrixError("(Matrix Addition) matrices have non-equal dimension")
            else:
                matSum = copy(matrix)
                for i in range(matrix.rows):
                    for j in range(matrix.cols):
                        matSum.data[i][j] += matrixOrNumber.data[i][j]
                return matSum
            
        elif (isinstance(matrix, Matrix) and isinstance(matrixOrNumber, (int, float))):
            matSum = copy(matrix)
            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    matSum.data[i][j] += matrixOrNumber
            return matSum

        else:
            raise TypeError("(Matrix Addition) must use Matrix and one of {Matrix, int, float}")

    def __sub__(matrix, matrixOrNumber):
        if (isinstance(matrix, Matrix) and isinstance(matrixOrNumber, Matrix)):
            if not (matsSameDim(matrix, matrixOrNumber)):
                raise MatrixError("(Matrix Subtraction) matrices have non-equal dimension")
            else:
                matDiff = copy(matrix)
                for i in range(matrix.rows):
                    for j in range(matrix.cols):
                        matDiff.data[i][j] -= matrixOrNumber.data[i][j]
                return matDiff
            
        elif (isinstance(matrix, Matrix) and isinstance(matrixOrNumber, (int, float))):
            matDiff = copy(matrix)
            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    matDiff.data[i][j] -= matrixOrNumber
            return matDiff

        else:
            raise TypeError("(Matrix Subtraction) must use Matrix and one of {Matrix, int, float}")

    def __mul__(matrix, matNumVec):
        if (isinstance(matrix, Matrix) and isinstance(matNumVec, Matrix)):
            if not (matrix.m() == matNumVec.n()):
                raise MatrixError("(Matrix Multiplication) left matrix column number does not equal right matrix row number")
            else:
                product = Matrix(matrix.n(), matNumVec.m())
                for i in range(product.rows):
                    for j in range(product.cols):
                        product.data[i][j] = dotProduct(matrix.getRow(i), matNumVec.getCol(j))
                return product
        elif (isinstance(matrix, Matrix) and isinstance(matNumVec, (int, float))):
            product = copy(matrix)
            for i in range(matrix.rows):
                for j in range(matrix.rows):
                    product.data[i][j] *= matNumVec
            return product
        elif (isinstance(matrix, Matrix) and isinstance(matNumVec, Vector)):
            if not (matrix.m() == matNumVec.n()):
                raise MatrixError("(Matrix Multiplication) matrix row number must equal vector row number")
            else:
                product = copy(matrix)
                for i in range(matrix.rows):
                    for j in range(matrix.cols):
                        product.data[i][j] = matrix.data[i][j]*matNumVec.data[j]
                return product
        else:
            raise TypeError("(Matrix Multiplication) must use Matrix and one of {Matrix, Vector, int, float}")


    def __eq__(self, other):
        flag = False
        if matsSameDim(self, other):
            flag = True
            for i in range(self.rows):
                for j in range(self.cols):
                    if not isEqual(self.data[i][j], other.data[i][j]):
                        flag = False
        return flag

    def __str__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.cols):
                s += str(self.data[i][j])
                if not(j == (self.cols - 1)): s += " "
            if not(i == (self.rows - 1)): s += "\n"
        return s

    def n(self):
        return self.rows

    def m(self):
        return self.cols

    def getRow(self, rowIndex):
        if ((rowIndex < 0) or (rowIndex >= self.rows)):
            raise MatrixError("(getRow) index out of bounds")
        else:
            row = Vector(self.cols)
            for col in range(self.cols):
                row[col] = self.data[rowIndex][col]
            return row

    def getCol(self, colIndex):
        if ((colIndex < 0) or (colIndex >= self.cols)):
            raise MatrixError("(getCol) index out of bounds")
        else:
            col = Vector(self.rows)
            for row in range(self.rows):
                col[row] = self.data[row][colIndex]
            return col

    def getDiag(self):
        if not self.isSquare():
            raise MatrixError("(getDiag) not a square matrix")
        else:
            x = Vector(self.n())
            for i in range(self.cols):
                x.data[i] = self.data[i][i]
            return x

    def isSquare(self):
        return(self.n() == self.m())



class Vector():

    def __init__(self, dimension):
        self.cols = dimension

        if (self.cols < 1):
            raise VectorError("(Vector initialization) dimension must be >= 1")

        else:
            self.data = [0 for i in range(self.cols)]

    def __setitem__(self, index, data):
        self.data[index] = data

    def __getitem__(self, index):
        return self.data[index]

    def __add__(vector, vectorOrNumber):
        if (isinstance(vector, Vector) and isinstance(vectorOrNumber, Vector)):
            if not (vectsSameDim(vector, vectorOrNumber)):
                raise VectorError("(Vector Addition) vectors have non-equal dimension")
            else:
                vectSum = copy(vector)
                for j in range(vector.cols):
                    vectSum.data[j] += vectorOrNumber.data[j]
                return vectSum
            
        elif (isinstance(vector, Vector) and isinstance(vectorOrNumber, (int, float))):
            vectSum = copy(vector)
            for j in range(vector.cols):
                    vectSum.data[j] += vectorOrNumber
            return vectSum

        else:
            raise TypeError("(Vector Addition) must use Vector and one of {Vector, int, float}")

    def __sub__(vector, vectorOrNumber):
        if (isinstance(vector, Vector) and isinstance(vectorOrNumber, Vector)):
            if not (vectsSameDim(vector, vectorOrNumber)):
                raise VectorError("(Vector Addition) vectors have non-equal dimension")
            else:
                vectSum = copy(vector)
                for j in range(vector.cols):
                    vectSum.data[j] -= vectorOrNumber.data[j]
                return vectSum
            
        elif (isinstance(vector, Vector) and isinstance(vectorOrNumber, (int, float))):
            vectSum = copy(vector)
            for j in range(vector.cols):
                    vectSum.data[j] -= vectorOrNumber
            return vectSum

        else:
            raise TypeError("(Vector Addition) must use Vector and one of {Vector, int, float}")

    def __mul__(vector, number):
        if not (isinstance(vector, Vector) and isinstance(number, (int, float))):
            raise TypeError("(Vector Multiplication) must multiply by a scalar")
        else:
            vectProd = copy(vector)
            for j in range(vector.cols):
                vectProd.data[j] *= number
            return vectProd

    def __eq__(self, other):
        flag = False
        if vectsSameDim(self, other):
            flag = True
            for i in range(self.cols):
                if not isEqual(self.data[i], other.data[i]):
                    flag = False
        return flag

    def __str__(self):
        s = ""
        for i in range(self.cols):
            s += str(self.data[i])
            if not(i == (self.cols - 1)): s+= " "
        return s

    def n(self):
        return self.cols

    def l2Norm(self):
        s = 0
        for i in range(self.cols):
            s += (self.data[i] * self.data[i])
        s = math.sqrt(s)
        return s;

    def maxNorm(self):
        m = 0
        for i in range(self.cols):
            if (self.data[i] > m):
                m = self.data[i]
        return m
