# Jacobian Method #############################################################################
# Python v3.4.3
# ~~~~Created by David M Carter (2016)~~~~
#
# This program uses the Jacobian method to solve a linear system of equations
# of the form Ax = b
#
# There must not be any entries A[i,i] equal to 0
#
# INPUT:
#           A          coefficients (matrix)
#           b          right-hand side of equations (vector)
#           x0         initial guess to solution
#           tol        desired tolerance
#           maxIter    maximum number of iteration
#
# OUTPUT:
#           x          approximation of system solution (vector)
#
# RETURN TYPE:         vector object
#
###############################################################################################

from LinAlg import *
import math

def jacobi(A, b, x0, tol, maxIter):
    k = 0
    x = Vector(b.n())
    xOld = copy(x0)

    while (k < maxIter):
        for i in range(x.n()):
            d = 0.0
            for j in range(x.n()):
                if (j==i):
                    continue
                d += (A[i,j] * xOld[j])
            x[i] = (d*(-1.0) + b[i]) / A[i,i]

        if ((x - xOld).maxNorm() < tol):
            print("Solution approximated in " + str(k) + " iterations.")
            return x

        k +=1

        for i in range(x.n()):
            xOld[i] = x[i]
            
    print("Exceeded maximum number of iterations")
    

def main():
    print("MATRIX A")
    A = promptMatrix()
    print("\n")

    print("VECTOR b")
    b = promptVector()
    print("\n")

    print("INTIAL GUESS x0")
    x0 = promptVector()
    print("\n")
    
    tolIter = eval(input("Enter tolerance and maximum iterations: tol, maxIter = "))
    tol = tolIter[0]
    maxIter = tolIter[1]
    print("\n")

    x = jacobi(A, b, x0, tol, maxIter)
    print(x)
    
main()

