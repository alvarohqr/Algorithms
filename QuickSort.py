def partition(A, p, r):
    x = A[r]
    i = p - 1
     
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1
    
    
def QuickSort (A, p, r):
    if p<r:
        q = partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A

A = [2,8, 7, 1, 3, 5, 6, 4]
p = 0
r = len(A)-1

print(QuickSort(A,p,r))
