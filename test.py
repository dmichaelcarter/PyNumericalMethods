from LinAlg import *

def test():
    A = Matrix(2,3)
    A[0,0] = 1
    A[0,1] = 2
    A[0,2] = 3
    A[1,0] = 4
    A[1,1] = 5
    A[1,2] = 6
    print("A:")
    print(A, "\n")

    B = Matrix(3,2)
    B[0,0] = 1.01
    B[0,1] = 3.14
    B[1,0] = 2.71
    B[1,1] = 7.89
    B[2,0] = 2.02
    B[2,1] = 3.03
    print("B:")
    print(B, "\n")

    print("A * B:")
    print(A*B, "\n")

    C = copy(A)
    print("C:")
    print(C, "\n")
    print("C == A:", (C == A), "\n")
    
    C[0,0] = 1 + 1e-16
    print("C[0,0] = 1 + 1e-16:")
    print(C, "\n")
    print("C == A:", (C == A), "\n")

    C[0,0] = 1 + 2e-16
    print("C[0,0] = 1 + 2e-16:")
    print(C, "\n")
    print("C == A:", (C == A), "\n")

    print("transpose(A):")
    print(transpose(A), "\n")

    x = Vector(2)
    x[0] = 10
    x[1] = 20
    print("x: ")
    print(x, "\n")

    print("transpose(A) * x:")
    print(transpose(A)*x, "\n")

test()
input()

