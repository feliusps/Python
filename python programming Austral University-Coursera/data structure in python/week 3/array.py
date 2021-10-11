#working with matrices

#define a matrix
mat_a = [[1,2,3,4],
        [5,6,7,8],
        [9, 10, 11, 12],]

#element access
print(mat_a[0][0])
print()
print(mat_a[1][2])

#function matrices addition

def mat_addition(A, B):
    
    #A and B must be the same size 
    row_size = len(A)
    col_size = len(A[0])
    C =[]

    for row in range(row_size):
        row_sum = []
        for col in range(col_size):
            row_sum.append(A[row][col] + B[row][col])
        C.append(row_sum)
    return C

A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]

print(mat_addition(A, B))