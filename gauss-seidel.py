# Gauss-Seidel Method #########################################################################
# Python v3.4.3
# ~~~~Created by David M Carter (2016)~~~~
#
# This program uses the Gauss-Seidel method to solve a linear system of equations
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
# OUTPUT
#                      number of iterations
#           x          approximation of system solution (vector object returned)
#
# RETURN TYPE:         vector object
#
###############################################################################################

from LinAlg import *
import math

def gs(A, b, x0, tol, maxIter):
    iteration = 0
    x = Vector(b.n())
    xOld = copy(x0)

    while (iteration < maxIter):
        for i in range(1, x.n() + 1):
            sum1 = 0.0
            sum2 = 0.0
            for j in range(1,i):
                sum1 += (A[i-1,j-1] * x[j-1])
            for k in range(i+1, x.n()+1):
                sum2 += (A[i-1,k-1] * xOld[k-1])
            x[i-1] = (sum1*(-1) - sum2 + b[i-1]) / A[i-1,i-1]

        if ((x - xOld).maxNorm() < tol):
            print("Solution approximated in " + str(iteration) + " iterations.")
            return x

        iteration +=1

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

    x = gs(A, b, x0, tol, maxIter)
    print(x)
    
main()

