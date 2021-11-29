def countingSort(A,B,k):
    C=[]
    for i in range(k):
        C.append(0)
        B.append(0)
    for j in range(1, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1,k):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] -1
    return B

A=[2,5,3,0,2,3,0,3,1]
k = len(A)
B=[]
print(countingSort(A,B,k))